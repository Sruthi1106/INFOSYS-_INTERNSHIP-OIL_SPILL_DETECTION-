# ============================================================
# 🌊 Oil Spill Detection AI Web App
# Developed by Bilakanti Sruthi
# ============================================================

import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image
from sklearn.metrics import precision_score, recall_score, accuracy_score
import datetime
import pandas as pd
import base64
import io

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="🌊 Aqua Vision",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# CUSTOM CSS STYLING
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    text-align: center;
    color: #00FFFF;
    text-shadow: 1px 1px 10px #00FFFF;
}
.metric-card {
    background: rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
    transition: 0.3s;
}
.metric-card:hover {
    transform: scale(1.05);
    background: rgba(255,255,255,0.25);
}
.footer {
    text-align: center;
    color: #B0E0E6;
    margin-top: 40px;
}
.chatbox {
    background-color: rgba(255,255,255,0.15);
    border-radius: 10px;
    padding: 15px;
    max-height: 300px;
    overflow-y: auto;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# HEADER SECTION
# ------------------------------------------------------------
st.markdown("<h1>🌊 AquaVision</h1>", unsafe_allow_html=True)
st.markdown("<h2> AI-Powered Oil Spill Detection System</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#A9A9A9'>AquaVision is an AI-driven platform that detects, classifies, and visualizes oil spill regions from satellite imagery using advanced deep learning models like U-Net. It aims to support early detection, precise segmentation, and effective environmental decision-making to protect marine ecosystems.</p>", unsafe_allow_html=True)
st.sidebar.title("🧭 Controls & Info")
st.sidebar.markdown("*Developed by Bilakanti Sruthi*")
st.sidebar.markdown("[🔗 Connect on LinkedIn](https://www.linkedin.com/in/bilakanti-sruthi-guptha1106/)", unsafe_allow_html=True)

# Theme toggle
theme = st.sidebar.radio("Theme Mode", ["🌙 Dark", "☀ Light"])
if theme == "☀ Light":
    st.markdown("<style>.stApp{background: linear-gradient(135deg, #f8f9fa, #e3f2fd); color: black;}</style>", unsafe_allow_html=True)

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------
@st.cache_resource
def load_unet_model(path="unet_oilspill_final.h5"):
    return load_model(path, compile=False)

try:
    model = load_unet_model("unet_oilspill_final.h5")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def dice_coef(y_true, y_pred, smooth=1e-6):
    y_true_f, y_pred_f = y_true.flatten(), y_pred.flatten()
    inter = np.sum(y_true_f * y_pred_f)
    return (2. * inter + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth)

def iou_score(y_true, y_pred, smooth=1e-6):
    y_true_f, y_pred_f = y_true.flatten(), y_pred.flatten()
    inter = np.sum(y_true_f * y_pred_f)
    union = np.sum(y_true_f) + np.sum(y_pred_f) - inter
    return (inter + smooth) / (union + smooth)

def pixel_accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

# ------------------------------------------------------------
# SIDEBAR INPUTS
# ------------------------------------------------------------
uploaded_image = st.sidebar.file_uploader("Upload Satellite Image (.jpg/.png)", type=["jpg", "jpeg", "png"])
uploaded_mask = st.sidebar.file_uploader("Upload Ground Truth Mask (optional)", type=["jpg", "jpeg", "png"])
threshold = st.sidebar.slider("Prediction Threshold", 0.1, 0.9, 0.5, 0.01)

if "history" not in st.session_state:
    st.session_state["history"] = []

# ------------------------------------------------------------
# MAIN APP FUNCTIONALITY
# ------------------------------------------------------------
if uploaded_image:
    img = Image.open(uploaded_image).convert("RGB")
    img_np = np.array(img)
    resized = cv2.resize(img_np, (256, 256))
    inp = np.expand_dims(resized.astype("float32") / 255.0, 0)
    pred = model.predict(inp, verbose=0)[0, ..., 0]
    pred_bin = (pred > threshold).astype("uint8")

    # Confidence heatmap
    heatmap = cv2.applyColorMap((pred * 255).astype("uint8"), cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    # Red overlay for prediction
    overlay = resized.copy()
    red_mask = np.zeros_like(overlay)
    red_mask[..., 0] = pred_bin * 255
    overlay = cv2.addWeighted(red_mask, 0.5, overlay, 0.7, 0)

    metrics = {"Mean Confidence": np.mean(pred)}
    if uploaded_mask:
        gt = np.array(Image.open(uploaded_mask).convert("L"))
        gt = cv2.resize(gt, (256, 256))
        gt_bin = (gt > 127).astype("uint8")
        metrics.update({
            "Accuracy": pixel_accuracy(gt_bin, pred_bin),
            "IoU": iou_score(gt_bin, pred_bin),
            "Dice": dice_coef(gt_bin, pred_bin),
            "Precision": precision_score(gt_bin.flatten(), pred_bin.flatten(), zero_division=0),
            "Recall": recall_score(gt_bin.flatten(), pred_bin.flatten(), zero_division=0)
        })

    # Add to history
    entry = {"Image": uploaded_image.name, "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    entry.update(metrics)
    st.session_state.history.append(entry)

    # Display
    st.subheader("🛰 Results")
    c1, c2, c3 = st.columns(3)
    c1.image(resized, caption="Original Image", use_container_width=True)
    if uploaded_mask:
        c2.image(gt, caption="Ground Truth Mask", use_container_width=True)
    else:
        c2.info("Upload a mask to compare performance.")
    c3.image(pred_bin * 255, caption="Predicted Mask", use_container_width=True)

    c4, c5 = st.columns(2)
    c4.image(overlay, caption="Overlay (Red = Spill)", use_container_width=True)
    c5.image(heatmap, caption="Confidence Heatmap", use_container_width=True)

    # ------------------------------------------------------------
# 📊 METRICS DASHBOARD (SAFE + CLEAN LAYOUT)
# ------------------------------------------------------------
if "metrics" in locals() and metrics:  # Only show if metrics exist
    st.subheader("📊 Metrics Dashboard")

    # Convert metrics dictionary to list
    metric_items = list(metrics.items())

    # Display metrics in rows of 3 columns
    for i in range(0, len(metric_items), 3):
        cols = st.columns(3, gap="large")
        for j, (k, v) in enumerate(metric_items[i:i+3]):
            color = "#7CFC00" if v > 0.8 else "#FFA500" if v > 0.5 else "#FF6347"
            val = f"{v*100:.2f}%" if k != "Mean Confidence" else f"{v:.3f}"
            card_html = f"""
            <div class='metric-card' style='min-height:120px;margin-bottom:15px;'>
                <h4 style='color:{color}'>{k}</h4>
                <p style='font-size:22px;margin-top:10px;'>{val}</p>
            </div>
            """
            cols[j].markdown(card_html, unsafe_allow_html=True)

# ----------------------- SUMMARY DASHBOARD -----------------------
#



# HISTORY TABLE
# ------------------------------------------------------------
st.markdown("<h3>📜 Detection History</h3>", unsafe_allow_html=True)
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)
    col1, col2 = st.columns(2)
    with col1:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download History", data=csv, file_name="history.csv", mime="text/csv")
    with col2:
        if st.button("🗑 Clear History"):
            st.session_state.history.clear()
            st.success("History cleared.")
else:
    st.info("No detection history yet.")



# ------------------------------------------------------------
# SMART CHATBOT
# ------------------------------------------------------------
st.markdown("<h3>🤖 Smart Assistant</h3>", unsafe_allow_html=True)
user_input = st.text_input("Ask about Oil Spill Detection (e.g., What is IoU?)")
responses = {
        "hello": "Hi there! 👋 I’m your Oil Spill Assistant. I can help you understand this app!",
        "what is this app": "This app detects oil spills in satellite images using a U-Net deep learning model.",
        "how to use": "Just upload a satellite image (and optionally a ground truth mask) to see detection results, metrics, and overlays.",
        "accuracy": "Accuracy shows how many pixels were correctly predicted as spill or non-spill.",
        "iou": "IoU (Intersection over Union) measures how much the predicted region overlaps with the ground truth region.",
        "dice": "Dice Coefficient is another overlap metric — higher means better segmentation performance.",
        "heatmap": "The confidence heatmap shows where the model is most certain about detecting oil spills.",
        "who developed this": "This web app was proudly developed by *Bilakanti Sruthi* 💫 as part of an AI-based oil spill detection project.",
        "thank you": "You’re most welcome! 🌸 Happy to help.",
    }

if user_input:
    answer = None
    for key in responses:
        if key in user_input.lower():
            answer = responses[key]
            break
    if not answer:
        answer = "I’m your Oil Spill AI Assistant 🌊 — I can help explain IoU, Dice, Accuracy, or Confidence metrics."
    st.markdown(f"<div class='chatbox'>{answer}</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("<div class='footer'>© 2025 Developed by <b>Bilakanti Sruthi</b> | AquaVision | Oil Spill Detection AI Project</div>", unsafe_allow_html=True)
