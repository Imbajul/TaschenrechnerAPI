from typing import List
from fastapi import HTTPException

def perform_calculation(numbers: List[float], operator: str) -> float:
    """
    Führt die eigentliche Berechnung basierend auf den gegebenen Zahlen und dem Operator durch.

    :param numbers: Liste von Zahlen
    :param operator: Mathematischer Operator (addieren, subtrahieren, multiplizieren, dividieren)
    :return: Ergebnis der Berechnung
    """
    if operator == "add":
        return sum(numbers)
    elif operator == "subtract":
        return numbers[0] - sum(numbers[1:])
    elif operator == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operator == "divide":
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise HTTPException(status_code=400, detail="Division durch Null ist nicht erlaubt")
            result /= num
        return result
    else:
        raise HTTPException(status_code=400, detail="Ungültiger Operator. Unterstützte Operatoren sind addieren, subtrahieren, multiplizieren, dividieren")