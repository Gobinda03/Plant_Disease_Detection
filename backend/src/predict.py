import numpy as np
import tensorflow as tf
from pathlib import Path
from backend.src.logger import log_event


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "ai" / "models" / "trained_plant_disease_model.keras"
CLASS_NAMES = BASE_DIR / "ai" / "models" / "class_names.json"

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

CLASS_NAMES = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

def predict_disease(image):
    img = tf.keras.preprocessing.image.load_img(
        image,
        target_size=(128,128)
    )

    arr = tf.keras.preprocessing.image.img_to_array(img)

    arr = np.expand_dims(arr, axis=0)

    prediction = model.predict(arr)

    idx = np.argmax(prediction)

    confidence = float(np.max(prediction))*100

    log_event(
        "DISEASE DETECTED",
        {
            "disease": CLASS_NAMES[idx],
            "confidence": confidence
        }
    )

    return CLASS_NAMES[idx], confidence