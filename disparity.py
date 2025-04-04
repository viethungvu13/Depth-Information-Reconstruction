import cv2
import numpy as np
from pixel_matching import pixel_wise_matching_vectorized
from window_matching import window_based_matching_vectorized
from window_matching_cosine import window_matching_cosine

def cal_disparity_map_vectorized(path_to_img_left, path_to_img_right):

    img_l_origin = cv2.imread(path_to_img_left, 1)
    img_r_origin = cv2.imread(path_to_img_right, 1)

    img_l = cv2.imread(path_to_img_left, 0).astype(np.float32)
    img_r = cv2.imread(path_to_img_right, 0).astype(np.float32)

    disparity_range = 16

    depth_pixel_wise_l1, depth_pixel_wise_l2 = pixel_wise_matching_vectorized(img_l, img_r, disparity_range)
    depth_window_based_l1, depth_window_based_l2 = window_based_matching_vectorized(img_l, img_r, disparity_range, kernel_size=5)
    depth_window_cosine = window_matching_cosine(img_l, img_r, disparity_range, kernel_size=5)

    return (img_l_origin, img_r_origin,
            depth_pixel_wise_l1, depth_pixel_wise_l2, 
            depth_window_based_l1, depth_window_based_l2,
            depth_window_cosine)
