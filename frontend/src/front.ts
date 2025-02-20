const symptoms: string[] = [
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
  
    const container = document.getElementById("symptom-container") as HTMLDivElement;
    const button = document.getElementById("diagnose-btn") as HTMLButtonElement;
  
    console.log("Container encontrado:", container);
    console.log("Button encontrado:", button);
  
    if (!container) {
      console.error("Error: No se encontró el elemento con id 'symptom-container'.");
      return;
    }
  
    let symptomCount = 0; // Inicializar en 0 para agregar el primero
  
    function addSymptomSelect(): void {
      if (symptomCount >= 5) return;
  
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
  
    button?.addEventListener("click", async () => {
      const selectedSymptoms = Array.from(document.querySelectorAll(".symptom-select"))
        .map(select => (select as HTMLSelectElement).value)
        .filter(value => value);
  
      console.log("Síntomas seleccionados:", selectedSymptoms);
  
      if (selectedSymptoms.length === 0) {
        alert("Seleccione al menos un síntoma.");
        return;
      }
  
      try {
        const response = await fetch("http://127.0.0.1:8000/get/diagnosis", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ symptoms: selectedSymptoms }),
        });
  
        if (!response.ok) throw new Error("Error en la solicitud");
  
        const data = await response.json();
        console.log("Respuesta del backend:", data);
        alert(`Diagnóstico: ${data.diagnosis}\nTratamiento: ${data.treatment}`);
      } catch (error) {
        console.error("Error:", error);
        alert("Hubo un error al obtener el diagnóstico.");
      }
    });
  });
  