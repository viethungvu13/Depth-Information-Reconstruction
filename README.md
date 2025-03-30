# Depth Information Reconstruction
## Introduction
This project aims to reconstruct depth information from a pair of stereo images by computing and visualizing the disparity map. Various image processing methods are applied, including:

- ✅ **Pixel-wise Matching**: Calculates disparity per pixel using L1 and L2 distance metrics.
- ✅ **Window-based Matching**: Uses a window to compare pixel vectors for smoother results.
- ✅ **Cosine Similarity & Correlation Coefficient**: Enhances quality by reducing noise with optimized parameters.

## 📂 Project Structure
📂 Depth-Information-Reconstruction  
 ├── 📁 data/                 # Contains input stereo images  
 ├── 📁 results/              # Stores output disparity maps  
 ├── 📜 main.py               # Main execution file  
 ├── 📜 disparity.py          # Disparity calculation functions  
 ├── 📜 display.py            # Visualization and plotting functions  
 ├── 📜 utils.py              # Utility functions  
 ├── 📜 requirements.txt      # Dependencies  
 └── 📜 README.md             # Project documentation  