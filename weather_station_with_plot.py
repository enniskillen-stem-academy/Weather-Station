import matplotlib
matplotlib.use('TkAgg')  # Force the TkAgg backend for displaying the plot

import random
import matplotlib.pyplot as plt
import time

# Simulate weather data collection
temperatures = []
humidities = []
wind_speeds = []

for _ in range(10):
    temperature = round(random.uniform(10.0, 30.0), 1)
    humidity = round(random.uniform(30.0, 80.0), 1)
    wind_speed = round(random.uniform(0.0, 15.0), 1)

    temperatures.append(temperature)
    humidities.append(humidity)
    wind_speeds.append(wind_speed)

    time.sleep(1)  # Simulate time delay for data collection

# Plot the data
plt.plot(temperatures, label="Temperature (°C)", color="red")
plt.plot(humidities, label="Humidity (%)", color="blue")
plt.plot(wind_speeds, label="Wind Speed (m/s)", color="green")

plt.xlabel("Time Interval")
plt.ylabel("Values")
plt.title("Simulated Weather Data")
plt.legend()

# Ensure the plot stays open
plt.show(block=True)  # This forces the window to stay open
