import requests

city = input("Enter City: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:


        data = response.json()


        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        description = current["weatherDesc"][0]["value"]

        print("\n========== WEATHER REPORT ==========")
        print(f"City        : {city.title()}")
        print(f"Temperature : {temp}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind} km/h")
        print(f"Condition   : {description}")
        print("====================================")

    else:
        print(f"Request Failed! Status Code: {response.status_code}")

except Exception as e:
    print("Error:", e)
