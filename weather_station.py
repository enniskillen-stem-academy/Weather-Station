import random  # Import the random module to generate random weather data
import time    # Import the time module to add delay between data updates

# Function to generate random weather data for temperature, humidity, and wind speed
def generate_weather_data():
    temperature = round(random.uniform(10.0, 30.0), 1)  # Random temperature between 10 and 30°C
    humidity = round(random.uniform(30.0, 80.0), 1)     # Random humidity between 30% and 80%
    wind_speed = round(random.uniform(0.0, 15.0), 1)    # Random wind speed between 0 and 15 m/s
    return temperature, humidity, wind_speed            # Return the generated weather data as a tuple

# Infinite loop to continuously generate and display weather data
while True:
    # Generate the weather data
    temperature, humidity, wind_speed = generate_weather_data()

    # Print the generated weather data
    print(f"Temperature: {temperature}°C")  # Display temperature
    print(f"Humidity: {humidity}%")         # Display humidity
    print(f"Wind Speed: {wind_speed} m/s")  # Display wind speed
    print("----------------------------")     # Print a separator for clarity

    # Wait for 5 seconds before generating the next set of weather data
    time.sleep(5)
