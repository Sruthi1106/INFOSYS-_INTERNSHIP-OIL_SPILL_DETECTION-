# INFOSYS-INTERNSHIP-OIL_SPILL_DETECTION-
Perfect 🌊
Here’s a **complete, professional, and standout `README.md`** for your GitHub project **AquaVision**, modeled after your reference file but fully rewritten for your app and your work.
You can **copy-paste this directly** into your GitHub repository.

---

# 🌊 **AquaVision – AI-Powered Oil Spill Detection System**

> *“Safeguarding our oceans through intelligent satellite-based oil spill monitoring.”*

[![Visit AquaVision App](https://img.shields.io/badge/🌐_Visit_App-Streamlit-blue?style=for-the-badge)](https://aquavision.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)](https://github.com/Sruthi1106/INFOSYS-_INTERNSHIP-OIL_SPILL_DETECTION-)

---

## 🧠 **About the Project**

**AquaVision** is an **AI-driven oil spill detection platform** developed as part of the Infosys Springboard Internship by **Bilakanti Sruthi**.
It leverages **deep learning (U-Net)** and **satellite imagery** to detect, segment, and visualize marine oil spills in real time.

Oil spills cause irreparable damage to marine ecosystems and coastal regions. AquaVision provides a **fast, reliable, and automated solution** to identify and visualize spills — helping researchers and authorities take immediate action.

---

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

---

### 🔹 **Module 5: Visualization of Results**

* Displayed **side-by-side comparisons** of input, ground truth, and predicted masks.
* Generated **overlay maps** (red = detected spill).
* Created **confidence heatmaps** and confusion matrices.
* Visualized **best vs worst segmentations** for quality analysis.

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

---

## 💬 **About the Developer**

**👩‍💻 Bilakanti Sruthi**
AI & ML Enthusiast | B.Tech Student at Anurag University

📧 **Email:** [bilakantisruthi@gmail.com](mailto:bilakantisruthi@gmail.com)
🔗 **LinkedIn:** [linkedin.com/in/bilakanti-sruthi-guptha1106](https://www.linkedin.com/in/bilakanti-sruthi-guptha1106/)
💻 **GitHub:** [github.com/Sruthi1106](https://github.com/Sruthi1106)

---

##  **Acknowledgment**

> Developed as part of the **Infosys Springboard Internship ** under mentorship and guidance from **Ekshitha Namala**.
> Special thanks to the **Ekshitha Namala **.

---

## ⚖️ **License**

© 2025 **AquaVision** – Developed by *Bilakanti Sruthi*
Licensed under the **MIT License**.
For educational and environmental research purposes only.

