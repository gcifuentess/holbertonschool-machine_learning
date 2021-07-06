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
        image_h, image_w = image_size

        boxes = []
        box_confidences = []
        box_class_probs = []

        for i, output in enumerate(outputs):

            grid_h, grid_w = output.shape[:2]

            output[..., :2] = _sigmoid(output[..., :2])  # sig for t_x & t_y
            output[..., 4:] = _sigmoid(output[..., 4:])  # sig for all probs

            t_xy = output[..., 0:2]
            t_wh = output[..., 2:4]

            anchors = self.anchors[i]

            # -- Build the C_xy matrix (The grid for every anchor) --
            # # look Darknet e.g first scale shape transformation:
            # C_xy = np.indices((grid_w, grid_h))  # shape (2,13,13)
            # C_xy = np.expand_dims(C_xy, axis=-1)  # shape (2,13,13,1)
            # C_xy_ = C_xy.copy()
            # for i in range(anchors.shape[0] - 1):  # shape (2,13,13,3)
            #     C_xy = np.concatenate((C_xy, C_xy_), axis=-1)
            # C_xy = np.transpose(C_xy, axes=[1, 2, 3, 0])  # shape (13,13,3,2)
            C_xy = np.tile(np.indices((grid_w, grid_h)).T,
                           anchors.shape[0]).reshape(
                               (grid_h, grid_w) + anchors.shape)

            # Correct offset of the center points:
            b_xy = (t_xy + C_xy) / (grid_w, grid_h)
            # Correct offset of boxes dimensions:
            b_wh = (anchors * np.exp(t_wh)) / (input_w, input_h)

            # boxes coordinates with respect to the input image:
            xy1 = (b_xy - b_wh / 2) * (image_w, image_h)
            xy2 = (b_xy + b_wh / 2) * (image_w, image_h)

            boxes.append(np.concatenate((xy1, xy2), axis=-1))
            confidences = np.expand_dims(output[..., 4], axis=-1)
            box_confidences.append(confidences)
            box_class_probs.append(output[..., 5:])

        return (boxes, box_confidences, box_class_probs)
