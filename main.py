import cv2
import numpy as np
from disparity import cal_disparity_map_vectorized
from display import show_pixel_wise_matching, show_window_based_matching
from utils import get_valid_input

# Đường dẫn đến ảnh (đảm bảo rằng thư mục data chứa các file ảnh tương ứng)
path_to_img_left = 'data/Aloe_left_1.png'
path_to_img_right = 'data/Aloe_right_2.png'

def main():
    (img_l, img_r, 
     depth_pixel_wise_l1, depth_pixel_wise_l2, 
     depth_window_based_l1, depth_window_based_l2) = cal_disparity_map_vectorized(path_to_img_left, path_to_img_right)

    # Pixel-wise matching
    depth_pixel_wise_l1_normalized = cv2.normalize(depth_pixel_wise_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l1_normalized = np.uint8(depth_pixel_wise_l1_normalized)
    depth_pixel_wise_l2_normalized = cv2.normalize(depth_pixel_wise_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l2_normalized = np.uint8(depth_pixel_wise_l2_normalized)

    depth_pixel_wise_l1_colored = cv2.applyColorMap(depth_pixel_wise_l1_normalized, cv2.COLORMAP_JET)
    depth_pixel_wise_l2_colored = cv2.applyColorMap(depth_pixel_wise_l2_normalized, cv2.COLORMAP_JET)

    # Window-based matching
    depth_window_based_l1_normalized = cv2.normalize(depth_window_based_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l1_normalized = np.uint8(depth_window_based_l1_normalized)
    depth_window_based_l2_normalized = cv2.normalize(depth_window_based_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l2_normalized = np.uint8(depth_window_based_l2_normalized)

    depth_window_based_l1_colored = cv2.applyColorMap(depth_window_based_l1_normalized, cv2.COLORMAP_JET)
    depth_window_based_l2_colored = cv2.applyColorMap(depth_window_based_l2_normalized, cv2.COLORMAP_JET)

    ans = get_valid_input('Do you want to watch origin img? (yes/no): ', ['yes', 'no'])


    if ans == 'yes':
        cv2.imshow('Origin Left', img_l)
        cv2.imshow('Origin Right', img_r)
    else:
        print('Pixel-wise or window-based matching?')
        s = input().strip().lower()
        if s == 'pixel-wise matching':
            print('You choose gray or color img?', end=' ')
            choose = input().strip().lower()
            if choose == 'gray':
                show_pixel_wise_matching(depth_pixel_wise_l1_normalized, depth_pixel_wise_l2_normalized)
            elif choose == 'color':
                show_pixel_wise_matching(depth_pixel_wise_l1_colored, depth_pixel_wise_l2_colored)
        elif s == 'window-based matching':
            print('You choose gray or color img?', end=' ')
            choose = input().strip().lower()
            if choose == 'gray':
                show_window_based_matching(depth_window_based_l1_normalized, depth_window_based_l2_normalized)
            elif choose == 'color':
                show_window_based_matching(depth_window_based_l1_colored, depth_window_based_l2_colored)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Done!')

if __name__ == '__main__':
    main()
