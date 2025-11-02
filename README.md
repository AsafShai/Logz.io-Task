# Logz.io Weather Data Task

This application fetches weather data from multiple sources (CSV files and weather APIs) and sends it to Logz.io for logging and monitoring.

## Configuration

Create a `config.json` file in the root directory with the following structure:

### config.json Template and example. You can use any city

```json
{
    "data_sources": [
        {
            "source": "weather.csv",
            "source_type": "csv",
            "cities": ["Berlin", "Sydney"]
        },
        {
            "source": "openweathermap",
            "source_type": "api",
            "API_KEY": "YOUR_OPENWEATHERMAP_API_KEY_HERE",
            "API_URL": "https://api.openweathermap.org/data/2.5/weather",
            "cities": ["Berlin", "Sydney"]
        },
        {
            "source": "weatherapi",
            "source_type": "api",
            "API_KEY": "YOUR_WEATHERAPI_API_KEY_HERE",
            "API_URL": "https://api.weatherapi.com/v1/current.json",
            "cities": ["Berlin", "Sydney"]
        }
    ],
    "logz_io": {
        "listener_host": "listener-eu.logz.io",
        "listener_port": 8071,
        "listener_token": "YOUR_LOGZ_IO_TOKEN_HERE"
    },
    "polling_interval": 60
}
```

### Configuration Fields

#### Data Sources
- **`source`**: Identifier for the data source
- **`source_type`**: Either `"csv"` or `"api"`
- **`API_KEY`**: Your API key (required for API sources)
- **`API_URL`**: The API endpoint URL
- **`cities`**: Array of city names to fetch weather data for

#### Logz.io Settings
- **`listener_host`**: Your Logz.io listener host (e.g., `listener-eu.logz.io`, `listener-us.logz.io`)
- **`listener_port`**: 
  - Use `8071` for HTTPS (recommended)
  - Use `8070` for HTTP
- **`listener_token`**: Your Logz.io shipping token

#### Application Settings
- **`polling_interval`**: Time in seconds between data fetches

## API Keys

You'll need to obtain API keys from:
1. **OpenWeatherMap**: [https://api.openweathermap.org/data/3/weather](https://api.openweathermap.org/data/3/weather)
2. **WeatherAPI**: [https://api.weatherapi.com/v1/current.json](https://api.weatherapi.com/v1/current.json)
3. **Logz.io**: Get your shipping token from your Logz.io account settings

## Running the Application

```bash
# Install dependencies
uv sync

# Run the application
uv run -m src.main
```

## Security Note