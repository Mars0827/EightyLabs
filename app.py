import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from PIL import Image
import io
from styles import apply_styles

# Set page configuration
st.set_page_config(
    page_title="Chicken Fecal Disease Classifier",
    page_icon="🐔",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_styles()

# Class names for our model
CLASS_NAMES = ['salmo', 'cocci', 'ncd', 'healthy']

# Disease descriptions
DISEASE_INFO = {
    'salmo': {
        'full_name': 'Salmonellosis',
        'description': 'A bacterial disease caused by Salmonella bacteria. It affects the digestive tract and can lead to diarrhea, dehydration, and weakness in chickens.',
        'treatment': 'Antibiotics prescribed by a veterinarian, improved sanitation, and isolation of affected birds.'
    },
    'cocci': {
        'full_name': 'Coccidiosis',
        'description': 'A parasitic disease caused by coccidian protozoa. It damages the intestinal lining and can cause bloody diarrhea, weight loss, and decreased egg production.',
        'treatment': 'Anticoccidial medications, improved litter management, and supportive care with electrolytes.'
    },
    'ncd': {
        'full_name': 'Newcastle Disease',
        'description': 'A highly contagious viral disease affecting respiratory, nervous, and digestive systems. Symptoms include respiratory distress, neurological signs, and decreased egg production.',
        'treatment': 'No specific treatment for the virus. Vaccination is the primary prevention method. Supportive care for affected birds.'
    },
    'healthy': {
        'full_name': 'Healthy',
        'description': 'No disease detected. The fecal sample appears normal.',
        'treatment': 'Continue with regular care, good nutrition, clean water, and proper sanitation.'
    }
}

def load_model_file():
    """Load the trained model."""
    try:
        model = load_model("ISMOBILE2.h5")
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def preprocess_image(img_file):
    """Preprocess the uploaded image for prediction."""
    img = Image.open(img_file).convert('RGB')
    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image
    return img, img_array

def predict(model, img_array):
    """Predict the class of the image."""
    preds = model.predict(img_array)
    pred_class_index = np.argmax(preds, axis=1)[0]
    confidence = preds[0][pred_class_index]
    predicted_class = CLASS_NAMES[pred_class_index]
    return predicted_class, confidence, preds[0]

def display_result(predicted_class, confidence, all_probs):
    """Display the prediction results."""
    st.markdown(f'<div class="result-header">{DISEASE_INFO[predicted_class]["full_name"]}</div>', unsafe_allow_html=True)
    
    # Determine the status color based on the prediction
    if predicted_class == 'healthy':
        status_color = "green"
    else:
        status_color = "red"
    
    st.markdown(f'<div class="status-pill" style="background-color: {status_color};">{predicted_class.upper()}</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="confidence">Confidence: {confidence:.2%}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Description and treatment info
    st.markdown('<div class="info-section">', unsafe_allow_html=True)
    st.markdown(f'<div class="info-header">Description:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-text">{DISEASE_INFO[predicted_class]["description"]}</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="info-header">Treatment/Action:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-text">{DISEASE_INFO[predicted_class]["treatment"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show probabilities for all classes
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="prob-header">Probability Distribution</div>', unsafe_allow_html=True)
    
    # Create a bar chart for probabilities
    probs_dict = {CLASS_NAMES[i]: float(all_probs[i]) for i in range(len(CLASS_NAMES))}
    sorted_probs = sorted(probs_dict.items(), key=lambda x: x[1], reverse=True)
    
    for class_name, prob in sorted_probs:
        # Determine the width of the progress bar based on probability
        bar_width = int(prob * 100)
        status = "healthy" if class_name == "healthy" else "disease"
        st.markdown(
            f'''
            <div class="prob-row">
                <div class="prob-label">{class_name}</div>
                <div class="prob-bar-container">
                    <div class="prob-bar {status}" style="width: {bar_width}%;"></div>
                </div>
                <div class="prob-value">{prob:.2%}</div>
            </div>
            ''', 
            unsafe_allow_html=True
        )

def main():
    # Header
    st.markdown('<div class="main-header">Chicken Fecal Disease Classifier</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Upload an image to detect potential diseases</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/chicken.png", width=100)
        st.markdown('<div class="sidebar-header">About</div>', unsafe_allow_html=True)
        st.markdown(
            """
            This application detects diseases in chicken fecal samples using a trained deep learning model.
            
            **Supported diseases:**
            - Salmonellosis (salmo)
            - Coccidiosis (cocci)
            - Newcastle Disease (ncd)
            - Healthy samples
            
            Upload a clear image of a chicken fecal sample for accurate detection.
            """
        )
        st.markdown('<div class="sidebar-header">Instructions</div>', unsafe_allow_html=True)
        st.markdown(
            """
            1. Click "Browse files" to upload an image
            2. Wait for the model to analyze the image
            3. Review the diagnosis and recommended actions
            """
        )
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="footer">Powered by MobileNetV3 • TensorFlow</div>', unsafe_allow_html=True)
    
    # Main content area
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown('<div class="upload-header">Upload Fecal Sample Image</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Load model
    model = load_model_file()
    
    # Process uploaded image
    if uploaded_file is not None and model is not None:
        try:
            # Display the image and prediction in columns
            st.markdown('<div class="results-section">', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1.5])
            
            # Process and display image
            with col1:
                st.markdown('<div class="section-header">Uploaded Sample</div>', unsafe_allow_html=True)
                img, processed_img = preprocess_image(uploaded_file)
                st.image(img, use_column_width=True)
            
            # Make prediction and display result
            with col2:
                st.markdown('<div class="section-header">Diagnosis</div>', unsafe_allow_html=True)
                
                # Add a spinner during prediction
                with st.spinner("Analyzing sample..."):
                    predicted_class, confidence, all_probs = predict(model, processed_img)
                
                # Display prediction results
                display_result(predicted_class, confidence, all_probs)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Disclaimer
            st.markdown(
                """
                <div class="disclaimer">
                    <strong>Disclaimer:</strong> This tool is intended for educational purposes only and should not replace professional veterinary diagnosis. 
                    Always consult with a veterinarian for proper diagnosis and treatment of animal diseases.
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()