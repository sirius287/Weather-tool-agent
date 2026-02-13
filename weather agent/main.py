import os
import json
from groq import Groq
from weather_tool import get_weather

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": (
            "Extract only the city name from the user's weather question. "
            "Respond ONLY with JSON in this format: "
            '{"city": "CityName"}'
        )
    }
]

while True:
    user_input = input("Ask about weather (or type exit): ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    content = response.choices[0].message.content
    print("Model raw output:", content)  # Debug line

    try:
        data = json.loads(content)
        city = data["city"]
    except:
        print("Could not extract city. Try again.")
        continue

    result = get_weather(city)

    if "error" in result:
        print(result["error"])
    else:
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {result['temperature']}")
        print(f"Condition: {result['condition']}")
        print(f"Humidity: {result['humidity']}\n")
