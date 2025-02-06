# Basic-weather-app
Highlights and Key Features of the Basic Weather App:
1.	OpenWeatherMap API Integration:
	Fetches real-time weather data using the OpenWeatherMap API, providing accurate metrics like temperature, humidity, and weather conditions.
2.	User-Friendly CLI Interface:
	Simple command-line interface (CLI) that prompts users to input a city or ZIP code and displays weather data in a clear, formatted manner.
3.	Error Handling:
	Robust error handling for invalid locations, API issues, or network errors. Gracefully informs users of problems instead of crashing.
4.	Metric Units Support:
	Displays temperature in Celsius and humidity as a percentage, catering to regions that use the metric system.
5.	Structured Data Parsing:
	Extracts and processes JSON responses from the API to retrieve only essential information (temperature, humidity, description).
6.	Modular Code Design:
	Separation of concerns: get_weather_data() handles API interactions, while main() manages user I/O, ensuring readability and maintainability.
7.	Lightweight and Dependency-Free:
	Uses only the requests library for API calls, keeping the project minimal and easy to run.
