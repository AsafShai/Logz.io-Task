class OpenWeatherMapProvider:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        pass 

    async def get_weather_data(self, cities, client):
        try:
            for city in cities:
                geo_data_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
                response = await client.get(geo_data_url)
                if response.status_code != 200:
                    raise ValueError(f"Error fetching geo data from {source_name}: {response.status_code}")
                geo_data = response.json()
                lat = geo_data[0]['lat']
                lon = geo_data[0]['lon']
                weather_data_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
                response = await client.get(weather_data_url)
                if response.status_code != 200:
                    raise ValueError(f"Error fetching weather data from {source_name}: {response.status_code}")
                weather_data = response.json()
                city_data = {
                    "city": city,
                    "temperature_celsius": weather_data['current']['temp'],
                    "description": weather_data['current']['weather'][0]['description'],
                    "source_provider": source_name
                }
                data.append(city_data)
            return data
        except Exception as e:
            print(f"Error fetching data from {source_name}: {e}")
            return []