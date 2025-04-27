import requests

def get_weather(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return {"error": "City not found"}

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return {"weather": weather, "temperature": temperature}
