import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city, api_key):
    """
    Fetches weather data for a specified city using the OpenWeatherMap API.

    Parameters:
    city (str): The name of the city for which to fetch weather data.
    api_key (str): The API key for authenticating with the OpenWeatherMap API.

    Returns:
    dict: A JSON response containing weather data for the specified city.
    """
    # Construct the API URL with the city name and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a GET request to the API and return the JSON response
    response = requests.get(url)
    return response.json()

# Function to extract relevant weather information from the API response
def extract_weather_info(data):
    """
    Extracts temperature, humidity, and weather description from the API response.

    Parameters:
    data (dict): The JSON response from the OpenWeatherMap API.

    Returns:
    tuple: A tuple containing:
        - temperature (float): The temperature in Celsius.
        - humidity (int): The humidity in percentage.
        - description (str): A brief description of the weather.
    """
    # Extract main weather data
    main = data['main']
    weather = data['weather'][0]  # Index 0 is the current weather
    
    # Get temperature, humidity, and weather description
    temperature = main['temp']  # Temperature in Celsius
    humidity = main['humidity']  # Humidity in percentage
    description = weather['description']  # Weather description
    
    return temperature, humidity, description

# Function to plot weather data using Seaborn
def plot_weather_data_seaborn(temperature, humidity):
    """
    Plots temperature and humidity data using a bar plot.

    Parameters:
    temperature (float): The temperature in Celsius.
    humidity (int): The humidity in percentage.
    """
    # Create a DataFrame for plotting
    data = pd.DataFrame({
        'Category': ['Temperature (°C)', 'Humidity (%)'],
        'Value': [temperature, humidity]
    })

    # Create a bar plot using Seaborn
    sns.barplot(x='Category', y='Value', hue='Category', data=data, palette='viridis', legend=False)
    plt.title('Weather Data')
    plt.ylabel('Values')
    plt.show()

# Main function to execute the script
def main():
    """
    Main function to execute the weather data fetching and plotting process.
    Prompts the user for a city name and fetches the corresponding weather data.
    """
    # Get user input for API key and city
    api_key = "10d72fbc427d48e2e1d82043fed17aee"  # Replace with your own API key from OpenWeatherMap
    city = input("Enter the city name: ")  # Specify the city for which you want the weather data

    # Fetch weather data
    weather_data = get_weather_data(city, api_key)

    # Check if the response is valid
    if weather_data.get('cod') != 200:
        print(f"Error fetching data: {weather_data.get('message')}")
        return

    # Extract relevant information
    temperature, humidity, description = extract_weather_info(weather_data)
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Description: {description}")

    # Plot using Seaborn
    plot_weather_data_seaborn(temperature, humidity)

# Execute the main function
if __name__ == "__main__":
    main()
