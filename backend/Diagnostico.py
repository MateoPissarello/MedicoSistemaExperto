from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from experta import Fact
from MedicoSE import DrHouse, Sickness
from fastapi.middleware.cors import CORSMiddleware

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

# Modelo de entrada para la API
class SymptomsRequest(BaseModel):
    symptoms: list[str]

# Endpoint para obtener el diagnóstico
@app.post("/get/diagnosis")
def get_diagnosis(request: SymptomsRequest):
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