"""This module provides functions to fetch weather data from the weather.gov API."""

import requests


def get_weather(lat, long):
    """
    Fetch and return the relative location's properties for the specified
    coordinates.
    Example: https://api.weather.gov/points/38.8894,-77.0352

    Args:
        lat: Latitude coordinate
        long: Longitude coordinate

    Returns:
        The hourly forecast data from the API.

    Raises:
        ValueError: If lat/long are not numeric.
        requests.RequestException: If there is an error fetching data.
    """
    if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
        raise ValueError("Latitude and Longitude must be numeric values.")

    try:
        base_url = "https://api.weather.gov/points/"
        response = requests.get(f"{base_url}{lat},{long}", timeout=60)
        data = response.json()
        return data["properties"]["forecastHourly"]
    except requests.RequestException as exc:
        raise requests.RequestException("Error fetching weather data") from exc
