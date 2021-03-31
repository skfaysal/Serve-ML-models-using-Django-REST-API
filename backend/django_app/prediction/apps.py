from django.apps import AppConfig
import pickle
import os



class DiabapiConfig(AppConfig):
    name = 'prediction'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'prediction/mlmodel/')
    
    # Load model
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "model_logreg.pkl")
    classifier = pickle.load(open(CLASSIFIER_FILE, 'rb'))

    # Load scaler
    SCLAER_FILE = os.path.join(CLASSIFIER_FOLDER, "sc.pkl")
    scaler = pickle.load(open(SCLAER_FILE, 'rb'))

