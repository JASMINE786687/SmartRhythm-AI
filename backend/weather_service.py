import requests

API_KEY = "e53e76a7ec7866dcada1097c3cd1a403"

def get_weather(city="Tirunelveli"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q=Tirunelveli&appid=e53e76a7ec7866dcada1097c3cd1a403&units=metric"
        response = requests.get(url)
        data = response.json()

        temp = data["list"][0]["main"]["temp"]
        rainfall = data["list"][0].get("rain", {}).get("3h", 0)

        return {
            "temperature": temp,
            "rainfall": rainfall
        }

    except Exception as e:
        return {
            "temperature": None,
            "rainfall": 0
        }