import matplotlib
matplotlib.use('TkAgg')  # Force the TkAgg backend for displaying the plot

import random
import matplotlib.pyplot as plt
import time

# Set up the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line1, = ax.plot([], [], label="Temperature (°C)", color="red")
line2, = ax.plot([], [], label="Humidity (%)", color="blue")
line3, = ax.plot([], [], label="Wind Speed (m/s)", color="green")

ax.set_xlim(0, 10)  # Set the x-axis limits
ax.set_ylim(0, 100)  # Set the y-axis limits (adjust based on your data range)
plt.xlabel("Time Interval")
plt.ylabel("Values")
plt.title("Simulated Weather Data")
plt.legend()

# Initialize data lists
temperatures = []
humidities = []
wind_speeds = []

# Simulate weather data collection with real-time plot update
for i in range(10):
    temperature = round(random.uniform(10.0, 30.0), 1)
    humidity = round(random.uniform(30.0, 80.0), 1)
    wind_speed = round(random.uniform(0.0, 15.0), 1)

    temperatures.append(temperature)
    humidities.append(humidity)
    wind_speeds.append(wind_speed)

    # Update the plot data
    line1.set_xdata(range(len(temperatures)))
    line1.set_ydata(temperatures)
    line2.set_xdata(range(len(humidities)))
    line2.set_ydata(humidities)
    line3.set_xdata(range(len(wind_speeds)))
    line3.set_ydata(wind_speeds)

    # Adjust the x-axis limits dynamically
    ax.set_xlim(0, len(temperatures) + 1)

    # Redraw the plot
    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(1)  # Simulate data collection delay

# Keep the plot open
plt.ioff()
plt.show()
