# Depth Information Reconstruction
## Introduction
This project aims to reconstruct depth information from a pair of stereo images by computing and visualizing the disparity map. Various image processing methods are applied, including:

- ✅ **Pixel-wise Matching**: Calculates disparity per pixel using L1 and L2 distance metrics.
- ✅ **Window-based Matching**: Uses a window to compare pixel vectors for smoother results.
- ✅ **Cosine Similarity & Correlation Coefficient**: Enhances quality by reducing noise with optimized parameters.

## 📂 Project Structure
📂 **Depth-Information-Reconstruction**  
 ├── 📁 **data/**                 # Contains input stereo images  
 ├── 📁 **results/**              # Stores output disparity maps  
 ├── 📜 **main.py**               # Main execution file  
 ├── 📜 **disparity.py**          # Disparity calculation functions  
 ├── 📜 **display.py**            # Visualization and plotting functions  
 ├── 📜 **utils.py**              # Utility functions  
 ├── 📜 **metrics.py**            # Evaluation metrics for disparity maps  
 ├── 📜 **pixel_matching.py**     # Implements pixel-wise disparity matching  
 ├── 📜 **window_matching.py**    # Implements window-based disparity matching  
 ├── 📜 **requirements.txt**      # Dependencies  
 └── 📜 **README.md**             # Project documentation 

 ## 🚀 Installation & Usage

 ### 1️⃣ Prerequisites

Ensure you have:

- **Python 3.x**
- **Required Libraries:** NumPy, OpenCV, Matplotlib

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Running the Project

#### Pixel-wise Matching
```bash
from disparity import pixel_wise_matching
result = pixel_wise_matching('data/left.png', 'data/right.png', disparity_range=16)
```
#### Window-based Matching
```bash
from disparity import window_based_matching
result = window_based_matching('data/left.png', 'data/right.png', disparity_range=16, kernel_size=5)
```

## 📊 Results & Visualization
Disparity maps can be visualized in grayscale and color maps:
|--------------------| Grayscale Disparity | | Color Map Disparity |
|Pixel-wise matching|
|Window-based matching|

