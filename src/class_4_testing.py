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
	dict: The properties of the relative location.
	"""
	if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
		raise ValueError("Latitude and Longitude must be numeric values.")
	
	try:
		base_url = "https://api.weather.gov/points/"
		response = requests.get(f"{base_url}{lat},{long}")
		data = response.json()
		return data['properties']['forecastHourly']
	except requests.RequestException:
		raise requests.RequestException("Error fetching weather data")