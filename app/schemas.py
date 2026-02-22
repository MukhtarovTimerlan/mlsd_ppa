from pydantic import BaseModel, Field, validator
from typing import Optional

class HouseFeatures(BaseModel):
    MedInc: float = Field(..., ge=0, description="Медианный доход в блоке (десятки тысяч $)")
    HouseAge: float = Field(..., ge=0, le=100, description="Медианный возраст дома (годы)")
    AveRooms: float = Field(..., ge=0, description="Среднее количество комнат на домохозяйство")
    AveBedrms: float = Field(..., ge=0, description="Среднее количество спален на домохозяйство")
    Population: float = Field(..., ge=0, description="Население блока")
    AveOccup: float = Field(..., ge=0, description="Среднее количество членов домохозяйства")
    Latitude: float = Field(..., ge=32, le=42, description="Широта")
    Longitude: float = Field(..., ge=-125, le=-114, description="Долгота")
    rooms_per_household: Optional[float] = Field(None, ge=0, description="Комнат на человека")
    bedrooms_per_room: Optional[float] = Field(None, ge=0, le=1, description="Спален на комнату")

    @validator('AveRooms', 'AveBedrms', 'AveOccup', pre=True, always=True)
    def check_positive(cls, v):
        if v <= 0:
            raise ValueError('Значение должно быть положительным')
        return v

class PredictionResponse(BaseModel):
    prediction: float = Field(..., description="Предсказанная медианная стоимость дома (сотни тысяч $)")
    status: str = Field("success", description="Статус запроса")