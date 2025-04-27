from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import pickle

# Initialize Flask app
app = Flask(__name__)
CORS(app)  

# Load the trained model
with open('model.pkl', 'rb') as model_file: # change lang ang model.pkl sa path sa ai model lodibells
    model = pickle.load(model_file)

# Route for detecting disease
@app.route('/detect', methods=['POST'])
def detect_disease():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']

    try:
        image = Image.open(image_file)
        image = image.convert('RGB')
    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'}), 400

    # Preprocess the image (resize, flatten)
    image = image.resize((224, 224))  # Resize to 224x224
    image_array = np.array(image)      # Convert image to numpy array
    image_array = image_array.flatten().reshape(1, -1)  # Flatten for model input

    try:
        prediction = model.predict(image_array)
        response = {'prediction': str(prediction[0])}
    except Exception as e:
        return jsonify({'error': f'Error making prediction: {str(e)}'}), 500

    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
