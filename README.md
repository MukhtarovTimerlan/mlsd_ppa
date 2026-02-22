# California Housing Price Prediction Service

Сервис для предсказания медианной стоимости дома в Калифорнии на основе признаков из датасета California Housing.

## Установка и запуск

1. Клонировать репозиторий.
2. Создать виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux/Mac
   venv\Scripts\activate     # для Windows
   ```
3. Установить зависимости
    ```bash
    pip install -r requirements.txt
    ```
4. Запустить сервис - http://127.0.0.1:8000/docs
    ```bash
    python -m uvicorn app.main:app --reload
    ```
   
# Использование
Отправьте POST-запрос на /predgit initict с JSON, содержащим все признаки (включая созданные rooms_per_household и bedrooms_per_room).  
Пример:  
```json
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984,
  "AveBedrms": 1.023,
  "Population": 322.0,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23,
  "rooms_per_household": 2.73,
  "bedrooms_per_room": 0.15
}
```

## Ответ:
```json
{
  "prediction": 4.526,
  "status": "success"
}
```

# Модели
- Baseline: линейная регрессия (linear_model.pkl)

- Основная модель: XGBoost с tuned гиперпараметрами (xgb_model.pkl)

Для инференса используется XGBoost как лучшая модель.