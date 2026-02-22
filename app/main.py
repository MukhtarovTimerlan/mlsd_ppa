from fastapi import FastAPI, HTTPException, Depends
from .schemas import HouseFeatures, PredictionResponse
from .dependencies import load_model, load_scaler, load_feature_names, preprocess_input

app = FastAPI(
    title="California Housing Price Prediction API",
    description="Сервис для предсказания медианной стоимости дома в Калифорнии",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    # Предзагружаем модель, scaler и имена признаков при старте
    load_model()
    load_scaler()
    load_feature_names()
    print("Модель и scaler загружены")

@app.get("/")
def root():
    return {"message": "Добро пожаловать в API оценки стоимости жилья. Используйте /predict для предсказания."}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: HouseFeatures):
    try:
        # Получаем зависимости
        model = load_model()
        scaler = load_scaler()
        feature_names = load_feature_names()

        # Преобразуем входные данные в словарь (игнорируя поля, которых нет в обучении)
        input_dict = features.dict()
        # Убираем опциональные поля, которые могут отсутствовать в feature_names
        # (rooms_per_household и bedrooms_per_room должны быть, если они использовались при обучении)
        # Проверяем, что все необходимые признаки присутствуют
        missing = [f for f in feature_names if f not in input_dict]
        if missing:
            raise HTTPException(status_code=400, detail=f"Отсутствуют признаки: {missing}")

        # Предобработка
        X_scaled = preprocess_input(input_dict, scaler, feature_names)

        # Предсказание
        pred = model.predict(X_scaled)[0]

        return PredictionResponse(prediction=float(pred), status="success")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))