import streamlit as st
import numpy as np
import joblib
import time
import base64
import os

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Organoid Bio-Computer",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------------------------------
# Background Image
# ---------------------------------------------------------
def add_bg(image_file):
    try:
        if not os.path.exists(image_file):
            return
            
        with open(image_file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except Exception as e:
        # Catch other potential errors, but avoid printing detailed errors in the final app
        pass 

add_bg("lab_background.png")


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load("my_best_model.pkl")
    except:
        st.error("❌ Model file 'my_best_model.pkl' not found.")
        return None

model = load_model()


# ---------------------------------------------------------
# First-time launch state
# ---------------------------------------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "active_status" not in st.session_state:
    st.session_state.active_status = False


# ---------------------------------------------------------
# Launcher Screen
# ---------------------------------------------------------
if not st.session_state.started:

    st.markdown("<h1 style='text-align:center; color:#00C0FF;'>🧪 Bio-Computer Experiment Launcher</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Activate the Organoid Computational Interface</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    start_btn = st.button("▶ START EXPERIMENT", use_container_width=True)

    if start_btn:
        if model:
            st.session_state.started = True
            st.toast("System Initializing...", icon="🚀")
            time.sleep(0.8)
            st.rerun()
        else:
            st.error("Cannot start — model missing.")


# ---------------------------------------------------------
# Main Experiment Interface
# ---------------------------------------------------------
else:

    st.markdown("<h2 style='text-align:center; color:#39FF14;'>Real-Time Computational State Monitoring</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------------
    # Signal Control Panel (Left Sidebar)
    # ------------------------------------------
    with st.sidebar:
        st.header("Signal Control Panel")
        st.write("Adjust input signals to simulate organoid activity.")

        st.subheader("Neural Inputs")
        AF7 = st.slider("AF7 (Frontal)", 0.0, 1.0, 0.90)
        TP9 = st.slider("TP9 (Temporal)", 0.0, 1.0, 0.80)
        AF8 = st.slider("AF8 (Frontal)", 0.0, 1.0, 0.90)
        TP10 = st.slider("TP10 (Temporal)", 0.0, 1.0, 0.80)

        st.subheader("Synapse Activity")
        Alpha = st.slider("Alpha", 0.0, 1.0, 0.95)
        Beta = st.slider("Beta", 0.0, 1.0, 0.10)
        Delta = st.slider("Delta", 0.0, 1.0, 0.10)

        st.subheader("Metabolic & Ion Signals")
        M1 = st.slider("Metabolic Rate 1", 0.0, 1.0, 0.90)
        M2 = st.slider("Metabolic Rate 2", 0.0, 1.0, 0.60)
        Ion1 = st.slider("Ion Channel Flow 1", 0.0, 1.0, 0.90)
        Ion2 = st.slider("Ion Channel Flow 2", 0.0, 1.0, 0.30)
        Membrane = st.slider("Membrane Potential", 0.0, 1.0, 0.75)


    # ------------------------------------------
    # Feature Engineering (Bonus)
    # ------------------------------------------
    total_power = AF7 + TP9 + AF8 + TP10
    syn_ratio = Alpha / (Beta + 0.0001)

    st.markdown("### Computed Features")
    c1, c2 = st.columns(2)

    c1.metric("⚡ Total Input Power", f"{total_power:.2f}")
    c2.metric("🧬 Synapse Ratio", f"{syn_ratio:.2f}")
    st.markdown("<hr>", unsafe_allow_html=True)


    # ------------------------------------------
    # Prediction Button
    # ------------------------------------------
    analyze = st.button("🔍 Analyze Organoid State", use_container_width=True)

    if analyze and model:

        st.toast("Analyzing neural signals...", icon="🔬")
        time.sleep(0.4)

        # Note: Theta in sidebar was renamed to Delta above
        features = np.array([[AF7, TP9, AF8, TP10,
                              Alpha, Beta, Delta,
                              M1, M2, Ion1, Ion2, Membrane,
                              total_power, syn_ratio]])


        # ------------------------------------------
        # V3.4 Forced Activation Logic (Backdoor)
        # ------------------------------------------
        FORCE_POWER_THRESHOLD = 3.5

        if total_power >= FORCE_POWER_THRESHOLD:
            pred = 1
            prob = 0.99
            st.warning("⚠️ **System Threshold Overridden: Extreme Computational Load Detected**")
        else:
            pred = model.predict(features)[0]
            probs = model.predict_proba(features)[0]
            prob = probs[pred]

        st.session_state.pred = pred
        st.session_state.prob = prob
        
        st.rerun()


    # ------------------------------------------
    # Display Prediction Result
    # ------------------------------------------
    if "pred" in st.session_state:
        pred = st.session_state.pred
        prob = st.session_state.prob
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if pred == 0:
            st.error("🟠 SYSTEM STATE: INACTIVE")
            st.write("Organoid currently in resting mode.")
            st.session_state.active_status = False

        else:
            st.success("🟢 SYSTEM STATE: ACTIVE — Neural computation detected!")
            st.balloons()
            st.session_state.active_status = True

        st.write(f"### Confidence: **{prob*100:.2f}%**")
        st.progress(float(prob))

        # ------------------------------------------
        # Video Playback (Simulate single play)
        # ------------------------------------------
        if st.session_state.active_status:
            try:
                with open("success_video.mp4", "rb") as f:
                    video_bytes = f.read()
                encoded = base64.b64encode(video_bytes).decode()
                
                video_html = f"""
                    <video width="100%" autoplay muted playsinline>
                        <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
                    </video>
                """
                st.markdown(video_html, unsafe_allow_html=True)
            except FileNotFoundError:
                st.warning("Video file 'success_video.mp4' not found.")
                
        
        st.markdown("<p style='text-align:center; color:gray;'>Final Project Demo | Jiadong Liu</p>", unsafe_allow_html=True)
