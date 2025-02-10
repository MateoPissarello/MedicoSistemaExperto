from fastapi import FastAPI
from pydantic import BaseModel
from MedicoSE import DrHouse, Sickness
import uvicorn

# Inicializar la aplicación FastAPI
app = FastAPI()


# Modelo de entrada para la API
class SymptomsRequest(BaseModel):
    symptoms: list[str]


# Endpoint para obtener el diagnóstico
@app.post("/get/diagnosis")
def get_diagnosis(request: SymptomsRequest):
    """
    Endpoint to get a diagnosis based on provided symptoms.

    This endpoint receives a POST request with a list of symptoms, processes them
    using the DrHouse inference engine, and returns the resulting diagnosis.

    Args:
        request (SymptomsRequest): A request object containing a list of symptoms.

    Returns:
        dict: A dictionary containing the diagnosis result.
    """
    engine = DrHouse()
    engine.reset()

    # Declarar los síntomas recibidos en la API
    for symptom in request.symptoms:
        engine.declare(Sickness(symptom=symptom))

    # Ejecutar el motor de inferencia
    engine.run()

    # Obtener el diagnóstico resultante
    diagnosis_result = engine.get_diagnosis_dict()

    return diagnosis_result


if __name__ == "__main__":
    uvicorn.run(app="Diagnostico:app", host="0.0.0.0", port=8000, reload=True)
