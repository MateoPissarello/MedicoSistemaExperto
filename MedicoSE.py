import json
from experta import Fact, KnowledgeEngine, Rule

class Sickness(Fact):
    """Información sobre una enfermedad"""
    pass


class DrHouse(KnowledgeEngine):

    # Variable para saber si ya se hizo un diagnóstico
    diagnosed = False
    diagnosis_result = {}  # Aquí almacenaremos el diagnóstico y tratamiento en formato diccionario

    # Regla para COVID-19
    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Tos persistente"),
        Sickness(symptom="Fatiga extrema"),
        Sickness(symptom="Dificultad para respirar"),
        Sickness(symptom="Congestión Nasal"),
    )
    def covid_19_treatment(self):
        if not self.diagnosed:  # Solo si aún no se ha diagnosticado
            self.diagnosis_result = {
                "diagnosis": "COVID-19",
                "treatment": "Reposo, hidratación, antivirales en casos graves"
            }
            self.diagnosed = True

    # Regla para Neumonía
    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Tos persistente"),
        Sickness(symptom="Fatiga extrema"),
        Sickness(symptom="Dificultad para respirar"),
    )
    def pneumonia_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Neumonía",
                "treatment": "Antibióticos si es bacteriana, oxigenoterapia si es grave"
            }
            self.diagnosed = True

    # Otras reglas de diagnóstico...

    # Regla final para cuando no se encuentra ningún diagnóstico
    @Rule()
    def no_diagnosis(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "No se pudo hacer un diagnóstico",
                "treatment": "Por favor, consulte a un médico para una evaluación más precisa."
            }

    def get_diagnosis_dict(self):
        return self.diagnosis_result


if __name__ == "__main__":
    engine = DrHouse()
    engine.reset()

    # Declarar los síntomas del paciente
    engine.declare(Sickness(symptom="Fiebre"))
    engine.declare(Sickness(symptom="Tos persistente"))
    engine.declare(Sickness(symptom="Fatiga extrema"))
    engine.declare(Sickness(symptom="Dificultad para respirar"))
    engine.declare(Sickness(symptom="Congestión Nasal"))

    # Ejecutar el motor de reglas
    engine.run()

    # Obtener el diagnóstico como dict
    diagnosis_dict = engine.get_diagnosis_dict()
    print(diagnosis_dict)
