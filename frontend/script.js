document.getElementById("apiBtn").addEventListener("click", async () => {

  const village = document.getElementById("village").value;

  // Example OpenWeather API (Replace YOUR_API_KEY)
  const apiKey = "YOUR_API_KEY";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${village}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    alert(
      `🌦 Temperature: ${data.main.temp}°C
Humidity: ${data.main.humidity}%
Weather: ${data.weather[0].description}`
    );
  } catch (error) {
    alert("API Error");
  }
});
document.getElementById("confidenceBar").style.width = confidence + "%";

document.getElementById("analyzeBtn").addEventListener("click", function () {

  const crop = document.getElementById("crop").value;

  let irrigation = "";
  let confidence = 0;
  let risk = "";

  // Simulated AI Decision Logic
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js");
  }
  if (crop === "Paddy") {
    irrigation = "YES";
    confidence = 82;
    risk = "HIGH RISK";
  } 
  else if (crop === "Groundnut") {
    irrigation = "NO";
    confidence = 68;
    risk = "LOW RISK";
  } 
  else {
    irrigation = "YES";
    confidence = 74;
    risk = "MODERATE RISK";
  }
  const ctx = document.getElementById('waterChart').getContext('2d');

const waterChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Irrigation', 'Storage', 'Domestic Use'],
    datasets: [{
      label: 'Water Distribution (Litres)',
      data: [50, 30, 20],
      backgroundColor: [
        '#2EC4B6',
        '#1D3557',
        '#E63946'
      ]
    }]
  }
});

  // Update UI
  const irrigationElement = document.getElementById("irrigationResult");
  irrigationElement.innerText = irrigation;

  if (irrigation === "YES") {
    irrigationElement.className = "yes";
  } else {
    irrigationElement.className = "no";
  }

  document.getElementById("confidence").innerText = confidence + "%";

  const riskElement = document.getElementById("riskLevel");
  riskElement.innerText = risk;

  if (risk === "HIGH RISK") {
    riskElement.className = "risk-high";
  } else {
    riskElement.className = "risk-low";
  }
});