import pickle
import os

# Get the absolute path of the model file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model.pkl')  # <- your renamed file

# Load the model
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_crop(features):
    """
    features: 2D array [[n, p, k, temp, humidity, ph, rainfall]]
    returns: predicted crop as string
    """
    return model.predict(features)[0]

