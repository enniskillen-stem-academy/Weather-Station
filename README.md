# Weather Station STEM Project

## Overview
This project simulates a basic weather station that generates and displays weather data such as temperature, humidity, and wind speed using Python. The project helps students understand how weather data is collected and displayed in real-world applications, using random data generation and data visualization techniques.

## Project Goals
- Introduce students to random data generation in Python.
- Simulate weather data collection for temperature, humidity, and wind speed.
- Visualize the data using `matplotlib` by plotting graphs to show how the weather data changes over time.

## Features
- Generates random temperature (°C), humidity (%), and wind speed (m/s) values.
- Continuously updates and displays the simulated weather data every few seconds.
- Optionally visualizes the collected data using Python’s `matplotlib` library.

## Requirements
- Python 3.x
- `matplotlib` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-station-stem.git
   cd weather-station-stem
2. **Install the required dependencies: If matplotlib is not installed, install it using pip:**
    ```bash
    pip install matplotlib
3. **Optional: If you're using Homebrew on macOS, you might need to install python-tk to support matplotlib:**
    ```bash
    brew install python-tk

## Usage
- Run the main script:
    ```bash
    python3 weather_station.py
This will generate and display random weather data (temperature, humidity, and wind speed) every 5 seconds.
- Visualizing Data (Optional): To visualize the collected data on a graph, ensure matplotlib is installed, and run the script:
    ```bash 
    python weather_station_with_plot.py
This will generate and display a graph showing changes in temperature, humidity, and wind speed over time.

## Code Snippets
### Simulating Weather Data

```python
import random

def generate_weather_data():
    temperature = round(random.uniform(10.0, 30.0), 1)
    humidity = round(random.uniform(30.0, 80.0), 1)
    wind_speed = round(random.uniform(0.0, 15.0), 1)
    return temperature, humidity, wind_speed
```
### Plotting Weather Data

```python
import matplotlib.pyplot as plt

temperatures = [22.4, 21.1, 23.6, 24.0, 25.1]
humidities = [60.5, 55.0, 50.0, 53.2, 56.4]
wind_speeds = [5.4, 4.2, 6.1, 7.0, 6.3]

plt.plot(temperatures, label="Temperature (°C)")
plt.plot(humidities, label="Humidity (%)")
plt.plot(wind_speeds, label="Wind Speed (m/s)")
plt.legend()
plt.show()

```