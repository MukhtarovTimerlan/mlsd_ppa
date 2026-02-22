import joblib
import numpy as np
from .config import XGB_MODEL_PATH, SCALER_PATH, FEATURE_NAMES_PATH

# Глобальные переменные для модели и scaler (загружаются при старте)
_model = None
_scaler = None
_feature_names = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(XGB_MODEL_PATH)
    return _model

def load_scaler():
    global _scaler
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    return _scaler

def load_feature_names():
    global _feature_names
    if _feature_names is None:
        with open(FEATURE_NAMES_PATH, 'r') as f:
            _feature_names = [line.strip() for line in f.readlines()]
    return _feature_names

def preprocess_input(features: dict, scaler, feature_names):
    """
    Преобразует словарь признаков в массив, сортирует согласно порядку при обучении,
    применяет масштабирование.
    """
    # Создаём список значений в правильном порядке
    values = [features[name] for name in feature_names]
    X = np.array(values).reshape(1, -1)
    X_scaled = scaler.transform(X)
    return X_scaled