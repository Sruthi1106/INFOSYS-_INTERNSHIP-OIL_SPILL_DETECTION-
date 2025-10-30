# Oil Spill Detection Web App

This repository contains a Streamlit web application for oil-spill detection from satellite imagery using a U-Net segmentation model.

## Features
- Upload satellite images and (optionally) ground-truth masks.
- Predict oil spill regions with a pre-trained U-Net model.
- Visual outputs: predicted mask, overlay (red = detected spill), and confidence heatmap.
- Compute evaluation metrics (Accuracy, IoU, Dice, Precision, Recall) when ground-truth is provided.
- Download a ZIP package containing overlay image, predicted mask, confidence heatmap and metrics JSON.
- Clean, responsive UI and sidebar controls.

**Developed by: Bilakanti Sruthi**

## Usage (local)
1. Install dependencies:
```bash
pip install -r requirements.txt
