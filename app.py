from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils.model_utils import FruitClassifier

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

os. makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

MODEL_PATH = 'models/fruit_classifier_modelCNN.h5' 
try:
    classifier = FruitClassifier(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    classifier = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if classifier is None:
        return jsonify({
            'error': 'Model not loaded. Please check server logs.'
        }), 500
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({
            'error': f'Invalid file type.  Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'
        }), 400
    
    try:
     
        filename = secure_filename(file.filename)
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        result = classifier.predict(filepath)
        

        result['image_url'] = f'/static/uploads/{filename}'
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app. route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': classifier is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)