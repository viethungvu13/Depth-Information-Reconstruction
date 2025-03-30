import cv2

def show_pixel_wise_matching(depth_l1, depth_l2):
    print('Compute disparity map using pixel-wise matching with ...', end=' ')
    s = input().strip().lower()
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
    print('Compute disparity map using window-based matching with ...', end=' ')
    s = input().strip().lower()
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
