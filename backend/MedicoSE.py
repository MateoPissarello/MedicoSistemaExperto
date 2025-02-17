import json
from experta import Fact, KnowledgeEngine, Rule

class Sickness(Fact):
    """Información sobre una enfermedad"""
    pass


class DrHouse(KnowledgeEngine):
    """
    DrHouse is a knowledge-based expert system for diagnosing and suggesting treatments for various illnesses based on symptoms.
    Attributes:
        diagnosed (bool): A flag to indicate if a diagnosis has been made.
        diagnosis_result (dict): A dictionary to store the diagnosis and treatment.
    Methods:
        covid_19_treatment(): Diagnoses and suggests treatment for COVID-19.
        pneumonia_treatment(): Diagnoses and suggests treatment for pneumonia.
        flu_treatment(): Diagnoses and suggests treatment for influenza (flu).
        allergy_treatment(): Diagnoses and suggests treatment for respiratory allergies.
        arthritis_treatment(): Diagnoses and suggests treatment for rheumatoid arthritis.
        measles_treatment(): Diagnoses and suggests treatment for measles.
        gastroenteritis_treatment(): Diagnoses and suggests treatment for viral gastroenteritis.
        dengue_treatment(): Diagnoses and suggests treatment for dengue fever.
        ulcer_treatment(): Diagnoses and suggests treatment for gastric ulcers.
        no_diagnosis(): Provides a default message when no diagnosis can be made.
        get_diagnosis_dict(): Returns the diagnosis and treatment as a dictionary.
    """
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

    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Tos persistente"),
        Sickness(symptom="Dolor de cabeza"),
        Sickness(symptom="Fatiga extrema"),
        Sickness(symptom="Escalofríos"),
    )
    def flu_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Gripe (Influenza)",
                "treatment": "Reposo, líquidos, antivirales en casos específicos"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Tos persistente"),
        Sickness(symptom="Dificultad para respirar"),
        Sickness(symptom="Congestión Nasal"),
    )
    def allergy_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Alergia respiratoria",
                "treatment": "Antihistamínicos, evitar alérgenos"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Fatiga extrema"),
        Sickness(symptom="Escalofríos"),
    )
    def arthritis_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Artritis reumatoide",
                "treatment": "Antiinflamatorios, fisioterapia"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Dolor de cabeza"),
        Sickness(symptom="Dolor muscular"),
        Sickness(symptom="Congestión Nasal"),
    )
    def measles_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": " Sarampión",
                "treatment": "Manejo de síntomas, aislamiento, vacunas para prevención"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Diarrea"),
        Sickness(symptom="Náuseas o vómitos"),
    )
    def gastroenteritis_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": " Gastroenteritis viral",
                "treatment": "Hidratación, dieta blanda, medicamentos sintomáticos"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Fiebre"),
        Sickness(symptom="Fatiga extrema"),
        Sickness(symptom="Dolor muscular"),
        Sickness(symptom="Escalofríos"),
    )
    def dengue_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Dengue",
                "treatment": "Hidratación, control de fiebre y dolor"
            }
            self.diagnosed = True

    @Rule(
        Sickness(symptom="Diarrea"),
        Sickness(symptom="Fatiga extrema"),
    )
    def ulcer_treatment(self):
        if not self.diagnosed:
            self.diagnosis_result = {
                "diagnosis": "Úlcera gástrica",
                "treatment": "Antiácidos, inhibidores de la bomba de protones, dieta adecuada"
            }
            self.diagnosed = True


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
