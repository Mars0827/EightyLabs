import streamlit as st

def apply_styles():
    """Apply custom CSS styles to the Streamlit app"""
    
    st.markdown("""
    <style>
        /* Main Layout */
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .sub-header {
            font-size: 1.2rem;
            color: #7f8c8d;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .stApp {
            background-color: #f9f9f9;
        }
        
        /* Sidebar */
        .sidebar-header {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2c3e50;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        /* Upload Section */
        .upload-section {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
        }
        
        .upload-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        /* Results Section */
        .results-section {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }
        
        .section-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 1rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.5rem;
        }
        
        /* Prediction Results */
        .result-header {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        .status-pill {
            display: inline-block;
            padding: 0.25rem 1rem;
            border-radius: 2rem;
            color: white;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .confidence {
            font-size: 1.1rem;
            color: #7f8c8d;
            margin-bottom: 1rem;
        }
        
        .divider {
            height: 1px;
            background-color: #f0f0f0;
            margin: 1.5rem 0;
        }
        
        /* Information Section */
        .info-section {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .info-header {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        .info-text {
            color: #2c3e50;
            line-height: 1.5;
            margin-bottom: 1rem;
        }
        
        /* Probability Distribution */
        .prob-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        .prob-row {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        
        .prob-label {
            width: 70px;
            font-weight: 500;
        }
        
        .prob-bar-container {
            flex-grow: 1;
            height: 12px;
            background-color: #f0f0f0;
            border-radius: 6px;
            margin: 0 10px;
            overflow: hidden;
        }
        
        .prob-bar {
            height: 100%;
            border-radius: 6px;
        }
        
        .prob-bar.disease {
            background-color: #e74c3c;
        }
        
        .prob-bar.healthy {
            background-color: #2ecc71;
        }
        
        .prob-value {
            width: 60px;
            text-align: right;
            font-weight: 500;
        }
        
        /* Disclaimer */
        .disclaimer {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #7f8c8d;
            border-left: 4px solid #3498db;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-top: 1rem;
        }
        
        /* Improve Streamlit's default elements */
        div.stButton > button {
            width: 100%;
            border-radius: 5px;
            background-color: #3498db;
            color: white;
            font-weight: 500;
        }
        
        div.stButton > button:hover {
            background-color: #2980b9;
        }
    </style>
    """, unsafe_allow_html=True)