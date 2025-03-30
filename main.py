import cv2
import numpy as np
from disparity import cal_disparity_map_vectorized
from display import show_pixel_wise_matching, show_window_based_matching, show_window_cosine
from utils import get_valid_input

path_to_img_left = 'data/Aloe_left_1.png'
path_to_img_right = 'data/Aloe_right_1.png'

def main():
    (img_l, img_r, 
     depth_pixel_wise_l1, depth_pixel_wise_l2, 
     depth_window_based_l1, depth_window_based_l2, depth_window_cosine) = cal_disparity_map_vectorized(path_to_img_left, path_to_img_right)

    # Pixel-wise matching
    depth_pixel_wise_l1_normalized = cv2.normalize(depth_pixel_wise_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l1_normalized = np.clip(depth_pixel_wise_l1_normalized, 0, 255).astype(np.uint8)
    depth_pixel_wise_l2_normalized = cv2.normalize(depth_pixel_wise_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l2_normalized = np.clip(depth_pixel_wise_l2_normalized, 0, 255).astype(np.uint8)

    depth_pixel_wise_l1_colored = cv2.applyColorMap(depth_pixel_wise_l1_normalized, cv2.COLORMAP_JET)
    depth_pixel_wise_l2_colored = cv2.applyColorMap(depth_pixel_wise_l2_normalized, cv2.COLORMAP_JET)

    # Window-based matching 

    # l1 and l2
    # Grayscale
    depth_window_based_l1_normalized = cv2.normalize(depth_window_based_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l1_normalized = np.clip(depth_window_based_l1_normalized, 0, 255).astype(np.uint8)
    depth_window_based_l2_normalized = cv2.normalize(depth_window_based_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l2_normalized = np.clip(depth_window_based_l2_normalized, 0, 255).astype(np.uint8)

    # Color
    depth_window_based_l1_colored = cv2.applyColorMap(depth_window_based_l1_normalized, cv2.COLORMAP_JET)
    depth_window_based_l2_colored = cv2.applyColorMap(depth_window_based_l2_normalized, cv2.COLORMAP_JET)

    # Cosine Similarity
    # Grayscale
    depth_window_cosine_normalize = cv2.normalize(depth_window_cosine, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_cosine_normalize = np.clip(depth_window_cosine_normalize, 0, 255).astype(np.uint8)

    # Color
    depth_window_cosine_color = cv2.applyColorMap(depth_window_cosine_normalize, cv2.COLORMAP_JET)

    ans = get_valid_input('Do you want to watch origin img? (yes/no): ', ['yes', 'no'])


    if ans == 'yes':
        cv2.imshow('Origin Left', img_l)
        cv2.imshow('Origin Right', img_r)
    elif ans == 'no':
        print('Choose mode: (1) Pixel-wise Matching | (2) Window-based Matching')
        s = input('Enter 1 or 2: ').strip()
        if s == '1':
            print('Choose output: (1) Grayscale | (2) Color', end=' ')
            choose = input('Enter 1 or 2: ').strip()
            if choose == '1':
                show_pixel_wise_matching(depth_pixel_wise_l1_normalized, depth_pixel_wise_l2_normalized)
            elif choose == '2':
                show_pixel_wise_matching(depth_pixel_wise_l1_colored, depth_pixel_wise_l2_colored)
        elif s == '2':
            print('Choose method: (1) SAD/SSD | (2) Cosine Similarity')
            ans = input('Enter 1 or 2: ').strip()
            if ans == '1':
                print('Choose output: (1) Grayscale | (2) Color')
                choose = input('Enter 1 or 2: ').strip()
                if choose == '1':
                    show_window_based_matching(depth_window_based_l1_normalized, depth_window_based_l2_normalized)
                elif choose == '2':
                    show_window_based_matching(depth_window_based_l1_colored, depth_window_based_l2_colored)
            elif ans == '2':
                print('Choose output: (1) Grayscale | (2) Color')
                choose = input('Enter 1 or 2: ').strip()
                if choose == '1':
                    show_window_cosine(depth_window_cosine_normalize)
                else:
                    show_window_cosine(depth_window_cosine_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Done!')

if __name__ == '__main__':
    main()
