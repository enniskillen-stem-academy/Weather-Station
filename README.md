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
   git clone https://github.com/enniskillen-stem-academy/Weather-Station.git
   cd Weather-Station
2. **Set Up a Virtual Environment**
    - It’s important to create a virtual environment to ensure all dependencies are installed in an isolated environment.
    - Create a Virtual Environment: Run the following command to create a virtual environment named venv:

    ```bash 
    python3 -m venv venv
    ```
    -   Activate the Virtual Environment:
    ```bash
    source venv/bin/activate
    ```
    - You should now see the virtual environment activated in your terminal. The terminal prompt will change to show (venv).


3. **Install the required dependencies:**
    ```bash
    pip3 install -r requirements.txt
4. **Optional: If you're using Homebrew on macOS, you might need to install python-tk to support matplotlib:**
    ```bash
    brew install python-tk
## Usage
- Run the main script:
    ```bash
    python3 weather_station.py
This will generate and display random weather data (temperature, humidity, and wind speed) every 5 seconds.
- Visualizing Data (Optional): To visualize the collected data on a graph, ensure matplotlib is installed, and run the script:
    ```bash 
    python3 weather_station_with_plot.py
This will generate and display a graph showing changes in temperature, humidity, and wind speed over time.

**Closing the project**
- When you're done working, remember to close the virtual environment

    ```bash
    deactivate
    ```
