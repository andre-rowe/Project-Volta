# ⚡️ Project Volta

> **AI-powered Virtual Power Plant for Smarter, Cleaner Energy Grids**

---

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?logo=amazon-aws&logoColor=white)
![Grafana](https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white)
![InfluxDB](https://img.shields.io/badge/-InfluxDB-22ADF6?logo=influxdb&logoColor=white)

---

## 🌍 Overview

**Project Volta** was built during a Tesla-sponsored sustainability hackathon with one big goal:  
Make local energy grids smarter by teaching home batteries when to store and when to share.

Using **AI forecasting**, **reinforcement learning**, and real-time cloud architecture, this project simulates a microgrid that responds to energy demand like a pro — balancing sustainability and efficiency at the edge.

---

## 🚀 Key Features

- 🔮 **Forecasts Grid Demand:** Predicts next-hour usage with ML models (scikit-learn)
- ⚡ **RL-Controlled Battery Logic:** A DQN agent determines optimal charge/discharge timing
- 📊 **Live Analytics:** Time-series dashboards via Grafana + InfluxDB
- ☁️ **Cloud-Native:** Built on AWS IoT Core, Lambda, and CloudWatch for scalability

---

## 🧠 Tech Stack

| Category            | Tools/Tech                              |
|---------------------|------------------------------------------|
| Languages & AI      | Python, TensorFlow, scikit-learn         |
| Simulation Engine   | Custom Python logic, pandas, NumPy       |
| Infrastructure      | AWS IoT Core, Lambda, CloudWatch         |
| Data & Dashboards   | InfluxDB, Grafana, Docker                |

---

## 🖼️ Visuals

| AI-Driven Grid Simulation | RL Training Progress | Forecast Comparison |
|---------------------------|----------------------|----------------------|
| ![](docs/ai_power_grid.png) | ![](docs/rl_training_progress.png) | ![](docs/ai_vs_noai_comparison.png) |

---

## 📦 Getting Started

```bash
# Clone repo
git clone https://github.com/andre-rowe/Project-Volta.git
cd Project-Volta

# Install dependencies
pip install -r requirements.txt

# Run the simulation
python run_simulation.py

# (Optional) Start dashboard
docker-compose up
