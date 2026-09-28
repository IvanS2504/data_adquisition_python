#Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("data/generated_sensors.csv")

# Clean Data
data["temperature"] = pd.to_numeric(data["temperature"], errors="coerce")
data["pressure"] = pd.to_numeric(data["pressure"], errors="coerce")
data["humidity"] = pd.to_numeric(data["humidity"], errors="coerce")

data["temperature"] = data["temperature"].round(2)
data["pressure"] = data["pressure"].round(2)
data["humidity"] = data["humidity"].round(2)

data["temperature"].fillna(data["temperature"].mean(), inplace=True)
data["pressure"].fillna(data["pressure"].mean(), inplace=True)
data["humidity"].fillna(data["humidity"].mean(), inplace=True)

# Statistical calculations
results = {
    "temperature_mean": data["temperature"].mean(),
    "pressure_max": data["pressure"].max(),
    "pressure_min": data["pressure"].min(),
    "humidity_max": data["humidity"].max(),
    "humidity_min": data["humidity"].min()
}

# Print results
print("Average temperature:", results["temperature_mean"])
print("Maximum pressure:", results["pressure_max"])
print("Minimum pressure:", results["pressure_min"])
print("Maximum humidity:", results["humidity_max"])
print("Minimum humidity:", results["humidity_min"])

# Export results
pd.DataFrame([results]).to_csv("data/results.csv", index=False)


# Charts
plt.figure()
plt.plot(data["time"], data["temperature"], marker="o", label="Temperature (°C)")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Sensor Temperature Over Time")
plt.legend()
plt.grid(True)
plt.savefig("plots/sensor_temperature.png")
plt.show()

plt.figure()
plt.plot(data["time"], data["pressure"], marker="x", color="red", label="Pressure (bar)")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (bar)")
plt.title("Sensor Pressure Over Time")
plt.legend()
plt.grid(True)
plt.savefig("plots/sensor_pressure.png")
plt.show()

plt.figure()
plt.plot(data["time"], data["humidity"], marker="s", color="green", label="Humidity (%)")
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Sensor Humidity Over Time")
plt.legend()
plt.grid(True)
plt.savefig("plots/sensor_humidity.png")
plt.show()
