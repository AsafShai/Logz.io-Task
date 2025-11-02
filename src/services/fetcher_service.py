import pandas as pd

class FetcherService:
    def __init__(self):
        pass

    async def fetch_data(self, client, data_source):
        cities = data_source['cities']
        source = data_source['source']
        source_type = data_source['source_type']
        if source_type == 'csv':
            data = await self.fetch_data_from_csv(source, cities)
        elif source_type == 'api':
            data = await self.fetch_data_from_api(client, data_source, cities)
        else:
            raise ValueError(f"Invalid source type: {source_type}")
        return data

    async def fetch_data_from_csv(self, source, cities):
        df = pd.read_csv(source)
        
        relevant_cities = df[df['city'].isin(cities)]
        relevant_cities['source_provider'] = source
        return relevant_cities.to_dict(orient='records')

    async def fetch_data_from_api(self, client, source, cities):
        API_KEY = source['API_KEY']
        source_name = source['source']
        if source_name == 'openweathermap':
            # TODO: add openweathermap support
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
        elif source_name == 'weatherapi':
            try:
                data = []
                for city in cities:
                    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
                    response = await client.get(url)
                    if response.status_code != 200:
                        raise ValueError(f"Error fetching data from {source_name}: {response.status_code}")
                    response_data = response.json()
                    city_data = {
                        "city": response_data['location']['name'],
                        "temperature_celsius": response_data['current']['temp_c'],
                        "description": response_data['current']['condition']['text'],
                        "source_provider": source_name
                    }
                    data.append(city_data)
                return data
            except Exception as e:
                print(f"Error fetching data from {source_name}: {e}")
                return []
        else:
            raise ValueError(f"The source is not supported: {source_name}")