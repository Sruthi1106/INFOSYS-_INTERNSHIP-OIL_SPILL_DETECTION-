# Oil Spill Detection using Deep Learning

##  Project Overview

This project aims to develop a **deep learning-based system** for detecting oil spills in satellite images.
By leveraging **U-Net segmentation architecture**, the system identifies spill regions with high accuracy, supporting environmental monitoring and disaster response.

The work has been structured into milestones for clarity and systematic progress.



## 📌 Milestone 1: Data Collection & Preprocessing

### Objectives

* Acquire and prepare satellite imagery datasets.
* Organize data into training, validation, and testing sets.
* Perform preprocessing and augmentation to improve model generalization.

### Work Completed

1. **Dataset Acquisition**

   * Dataset: *Oil Spill Detection Dataset* (Kaggle / open-source).
   * Includes satellite images and labeled segmentation masks.

2. **Data Organization**

   * Images and masks arranged into structured folders (`train`, `val`, `test`).

3. **Preprocessing**

   * Resized images to **256 × 256 pixels**.
   * Normalized pixel values to `[0,1]`.
   * Applied basic speckle-noise reduction techniques.

4. **Augmentation**

   * Horizontal & vertical flips
   * Random rotations
   * Brightness/contrast adjustments
   * Gaussian blur

5. **Visualization**

   * Displayed side-by-side comparisons of raw images and masks to validate preprocessing.

---

## 📌 Milestone 2: Model Development, Training & Evaluation

### Objectives

* Build a segmentation model (U-Net).
* Implement loss functions for segmentation tasks.
* Train and evaluate the model on the prepared dataset.

### Work Completed

1. **Model Development (U-Net)**

   * Custom U-Net built using **TensorFlow/Keras**.
   * Encoder–Decoder structure with skip connections.
   * Handles both grayscale (SAR) and RGB satellite data.

2. **Loss Functions & Metrics**

   * Binary Cross-Entropy (BCE) + Dice Loss
   * Accuracy, IoU (Intersection over Union), Dice Coefficient, Precision, Recall

3. **Training Strategy**

   * Optimizer: **Adam (lr = 1e-4)**
   * Real-time augmentation applied during training
   * Callbacks used: ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

4. **Evaluation**

   * Training curves (accuracy & loss) plotted.
   * Achieved **>95% accuracy** on validation data.
   * Computed confusion matrix for pixel-level classification.
   * Fine-tuned hyperparameters for improved results.


##  Results 

* The trained U-Net successfully segments oil spill regions.
* Model shows strong performance across Accuracy, IoU, Dice, Precision, and Recall.
* Predictions were visualized against ground truth masks for validation.
  

##  Repository Structure


├── data/                      # Dataset (train/val/test)
├── notebooks/
│   ├── milestone1.ipynb        # Data preprocessing
│   ├── milestone2.ipynb        # Model training & evaluation
├── models/
│   ├── unet_oilspill_best.keras   # Saved trained model
│   ├── unet_oilspill_final.h5     # Legacy H5 format
├── results/
│   ├── predictions/            # Predicted segmentation outputs
│   ├── plots/                  # Training curves, confusion matrix
└── README.md                   # Project documentation


##  Tech Stack

* Python 3.12
* TensorFlow / Keras
* OpenCV
* Albumentations
* scikit-learn
* Matplotlib / Seaborn


