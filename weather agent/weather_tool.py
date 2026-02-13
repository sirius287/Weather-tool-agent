from weather_data import weather_db

def get_weather(city: str):
    city = city.strip().lower()

    # Create normalized dictionary
    normalized_db = {k.lower(): v for k, v in weather_db.items()}

    if city in normalized_db:
        return normalized_db[city]
    else:
        return {"error": f"City '{city}' not found in database"}
