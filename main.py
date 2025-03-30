import cv2
import numpy as np

path_to_img_left = 'data/Aloe_left_1.png'
path_to_img_right = 'data/Aloe_right_1.png'

def l1_distance(x, y):
    return abs(x - y)

def l2_distance(x, y):
    return (x - y)**2

def window_based_matching(img_l, img_r, height, width, disparity_range, kernel_size):
    depth1 = np.zeros((height, width)).astype(np.float32)
    depth2 = np.zeros((height, width)).astype(np.float32)
    kernel_half = (kernel_size - 1) // 2
    max_value = 255 * (kernel_size**2)

    for h in range(kernel_half, height - kernel_half):
        for w in range(kernel_half, width - kernel_half):
            cost_min_1 = max_value
            cost_min_2 = max_value
            doptimal1 = 0
            doptimal2 = 0
            for d in range(disparity_range + 1):
                cost1 = 0
                cost2 = 0
                for u in range(-kernel_half, kernel_half+1):
                    for v in range(-kernel_half, kernel_half+1):
                        if (w + v - d) < 0:
                            cost1 += 255
                            cost2 += 255**2
                        else:
                            cost1 += l1_distance(int(img_l[h + u][w + v]), int(img_r[h + u][w + v - d]))
                            cost2 += l2_distance(int(img_l[h + u][w + v]), int(img_r[h + u][w + v - d]))

                if cost1 < cost_min_1:
                    cost_min_1 = cost1
                    doptimal1 = d

                if cost2 < cost_min_2:
                    cost_min_2 = cost2
                    doptimal2 = d 

            depth1[h][w] = doptimal1 * 255 / disparity_range
            depth2[h][w] = doptimal2 * 255 / disparity_range

    return depth1.astype(np.uint8), depth2.astype(np.uint8) 

def pixel_wise_matching(img_l, img_r, height, width, disparity_range):
    depth_l1 = np.zeros((height, width)).astype(np.float32)
    depth_l2 = np.zeros((height, width)).astype(np.float32)
    max_value = 255
    for h in range(height):
        for w in range(width):
            doptimal1 = 0
            doptimal2 = 0
            cost_min_1 = max_value
            cost_min_2 = max_value
            for d in range(disparity_range + 1):
                cost1 = max_value if (w - d) < 0 else l1_distance(int(img_l[h][w]), int(img_r[h][w - d]))
                cost2 = max_value**2 if (w - d) < 0 else l2_distance(int(img_l[h][w]), int(img_r[h][w - d]))

                if cost1 < cost_min_1:
                    cost_min_1 = cost1
                    doptimal1 = d

                if cost2 < cost_min_2:
                    cost_min_2 = cost2
                    doptimal2 = d 

            depth_l1[h][w] = doptimal1 * 255 / disparity_range
            depth_l2[h][w] = doptimal2 * 255 / disparity_range
    return depth_l1.astype(np.uint8), depth_l2.astype(np.uint8)

def cal_disparity_map(path_to_img_left, path_to_img_right):

    img_l_origin = cv2.imread(path_to_img_left, 1)
    img_r_origin = cv2.imread(path_to_img_right, 1)

    img_l = cv2.imread(path_to_img_left, 0)
    img_r = cv2.imread(path_to_img_right, 0)

    img_l = img_l.astype(np.float32)
    img_r = img_r.astype(np.float32)

    height = len(img_l)
    width = len(img_l[0])

    disparity_range = 16

    depth_pixel_wise_matching_l1, depth_pixel_wise_matching_l2 = pixel_wise_matching(img_l, img_r, height, width, disparity_range)
    depth_window_based_matching_l1, depth_window_based_matching_l2 = window_based_matching(img_l, img_r, height, width, disparity_range, kernel_size=5)

    return img_l_origin, img_r_origin, depth_pixel_wise_matching_l1, depth_pixel_wise_matching_l2, depth_window_based_matching_l1, depth_window_based_matching_l2

def show_pixel_wise_matching(depth_l1, depth_l2):
    print('Compute disparity map using pixel-wise matching with ...', end= ' ')
    s = input()

    if s == 'l1':
        print('Saving result ...')
        cv2.imshow('Depth', depth_l1)
    elif s == 'l2':
        print('Saving result ...')
        cv2.imshow('Depth', depth_l2)
    elif s == 'l1 and l2':
        print('Saving result ...')
        cv2.imshow('Depth_l1', depth_l1)
        cv2.imshow('Depth_l2', depth_l2)

def show_window_based_matching(depth_l1, depth_l2):
    print('Compute disparity map using window_based matching with ...', end= ' ')
    s = input()

    if s == 'l1':
        print('Saving result ...')
        cv2.imshow('Depth', depth_l1)
    elif s == 'l2':
        print('Saving result ...')
        cv2.imshow('Depth', depth_l2)
    elif s == 'l1 and l2':
        print('Saving result ...')
        cv2.imshow('Depth_l1', depth_l1)
        cv2.imshow('Depth_l2', depth_l2)

def main():
    img_l, img_r, depth_pixel_wise_l1, depth_pixel_wise_l2, depth_window_based_l1, depth_window_based_l2  = cal_disparity_map(path_to_img_left, path_to_img_right)

    # Pixel-wise matching
    # Gray
    depth_pixel_wise_l1_normalized = cv2.normalize(depth_pixel_wise_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l1_normalized = np.uint8(depth_pixel_wise_l1_normalized)

    depth_pixel_wise_l2_normalized = cv2.normalize(depth_pixel_wise_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_pixel_wise_l2_normalized = np.uint8(depth_pixel_wise_l2_normalized)

    # Color
    depth_pixel_wise_l1_colored = cv2.applyColorMap(depth_pixel_wise_l1_normalized, cv2.COLORMAP_JET)
    depth_pixel_wise_l2_colored = cv2.applyColorMap(depth_pixel_wise_l2_normalized, cv2.COLORMAP_JET)

    # Window-based matching
    # Gray
    depth_window_based_l1_normalized = cv2.normalize(depth_window_based_l1, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l1_normalized = np.uint8(depth_window_based_l1_normalized)

    depth_window_based_l2_normalized = cv2.normalize(depth_window_based_l2, None, 0, 255, cv2.NORM_MINMAX)
    depth_window_based_l2_normalized = np.uint8(depth_window_based_l2_normalized)

    # Color
    depth_window_based_l1_colored = cv2.applyColorMap(depth_window_based_l1_normalized, cv2.COLORMAP_JET)
    depth_window_based_l2_colored = cv2.applyColorMap(depth_window_based_l2_normalized, cv2.COLORMAP_JET)

    print('Do you want to watch origin img?', end = ' ')
    ans = input()

    if ans == 'yes':
        cv2.imshow('img_l', img_l)
        cv2.imshow('img_r', img_r)
    else:
        print('Pixel-wise or window-based matching?')
        s = input()

        if s == 'pixel-wise matching':
            print('You choose gray or color img?', end = ' ')
            choose = input()
            
            if choose == 'gray':
                show_pixel_wise_matching(depth_pixel_wise_l1_normalized, depth_pixel_wise_l2_normalized)
            elif choose == 'color':
                show_pixel_wise_matching(depth_pixel_wise_l1_colored, depth_pixel_wise_l2_colored)
        elif s == 'window-based matching':
            print('You choose gray or color img?', end = ' ')
            choose = input()
            
            if choose == 'gray':
                show_window_based_matching(depth_window_based_l1_normalized, depth_window_based_l2_normalized)
            elif choose == 'color':
                show_window_based_matching(depth_window_based_l1_colored, depth_window_based_l2_colored)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print('Done!')

main()
