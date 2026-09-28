#Import libraries
import pandas as pd
import numpy as np

# Number of simulated reads to generate
n = 100

# Array for time (seconds, for example)
time = np.arange(n)

# Temperature simulation (mean 25°C, random variation)
temperature = 25 + np.random.normal(0, 0.5, n)

# Pressure simulation (mean 1.03 bar, random variation)
pressure = 1.03 + np.random.normal(0, 0.02, n)

# Humidity simulation (mean 40%, random variation)
humidity = 40 + np.random.normal(0, 5, n)

# Create DataFrame
data = pd.DataFrame({
    "time": time,
    "temperature": temperature,
    "pressure": pressure,
    "humidity": humidity
})

# Save CSV
data.to_csv("data/generated_sensors.csv", index=False)

print("Dataset generated and saved to data/generated_sensors.csv")
