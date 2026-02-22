import os
from pathlib import Path

# Корневая папка проекта
ROOT_DIR = Path(__file__).parent.parent

# Пути к моделям
MODELS_DIR = ROOT_DIR / "models"
XGB_MODEL_PATH = MODELS_DIR / "xgb_model.pkl"
SCALER_PATH = MODELS_DIR / "scaler.pkl"
FEATURE_NAMES_PATH = MODELS_DIR / "feature_names.txt"