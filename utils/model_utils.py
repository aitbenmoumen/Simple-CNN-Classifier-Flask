import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras. preprocessing import image
from PIL import Image
import os

class FruitClassifier:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.class_names = ['apple', 'banana', 'orange']
        self.img_size = (32, 32)
        
    def preprocess_image(self, img_path):
        img = Image.open(img_path).convert('RGB')
        img = img.resize(self.img_size)
        img_array = np.array(img)
    
        # img_array = img_array / 255.0  
        
        img_array = np.expand_dims(img_array, axis=0)    
        return img_array
    
    def predict(self, img_path):
        processed_img = self.preprocess_image(img_path)
        predictions = self.model.predict(processed_img, verbose=0)
        print(f"Predictions: {predictions}") 
        predicted_class_idx = np.argmax(predictions)
        predicted_class = self.class_names[predicted_class_idx]
        confidence = float(np.max(predictions)) * 100
        all_predictions = {
            self.class_names[i]: float(predictions[0][i]) * 100 
            for i in range(len(self.class_names))
        }
        
        return {
            'predicted_class': predicted_class,
            'confidence': round(confidence, 2),
            'all_predictions': all_predictions
        }