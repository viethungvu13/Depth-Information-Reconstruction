import numpy as np
import cv2

def window_based_matching_vectorized(img_l, img_r, disparity_range, kernel_size):
    
    height, width = img_l.shape
    max_value = 255.0
    kernel = (kernel_size, kernel_size)

    costs_l1 = np.empty((disparity_range + 1, height, width), dtype=np.float32)
    costs_l2 = np.empty((disparity_range + 1, height, width), dtype=np.float32)

    for d in range(disparity_range + 1):
        if d == 0:
            diff = np.abs(img_l - img_r)
            diff2 = (img_l - img_r) ** 2
        else:
            diff = np.empty_like(img_l)
            diff[:, :d] = max_value
            diff[:, d:] = np.abs(img_l[:, d:] - img_r[:, :-d])
            
            diff2 = np.empty_like(img_l)
            diff2[:, :d] = max_value ** 2
            diff2[:, d:] = (img_l[:, d:] - img_r[:, :-d]) ** 2

        cost_l1 = cv2.boxFilter(diff, ddepth=-1, ksize=kernel, normalize=False)
        cost_l2 = cv2.boxFilter(diff2, ddepth=-1, ksize=kernel, normalize=False)

        costs_l1[d] = cost_l1
        costs_l2[d] = cost_l2

    doptimal_l1 = np.argmin(costs_l1, axis=0)
    doptimal_l2 = np.argmin(costs_l2, axis=0)

    disparity_map_l1 = (doptimal_l1.astype(np.float32) * 255 / disparity_range).astype(np.uint8)
    disparity_map_l2 = (doptimal_l2.astype(np.float32) * 255 / disparity_range).astype(np.uint8)

    return disparity_map_l1, disparity_map_l2