import os
from fastapi import FastAPI, HTTPException

import uvicorn
import models
from helpers import perform_calculation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) Konfiguration
origins = ["*"]  # Hier können Sie spezifische Ursprünge anstelle von '*' angeben

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Erlaubt alle HTTP-Methoden (GET, POST, usw.)
    allow_headers=["*"],  # Erlaubt alle HTTP-Header
)

API_PORT = os.getenv("API_PORT", 8000)

@app.get("/")
async def root():
    """
    API Root
    """
    res = {
        "message": "Hello from the Calculator API",
        "status_code": 200
    }

    return res

@app.post("/calculate")
async def calculate(request_data: models.CalculationRequest):
    """
    Führt eine Berechnung auf einer Liste von Zahlen durch.

    :param request_data: Request-Body, der das Pydantic-Modell CalculationRequest verwendet
    :return: Ergebnis der Berechnung
    """
    numbers = request_data.numbers
    operator = request_data.operator

    # Überprüfen Sie, ob die erforderlichen Daten vorhanden sind
    if not numbers or not operator:
        raise HTTPException(status_code=400, detail="Ungültiger Request. Bitte geben Sie Zahlen und einen Operator an")

    result = perform_calculation(numbers, operator)
    rounded_result = round(result, 2)
    return {"result": rounded_result}
    

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(API_PORT), reload=False)