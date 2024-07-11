from pydantic import BaseModel

class WeightPredictModel(BaseModel):
    height: float
    
    