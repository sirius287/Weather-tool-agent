from fastapi import FastAPI
from pydantic import BaseModel
from weather_tool import get_weather

app = FastAPI()

class WeatherRequest(BaseModel):
    city: str

@app.get("/")
def home():
    return {"message": "Weather API is running 🚀"}

@app.post("/weather")
def weather(request: WeatherRequest):
    result = get_weather(request.city)

    if "error" in result:
        return {"error": result["error"]}

    return {
        "city": request.city.title(),
        "temperature": result["temperature"],
        "condition": result["condition"],
        "humidity": result["humidity"]
    }
