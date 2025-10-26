import src.class_4_testing as weather_module
from unittest.mock import patch, Mock, MagicMock
import pytest
import requests

def test_get_weather():
    lat = 38.8894
    long = -77.0352
    expected_response = 'expected_forecast_data'

    mock_response = MagicMock()
    mock_response.json.return_value = {
        'properties': {'forecastHourly': expected_response}
    }
    weather_module.requests.get = Mock(return_value=mock_response)
    response = weather_module.get_weather(lat, long)
    assert response == expected_response, f"Expected {expected_response}, but got {response}"
    
@patch("src.class_4_testing.requests.get")
def test_get_weather_api_call(mock_get):
    lat = 38.8894
    long = -77.0352
    expected_response = 'expected_forecast_data'

    mock_get.return_value.json.return_value = {
        'properties': {'forecastHourly': expected_response}
    }

    response = weather_module.get_weather(lat, long)
    assert response == expected_response, f"Expected {expected_response}, but got {response}"


def test_get_weather_invalid_lat():
    invalid_lat = "invalid_lat"
    long = -77.0352

    with pytest.raises(ValueError) as exc_info:
        weather_module.get_weather(invalid_lat, long)

    assert str(exc_info.value) == "Latitude and Longitude must be numeric values."

def test_get_weather_invalid_long():
    invalid_lat = 38.8894
    long = "invalid_long"

    with pytest.raises(ValueError) as exc_info:
        weather_module.get_weather(invalid_lat, long)

    assert str(exc_info.value) == "Latitude and Longitude must be numeric values."

@patch("src.class_4_testing.requests.get")
def test_get_weather_api_call_error(mock_get):
    lat = 38.8894
    long = -77.0352
    mock_get.side_effect = requests.RequestException("API error simulated")

    with pytest.raises(requests.RequestException) as exc_info:
        weather_module.get_weather(lat, long)

    assert "Error fetching weather data" in str(exc_info.value)