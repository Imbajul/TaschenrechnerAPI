from pydantic import BaseModel
from typing import List

# Pydantic-Modell für den Request-Body
class CalculationRequest(BaseModel):
    numbers: List[float]
    operator: str