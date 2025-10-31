# INFOSYS-INTERNSHIP-OIL_SPILL_DETECTION-

# 🌊 **AquaVision – AI-Powered Oil Spill Detection System**

> *“Safeguarding our oceans through intelligent satellite-based oil spill monitoring.”*

[![Visit AquaVision App](https://img.shields.io/badge/🌐_Visit_App-Streamlit-blue?style=for-the-badge)](https://aquavision.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)](https://github.com/Sruthi1106/INFOSYS-_INTERNSHIP-OIL_SPILL_DETECTION-)

---

## 🧠 **About the Project**

**AquaVision** is an **AI-driven oil spill detection platform** developed as part of the Infosys Springboard Internship by **Bilakanti Sruthi**.
It leverages **deep learning (U-Net)** and **satellite imagery** to detect, segment, and visualize marine oil spills in real time.

Oil spills cause irreparable damage to marine ecosystems and coastal regions. AquaVision provides a **fast, reliable, and automated solution** to identify and visualize spills — helping researchers and authorities take immediate action.

Why This Matters
Oil spills pose severe threats to:

🐋 Marine Ecosystems - Devastating impact on aquatic life

🏖️ Coastal Regions - Contamination of beaches and shorelines

💰 Local Economies - Damage to fishing and tourism industries

🌍 Global Environment - Long-term ecological consequences 

Traditional detection methods are slow, labor-intensive, and often delayed. HydroVexel provides instant, accurate detection to enable immediate intervention.

---
## 🚨 Problem Statement

Oil spills pose a severe threat to marine ecosystems, coastal regions, and local economies.
Traditional detection methods — such as manual inspection of satellite images or physical patrolling — are:

⏰ Time-consuming: Hours to days for analysis

👷 Labor-intensive: Requires expert human inspection

🐌 Often delayed: Causes loss of critical response time

💡 Solution:
Develop an AI-powered oil spill detection system using deep learning and satellite imagery to automatically identify and localize oil spills with high accuracy, enabling early intervention and faster emergency response.

## ✨ Key Features
🎯 Core Capabilities

⚡ Real-time Oil Spill Detection — Upload satellite or aerial images and get instant results

🎯 High Accuracy Segmentation — Achieves 94.57% accuracy with U-Net + Attention architecture

🔥 Confidence Mapping — Generates visual heatmaps showing detection confidence levels

🖼 Multi-format Support — Works with .JPG, .JPEG, .PNG satellite imagery

☁️ Cloud Integration — Optional saving to Supabase or local database for storage

🕒 Historical Analysis — View and track past detections with date-based filtering

## 🖥️ User Interface

🧭 Interactive Web Application — Built using Streamlit

🌊 Beautiful Ocean Theme — Inspired by marine environments with a glassmorphism UI

🔍 Real-time Visualization — Displays overlays, binary masks, and confidence heatmaps

📤 Export Options — Download predictions as PNG, metrics as CSV or JSON

📱 Responsive Design — Works seamlessly across desktop and mobile

## 📊 Analytics & Reporting

📈 Detection Metrics — Shows coverage %, confidence, pixel statistics

🖼 Image Gallery — View all processed images with filters and sorting

🗃 Database Dashboard — Summarizes detection trends and overall accuracy

📂 Export Options — Full data export for external analysis and documentation


## 🧩 **Project Workflow**

### 🔹 **Module 1: Data Collection**

* Acquired satellite image dataset from **Zenodo Oil Spill Detection Dataset**
  [Dataset Source](https://zenodo.org/records/10555314)
* Organized data into `train`, `validation`, and `test` sets.
* Verified directory integrity and configured GPU acceleration in Colab.

---

### 🔹 **Module 2: Data Exploration & Preprocessing**

* Visualized random image–mask pairs.
* Standardized all images to **256×256** resolution.
* Normalized and enhanced images with **SAR-specific preprocessing** (e.g., speckle noise reduction).
* Applied **Albumentations** for augmentation: flips, rotations, brightness, and contrast shifts.
<img width="711" height="361" alt="Screenshot 2025-10-31 132346" src="https://github.com/user-attachments/assets/d341810c-4888-44ba-b323-d809be58b1ec" />

---

### 🔹 **Module 3: Model Development**

* Implemented **U-Net** with attention and residual connections.
* Model Input: `256×256×3` | Output: Binary mask `256×256×1`
* Loss Functions: **Binary Cross-Entropy (BCE)** + **Dice Loss**
* Metrics: **Accuracy, IoU, Dice, Precision, Recall**
* Parameters: ~33 million | Layers: 122

---

### 🔹 **Module 4: Training & Evaluation**

* Training configured with:

  * Epochs: 30 | Batch Size: 8 | Learning Rate: 0.0001
  * Optimizer: **AdamW** | Early Stopping Enabled
* Achieved:

  * ✅ **Accuracy:** ~95%
  * ✅ **Dice Coefficient:** 0.89
  * ✅ **IoU:** 0.83–0.90
  * ✅ **Precision/Recall:** ~96%
* Real-time validation and monitored metric graphs for loss, accuracy, IoU, and Dice.

<img width="513" height="808" alt="Screenshot 2025-10-31 132222" src="https://github.com/user-attachments/assets/ee3c8931-e292-41c4-9364-6734cf1ce8e8" />
<img width="515" height="806" alt="Screenshot 2025-10-31 132210" src="https://github.com/user-attachments/assets/c067ca4b-6e7e-4f35-b858-60235e8872dc" />

---

### 🔹 **Module 5: Visualization of Results**

* Displayed **side-by-side comparisons** of input, ground truth, and predicted masks.
* Generated **overlay maps** (red = detected spill).
* Created **confidence heatmaps** and confusion matrices.
<img width="730" height="820" alt="Screenshot 2025-10-31 132239" src="https://github.com/user-attachments/assets/8bb577f6-2250-41f7-becf-75804cfe32f8" />

<img width="1281" height="433" alt="Screenshot 2025-10-31 132317" src="https://github.com/user-attachments/assets/eb59378e-3193-4f38-bb8c-0c228038e429" />

---

### 🔹 **Module 6: Deployment via Streamlit App**

> **App Name:** *AquaVision*
> **Developed by:** *Bilakanti Sruthi*

* Built an **interactive web interface** using **Streamlit** and **TensorFlow**.
* Integrated `.h5` model (stored on Google Drive for faster access).
* Added:

  * 📸 Image Upload for real-time detection
  * 🌡 Confidence Heatmap
  * 📊 Metrics Dashboard (Accuracy, IoU, Dice, Precision, Recall)
  * 📈 Summary Dashboard
  * 🤖 Smart Chatbot for user guidance
* Designed a custom **UI with gradient backgrounds** and smooth transitions.

---

## ⚙️ **Tech Stack**

| Category                 | Tools / Libraries                    |
| ------------------------ | ------------------------------------ |
| **Programming Language** | Python                               |
| **Deep Learning**        | TensorFlow, Keras                    |
| **Data Processing**      | NumPy, Pandas, OpenCV                |
| **Visualization**        | Matplotlib, Seaborn                  |
| **Web Framework**        | Streamlit                            |
| **Augmentation**         | Albumentations                       |
| **Deployment**           | Streamlit Cloud / Local Server       |
| **Dataset Source**       | Zenodo (Oil Spill Detection Dataset) |

---

## 🧭 **Project Structure**

```
INFOSYS-_INTERNSHIP-OIL_SPILL_DETECTION-/
│
├── app.py                  # Streamlit main app file
├── unet_oilspill_final.h5  # Trained model (stored on GDrive)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── /notebooks              # Jupyter/Colab notebooks for training
```

---

## 🌟 **App Features**

✅ Upload satellite images (.jpg/.png)
✅ Predict and visualize oil spill regions
✅ View **overlay**, **predicted mask**, and **heatmap**
✅ Compare with ground truth masks
✅ View **metrics dashboard** (Accuracy, IoU, Dice, Precision, Recall)
✅ Track **prediction history** and download results
✅ Built-in **AI chatbot** for metric explanations

---

## 🎨 **Design Highlights**

* Dynamic gradient background (`#0f2027 → #2c5364`)
* Interactive sidebar controls
* Smooth hover animations for metric cards
* Responsive layout for all screen sizes
* Ocean-inspired blue & cyan theme 🌊

---

## 📈 **Model Performance Summary**

| Metric               | Score |
| :------------------- | :---: |
| **Accuracy**         |  95%  |
| **IoU**              |  0.87 |
| **Dice Coefficient** |  0.89 |
| **Precision**        |  0.96 |
| **Recall**           |  0.94 |

---

## 🧪 **How to Run Locally**

```bash
# Clone the repository
git clone https://github.com/Sruthi1106/INFOSYS-_INTERNSHIP-OIL_SPILL_DETECTION-.git
cd INFOSYS-_INTERNSHIP-OIL_SPILL_DETECTION-

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## **Web Interface**
## What is AquaVision
## Home Page

<img width="1906" height="960" alt="Screenshot 2025-10-31 120842" src="https://github.com/user-attachments/assets/a868ba4c-e649-4684-8745-f3d596cb04ed" />

## Upload images for evaluation

<img width="1901" height="964" alt="Screenshot 2025-10-31 121756" src="https://github.com/user-attachments/assets/a9271e2b-b361-4d07-909f-01a9e1bc5f5d" />

## Outputs

<img width="1885" height="837" alt="Screenshot 2025-10-31 121825" src="https://github.com/user-attachments/assets/27c2163b-4c15-479c-970e-768e575f8b19" />

## Metrics Dashboard

<img width="1439" height="491" alt="Screenshot 2025-10-31 121846" src="https://github.com/user-attachments/assets/47243994-9c3c-4b02-a877-82f435b2cfd4" />


## Detection History and Smart Assisstant for knowing about app

<img width="1406" height="714" alt="Screenshot 2025-10-31 121901" src="https://github.com/user-attachments/assets/e712c7b5-e0a9-41fc-9e33-567e8e9d8362" />

---

## 💬 **About the Developer**

**👩‍💻 Bilakanti Sruthi**
AI & ML Enthusiast | B.Tech Student at Anurag University

📧 **Email:** [bilakantisruthi@gmail.com](mailto:bilakantisruthi@gmail.com)
🔗 **LinkedIn:** [linkedin.com/in/bilakanti-sruthi-guptha1106](https://www.linkedin.com/in/bilakanti-sruthi-guptha1106/)
💻 **GitHub:** [github.com/Sruthi1106](https://github.com/Sruthi1106)

---

##  **Acknowledgment**

> Developed as part of the **Infosys Springboard Internship** under mentorship and guidance from **Ekshitha Namala**.
> Special thanks to the **Ekshitha Namala**.

---

## ⚖️ **License**

© 2025 **AquaVision** – Developed by *Bilakanti Sruthi*
Licensed under the **MIT License**.
For educational and environmental research purposes only.

>>>>>>> 13678512d8af25f9b61436364c5ce84ecf1817f7
