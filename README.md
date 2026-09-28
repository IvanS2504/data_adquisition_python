# Sensor Data Simulation and Analysis

This project simulates industrial sensor readings (temperature, pressure, humidity) using Python, and performs data acquisition, cleaning, statistical analysis, and visualization with **Pandas** and **Matplotlib**.

## 📂 Project Structure
- `src/generation.py` → generates random sensor datasets and saves them as CSV.
- `src/adquisition.py` → reads datasets, cleans invalid values, calculates metrics, and creates plots.
- `data/` → contains raw and processed datasets.
- `plots/` → stores generated plots.
- `README.md` → documentation.

## ⚙️ Features
- Generate datasets with NumPy (`arange`, `random.normal`).
- Handle invalid sensor values (`ERROR` → converted to NaN).
- Clean and preprocess data (rounding, filling missing values).
- Calculate metrics (mean, max, min, differences).
- Export results to CSV.
- Visualize sensor data with Matplotlib.

## 📦 Requirements
- Python 3.10+
- pandas
- numpy
- matplotlib


Install dependencies:
```bash
pip install pandas numpy matplotlib
```
## 🚀 How to Run
1. Clone the repository
2. Run dataset generation
```bash 
python src/generation.py
```
3. Run data adquisition and analysis
```bash
python src/adquisition.py
```

## 📊 Example Dataset
| time | temperature | pressure | humidity |
|------|-------------|----------|----------|
| 0    | 25.32       | 1.02     | 39.8     |
| 1    | 25.47       | 1.01     | 41.2     |

## 📑 Results
The script exports statistical metrics to `data/results.csv`:
- Average temperature
- Maximum and minimum pressure
- Maximum and minimum humidity

## 🔮 Future Work
- Add support for Excel input/output
- Connect to real sensors (ESP32)
- Build interactive dashboards with Streamlit

## 📜 License
This project is licensed under the MIT License.
