#!/usr/bin/env python3
'''YOLO Object Detection Module'''
import tensorflow.keras as K
import numpy as np


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

        boxes = []
        box_confidences = []
        box_class_probs = []

        for i in range(len(outputs)):
            output = outputs[i]

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

                        x1 = (b_x - b_w / 2) * image_size[1]
                        x2 = (b_x + b_w / 2) * image_size[1]
                        y1 = (b_y - b_h / 2) * image_size[0]
                        y2 = (b_y + b_h / 2) * image_size[0]

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
