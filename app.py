import streamlit as st
from model_utils import load_classification_model, load_and_preprocess_image, predict
from config import class_names
from styles import css
import os

# Set page configuration
st.set_page_config(
    page_title="Image Classifier",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(css, unsafe_allow_html=True)

# Main app header
st.markdown('<div class="main-header">Image Classification App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload an image to classify using MobileNetV3</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://www.tensorflow.org/images/tf_logo_social.png", width=150)
    st.title("About")
    st.info(
        """
        This application uses a pre-trained MobileNetV3 model to classify chicken fecal images.
        
        Simply upload an image, and the model will predict what type of chicken disease.
        
        The model was trained on custom data and saved as 'capstone1mobilenetsv3.h5'.
        """
    )
    st.write("---")
    st.write("Model: MobileNetV3")

    # Add confidence threshold slider
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="Predictions with confidence below this threshold will be shown as uncertain"
    )

# Load model
model = None
try:
    if os.path.exists("capstone1mobilenetsv3.h5"):
        model = load_classification_model("capstone1mobilenetsv3.h5")
        st.success("Model loaded successfully!")
    else:
        st.error("Model file not found. Please ensure 'capstone1mobilenetsv3.h5' is in the same directory as this app.")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

# Upload section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image to classify", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Main functionality
if uploaded_file is not None and model is not None:
    try:
        st.markdown('<div class="results-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Uploaded Image")
            img, processed_img = load_and_preprocess_image(uploaded_file)
            st.image(img, width=300, caption="Uploaded Image")
        
        with col2:
            st.subheader("Classification Results")
            predicted_class, confidence, all_predictions = predict(model, processed_img, class_names)
            
            st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
            
            if confidence >= confidence_threshold:
                st.markdown(f"<h3 style='color: #1E88E5;'>Prediction: {predicted_class}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h4>Confidence: {confidence:.2%}</h4>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h3 style='color: #FFA726;'>Uncertain Prediction</h3>", unsafe_allow_html=True)
                st.markdown(f"<h4>Best guess: {predicted_class} (Confidence: {confidence:.2%})</h4>", unsafe_allow_html=True)
                st.markdown("<p>Confidence is below the threshold. The model is uncertain about this prediction.</p>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

            st.write("---")
            st.write("Probabilities for all classes:")
            probs_dict = {class_names[i]: float(all_predictions[i]) for i in range(len(class_names))}
            sorted_probs = sorted(probs_dict.items(), key=lambda x: x[1], reverse=True)
            chart_data = {
                "Class": [item[0] for item in sorted_probs],
                "Probability": [item[1] for item in sorted_probs]
            }
            st.bar_chart(chart_data, x="Class", y="Probability", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error processing image: {str(e)}")

# Footer
st.markdown('<div class="footer">Developed for image classification using TensorFlow and MobileNetV3.</div>', unsafe_allow_html=True)
