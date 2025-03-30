import cv2

def show_pixel_wise_matching(depth_l1, depth_l2):
    print("\n--- Pixel-wise Matching ---")
    print("1. Show L1")
    print("2. Show L2")
    print("3. Show both L1 & L2")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == '1':
        print("Displaying L1...")
        cv2.imshow('Depth L1', depth_l1)
    elif choice == '2':
        print("Displaying L2...")
        cv2.imshow('Depth L2', depth_l2)
    elif choice == '3':
        print("Displaying both L1 & L2...")
        cv2.imshow('Depth L1', depth_l1)
        cv2.imshow('Depth L2', depth_l2)
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

def show_window_based_matching(depth_l1, depth_l2):
    print("\n--- Window-based Matching ---")
    print("1. Show L1")
    print("2. Show L2")
    print("3. Show both L1 & L2")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == '1':
        print("Displaying L1...")
        cv2.imshow('Depth L1', depth_l1)
    elif choice == '2':
        print("Displaying L2...")
        cv2.imshow('Depth L2', depth_l2)
    elif choice == '3':
        print("Displaying both L1 & L2...")
        cv2.imshow('Depth L1', depth_l1)
        cv2.imshow('Depth L2', depth_l2)
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

def show_window_cosine(depth):
    print("\nDisplaying Depth Map using Cosine Similarity...")
    cv2.imshow('Depth', depth)
