"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const symptoms = [
    "Fiebre",
    "Tos persistente",
    "Fatiga extrema",
    "Dificultad para respirar",
    "Congestión Nasal",
    "Dolor de cabeza",
    "Escalofríos",
    "Dolor muscular",
    "Diarrea",
    "Náuseas o vómitos",
];
document.addEventListener("DOMContentLoaded", () => {
    console.log("El archivo Syntoms.ts se está ejecutando");
    const container = document.getElementById("symptom-container");
    const button = document.getElementById("diagnose-btn");
    console.log("Container encontrado:", container);
    console.log("Button encontrado:", button);
    if (!container) {
        console.error("Error: No se encontró el elemento con id 'symptom-container'.");
        return;
    }
    let symptomCount = 0; // Inicializar en 0 para agregar el primero
    function addSymptomSelect() {
        if (symptomCount >= 5)
            return;
        const select = document.createElement("select");
        select.className = "symptom-select";
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = "Seleccione un síntoma";
        select.appendChild(defaultOption);
        symptoms.forEach(symptom => {
            const option = document.createElement("option");
            option.value = symptom;
            option.textContent = symptom;
            select.appendChild(option);
        });
        select.addEventListener("change", () => {
            if (select.value && symptomCount < 5) {
                symptomCount++;
                addSymptomSelect();
            }
        });
        container.appendChild(select);
    }
    // **Llamar a la función para mostrar el primer select**
    addSymptomSelect();
    button === null || button === void 0 ? void 0 : button.addEventListener("click", () => __awaiter(void 0, void 0, void 0, function* () {
        const selectedSymptoms = Array.from(document.querySelectorAll(".symptom-select"))
            .map(select => select.value)
            .filter(value => value);
        console.log("Síntomas seleccionados:", selectedSymptoms);
        if (selectedSymptoms.length === 0) {
            alert("Seleccione al menos un síntoma.");
            return;
        }
        try {
            const response = yield fetch("http://127.0.0.1:8000/get/diagnosis", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ symptoms: selectedSymptoms }),
            });
            if (!response.ok)
                throw new Error("Error en la solicitud");
            const data = yield response.json();
            console.log("Respuesta del backend:", data);
            alert(`Diagnóstico: ${data.diagnosis}\nTratamiento: ${data.treatment}`);
        }
        catch (error) {
            console.error("Error:", error);
            alert("Hubo un error al obtener el diagnóstico.");
        }
    }));
});
