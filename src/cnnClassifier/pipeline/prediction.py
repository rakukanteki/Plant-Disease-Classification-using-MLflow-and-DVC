import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename  # Ensure correct attribute usage

    def predict(self):
        # Load the model
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess the image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0  # Normalize pixel values

        # Predict
        result = np.argmax(model.predict(test_image), axis=1)

        # Map prediction to class label
        class_labels = {0: "Early_Blight", 1: "Healthy", 2: "Late_Blight"}
        prediction = class_labels.get(result[0], "Unknown")  # Handle unexpected classes
        
        return [{"image": prediction}]
