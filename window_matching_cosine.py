import numpy as np
from metrics import cosine_similarity

def window_matching_cosine(img_l, img_r, disparity_range, kernel_size):
    height, width = img_l.shape
    kernel_half = (kernel_size - 1) // 2
    scale = 255 / disparity_range

    depth = np.zeros((height, width), np.float32)

    for y in range(kernel_half, height - kernel_half):
        for x in range(kernel_half, width - kernel_half):
            disparity = 0
            cost_optimal = -1

            for j in range(disparity_range):
                d = x - j
                cost = -1
                if (d - kernel_half) > 0:
                    wp = img_l[(y-kernel_half):(y+kernel_half)+1, (x-kernel_half):(x+kernel_half)+1]
                    wqd = img_r[(y-kernel_half):(y+kernel_half)+1, (d-kernel_half):(d+kernel_half)+1]

                    wp_flattened = wp.flatten()
                    wqd_flattened = wqd.flatten()
                    
                    cost = cosine_similarity(wp_flattened, wqd_flattened)
                
                if cost > cost_optimal:
                    cost_optimal = cost
                    disparity = j
                
                depth[y, x] = disparity * scale
    return depth