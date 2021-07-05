#!/usr/bin/env python3
'''YOLO Object Detection Module'''
import tensorflow.keras as K
import numpy as np
import cv2


class Yolo():
    '''Uses the Yolo v3 algorithm to perform object detection'''

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        '''class initializer
        Args:
            model_path is the path to where a Darknet Keras model is stored
            classes_path is the path to where the list of class names used for
                         the Darknet model, listed in order of index, can be
                         found
            class_t is a float representing the box score threshold for the
                    initial filtering step
            nms_t is a float representing the IOU threshold for non-max
                  suppression
            anchors is a numpy.ndarray of shape (outputs, anchor_boxes, 2)
                    containing all of the anchor boxes:
                    - outputs is the number of outputs (predictions) made by
                              the Darknet model
                    - anchor_boxes is the number of anchor boxes used for each
                                   prediction
                    - 2 => [anchor_box_width, anchor_box_height]
        '''
        self.model = K.models.load_model(model_path)
        self.class_names = []
        with open(classes_path, encoding='utf-8') as f:
            for line in f:
                self.class_names.append(line[:-1])
        self.class_t = float(class_t)
        self.nms_t = float(nms_t)
        self.anchors = anchors

    def process_outputs(self, outputs, image_size):
        '''method tha process Darknet model outputs
        Args:
            outputs is a list of numpy.ndarrays containing the predictions
                    from the Darknet model for a single image:
                    - Each output will have the shape (grid_height, grid_width,
                      anchor_boxes, 4 + 1 + classes)
                        - grid_height & grid_width => the height and width of
                          the grid used for the output
                        - anchor_boxes => the number of anchor boxes used
                        - 4 => (t_x, t_y, t_w, t_h)
                        - 1 => box_confidence
                        - classes => class probabilities for all classes
            image_size is a numpy.ndarray containing the image’s original size
                       [image_height, image_width]
        Returns a tuple of (boxes, box_confidences, box_class_probs):
                - boxes: a list of numpy.ndarrays of shape (grid_height,
                         grid_width,  anchor_boxes, 4) containing the processed
                         boundary boxes for each output, respectively:
                          - 4 => (x1, y1, x2, y2)
                          - (x1, y1, x2, y2) should represent the boundary box
                            relative to original image
                - box_confidences: a list of numpy.ndarrays of shape
                                   (grid_height, grid_width, anchor_boxes, 1)
                                   containing the box confidences for each
                                   output, respectively
                - box_class_probs: a list of numpy.ndarrays of shape
                                   (grid_height, grid_width, anchor_boxes,
                                   classes) containing the box’s class
                                   probabilities for each output, respectively
        '''
        def _sigmoid(x):
            '''sigmoid function'''
            return 1 / (1 + np.exp(-x))

        input_h, input_w = self.model.inputs[0].shape.as_list()[1:3]
        image_h, image_w = image_size

        boxes = []
        box_confidences = []
        box_class_probs = []

        for i, output in enumerate(outputs):

            grid_h, grid_w = output.shape[:2]
            n_b = output.shape[2]  # YOLOv3 preds boxes at 3 different scales
            n_classes = output.shape[-1] - 4 - 1

            output[..., :2] = _sigmoid(output[..., :2])  # sig for t_x & t_y
            output[..., 4:] = _sigmoid(output[..., 4:])  # sig for all probs

            box = np.empty((grid_h, grid_w, n_b, 4))
            confidence = np.empty((grid_h, grid_w, n_b, 1))
            classes_probs = np.empty((grid_h, grid_w, n_b, n_classes))

            for row in range(grid_h):
                for col in range(grid_w):
                    for b in range(n_b):

                        t_x, t_y, t_w, t_h = output[row][col][b][:4]
                        b_x = (t_x + col) / grid_w  # center x position
                        b_y = (t_y + row) / grid_h  # center y position

                        anchor = self.anchors[i][b]
                        pw = anchor[0]
                        b_w = (pw * np.exp(t_w)) / input_w
                        ph = anchor[1]
                        b_h = (ph * np.exp(t_h)) / input_h

                        x1 = (b_x - b_w / 2) * image_w
                        x2 = (b_x + b_w / 2) * image_w
                        y1 = (b_y - b_h / 2) * image_h
                        y2 = (b_y + b_h / 2) * image_h

                        box[row, col, b, :] = [x1, y1, x2, y2]
                        confidence[row, col, b] = output[row][col][b][4]
                        classes_probs[row, col, b] = output[row][col][b][5:]

            boxes.append(box)
            box_confidences.append(confidence)
            box_class_probs.append(classes_probs)

        return (boxes, box_confidences, box_class_probs)

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        '''method that filter boxes with the given threshold
        Args:
            boxes: a list of numpy.ndarrays of shape (grid_height, grid_width,
                   anchor_boxes, 4) containing the processed boundary boxes for
                   each output, respectively
            box_confidences: a list of numpy.ndarrays of shape (grid_height,
                             grid_width, anchor_boxes, 1) containing the
                             processed box confidences for each output,
                             respectively
            box_class_probs: a list of numpy.ndarrays of shape (grid_height,
                             grid_width, anchor_boxes, classes) containing the
                             processed box class probabilities for each output,
                             respectively
        Returns: a tuple of (filtered_boxes, box_classes, box_scores):
            filtered_boxes: a numpy.ndarray of shape (?, 4) containing all of
                            the filtered bounding boxes:
            box_classes: a numpy.ndarray of shape (?,) containing the class
                         number that each box in filtered_boxes predicts,
                         respectively
            box_scores: a numpy.ndarray of shape (?) containing the box scores
                        for each box in filtered_boxes, respectively
        '''
        filtered_boxes = []
        box_classes = []
        box_scores = []

        threshold = self.class_t

        for i, box in enumerate(boxes):
            this_box_confidences = box_confidences[i]
            this_box_cps = box_class_probs[i]
            this_box_scores = this_box_confidences * this_box_cps
            this_box_classes = np.argmax(this_box_scores, axis=-1)
            this_box_class_scores = np.max(this_box_scores, axis=-1)
            idxs = np.where(this_box_class_scores > threshold)

            filtered_boxes.append(box[idxs])
            box_classes.append(this_box_classes[idxs])
            box_scores.append(this_box_class_scores[idxs])

        filtered_boxes = np.concatenate(filtered_boxes)
        box_classes = np.concatenate(box_classes)
        box_scores = np.concatenate(box_scores)

        return (filtered_boxes, box_classes, box_scores)

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        '''method that performs non max suppresion (NMS)
        Args:
            filtered_boxes: a numpy.ndarray of shape (?, 4) containing all of
                            the filtered bounding boxes:
            box_classes: a numpy.ndarray of shape (?,) containing the class
                         number for the class that filtered_boxes predicts,
                         respectively
            box_scores: a numpy.ndarray of shape (?) containing the box scores
                        for each box in filtered_boxes, respectively
        Returns: a tuple of (box_predictions, predicted_box_classes,
                 predicted_box_scores):
            box_predictions: a numpy.ndarray of shape (?, 4) containing all of
                             the predicted bounding boxes ordered by class and
                             box score
            predicted_box_classes: a numpy.ndarray of shape (?,) containing the
                                   class number for box_predictions ordered by
                                   class and box score, respectively
            predicted_box_scores: a numpy.ndarray of shape (?) containing the
                                  box scores for box_predictions ordered by
                                  class and box score, respectively
        '''
        # =========================================================
        def _iou(box_a, box_b):
            '''Calculates the intersection over union of two boxes
            Args:
                box_a: the first box
                box_b: the second box
            Returns: the IOU between the boxes
            '''
            x1a, y1a, x2a, y2a = box_a
            x1b, y1b, x2b, y2b = box_b

            x1 = max(x1a, x1b)
            y1 = max(y1a, y1b)
            x2 = min(x2a, x2b)
            y2 = min(y2a, y2b)

            intersection = max(0, y2 - y1) * max(0, x2 - x1)
            box_a_area = (x2a - x1a) * (y2a - y1a)
            box_b_area = (x2b - x1b) * (y2b - y1b)
            union = box_a_area + box_b_area - intersection

            return intersection / union

        # =========================================================

        threshold = self.nms_t

        # Order by class and box score
        sort = np.lexsort((-box_scores, box_classes))
        classes_ord = box_classes[sort]
        boxes_ord = filtered_boxes[sort]
        scores_ord = box_scores[sort]

        selected_idxs = []
        descarted_idxs = []
        found_classes = np.unique(box_classes)

        # Searches boxes in each class,
        # the first box has the highest score
        for cls in found_classes:
            idx = np.where(classes_ord == cls)
            comparables = boxes_ord[idx]
            n_comparables = len(comparables)
            for i in range(n_comparables):
                c_idx = idx[0][i]
                if c_idx not in descarted_idxs:
                    selected_idxs.append(c_idx)
                    b1 = comparables[i]
                else:
                    continue
                for j in range(i + 1, n_comparables):
                    b2 = comparables[j]

                    # If IOU is big, the boxes id the same object,
                    # the second box is descarted
                    if _iou(b1, b2) > threshold:
                        descarted_idxs.append(idx[0][j])

        box_predictions = boxes_ord[selected_idxs]
        predicted_box_classes = classes_ord[selected_idxs]
        predicted_box_scores = scores_ord[selected_idxs]

        return (box_predictions, predicted_box_classes, predicted_box_scores)

    @staticmethod
    def load_images(folder_path):
        '''static method to load images
        Args:
            folder_path: a string representing the path to the folder holding
                         all the images to load
        Returns: a tuple of (images, image_paths):
                 - images: a list of images as numpy.ndarrays
                 - image_paths: a list of paths to the individual images in
                   images
        '''
        import glob

        images = []
        image_paths = glob.glob(folder_path + '/*.jpg')
        for img_path in image_paths:
            img = cv2.imread(img_path)
            images.append(img)
        return (images, image_paths)

    def preprocess_images(self, images):
        '''preprocess images to fit in the model
        Args:
            images: a list of images as numpy.ndarrays
        Important:
            - Images are resized  with inter-cubic interpolation
            - Images are rescaled to have pixel values in the range [0, 1]
        Returns: a tuple of (pimages, image_shapes):
                 - pimages: a numpy.ndarray of shape (ni, input_h, input_w, 3)
                            containing all of the preprocessed images
                            - ni: the number of images that were preprocessed
                            - input_h: the input height for the Darknet model
                                       Note: this can vary by model
                            - input_w: the input width for the Darknet model
                                       Note: this can vary by model
                            - 3: number of color channels
                 - image_shapes: a numpy.ndarray of shape (ni, 2) containing
                                 the original height and width of the images
                                 - 2 => (image_height, image_width)
        '''
        # Capture the input size of the model
        # for Darknet it is 416x416
        input_h, input_w = self.model.inputs[0].shape.as_list()[1:3]

        pimages = []
        image_shapes = []

        for img in images:

            # Resize image:
            pimg = cv2.resize(img,
                              (input_h, input_w),
                              interpolation=cv2.INTER_CUBIC)

            # Normalize image:
            pimg = pimg / 255
            pimages.append(pimg)

            # Original shape:
            img_shape = (img.shape[0], img.shape[1])
            image_shapes.append(img_shape)

        pimages = np.array(pimages)
        image_shapes = np.array(image_shapes)

        return (pimages, image_shapes)

    def show_boxes(self, image, boxes, box_classes, box_scores, file_name):
        '''print boxes (if any) over the objects in the image
        Args:
            image: a numpy.ndarray containing an unprocessed image
            boxes: a numpy.ndarray containing the boundary boxes for the image
            box_classes: a numpy.ndarray containing the class indices for each
                         box
            box_scores: a numpy.ndarray containing the box scores for each box
            file_name: the file path where the original image is stored
        '''
        import os

        dir_to_save = './detections/'

        for i, box in enumerate(boxes):
            # drawing the box
            x1, y1, x2, y2 = box
            start_point = (int(x1), int(y1))
            end_point = (int(x2), int(y2))
            box_color = (255, 0, 0)  # blue
            font_color = (0, 0, 255)  # red
            cv2.rectangle(image,
                          start_point,
                          end_point,
                          box_color,
                          thickness=2)
            text = "{} {:.2f}".format(self.class_names[box_classes[i]],
                                      box_scores[i])

            # labeling the box
            cv2.putText(image,
                        text,
                        (start_point[0], start_point[1] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5,
                        color=font_color,
                        thickness=1,
                        lineType=cv2.LINE_AA)

        cv2.imshow(file_name, image)
        k = cv2.waitKey(0)

        # wait for 's' key to save and exit
        if k == ord('s'):
            try:
                os.makedirs(dir_to_save)
            except FileExistsError:
                pass
            cv2.imwrite(dir_to_save + file_name, image)
        cv2.destroyAllWindows()

    def predict(self, folder_path):
        '''predicts boxes for each image in the folder
        Args:
            folder_path: a string representing the path to the folder holding
                         all the images to predict
        Returns: a tuple of (predictions, image_paths):
                 - predictions: a list of tuples for each image of
                   (boxes, box_classes, box_scores)
                 - image_paths: a list of image paths corresponding to each
                   prediction in predictions
        '''
        images, image_paths_full = Yolo.load_images(folder_path)

        pimages, image_shapes = self.preprocess_images(images)

        model_predictions = self.model.predict(pimages)

        predictions = []
        image_paths = []

        # if model_predictions were a ndarray, it would have a shape
        # (3, n_images, 4), and we need it in shape (n_images, 3, 4):
        model_pred_adj = []
        for i in range(len(images)):
            output = []
            for j in range(len(model_predictions)):
                output.append(model_predictions[j][i])
            model_pred_adj.append(output)

        for i, output in enumerate(model_pred_adj):
            (boxes,
             box_confidences,
             box_class_probs) = self.process_outputs(
                 output,
                 image_shapes[i],
             )

            (filtered_boxes,
             box_classes,
             box_scores) = self.filter_boxes(
                 boxes,
                 box_confidences,
                 box_class_probs,
             )

            (box_predictions,
             predicted_box_classes,
             predicted_box_scores) = self.non_max_suppression(
                 filtered_boxes,
                 box_classes,
                 box_scores,
             )

            image_name = image_paths_full[i][len(folder_path) + 1:]
            self.show_boxes(
                images[i],
                box_predictions,
                predicted_box_classes,
                predicted_box_scores,
                image_name,
            )

            predictions.append((
                box_predictions,
                predicted_box_classes,
                predicted_box_scores))

            image_paths.append(image_name)

        return (predictions, image_paths)
