<h1 align="center">⚡ Project Volta</h1>

<p align="center">
  <b>A reinforcement-learning agent that dispatches a simulated home-battery fleet as a virtual power plant.</b><br/>
  <sub>Academic project · 2025 · custom Python simulation</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter"/>
</p>

---

## Overview

Rising rooftop solar and EV charging strain local distribution grids, and unsynchronized home batteries leave stored capacity idle exactly when it's needed. **Project Volta** explores a fix in simulation: coordinate a fleet of home batteries as a single **virtual power plant** that learns *when* to charge and *when* to discharge, smoothing the load the grid actually sees.

It pairs a **Deep Q-Network (DQN)** control agent with a **demand-forecasting** model inside a custom Python environment. Everything here runs in simulation — the goal was to prove the control strategy, not to ship hardware.

## What's in this repo

```
src/simulation/
  battery_env.py        # custom environment (Gym-style reset/step API) — 13.5 kWh cell, 96×15-min steps
  rl_control/           # DQN control logic
notebooks/
  train_dqn.ipynb       # trains the TensorFlow DQN agent against the environment
  volta_forecast.ipynb  # scikit-learn next-hour demand forecast
  volta_visualization.ipynb  # training-reward and with/without-agent analysis
data/
  volta_data.py         # synthetic solar / demand / battery data generator
  volta_simulated_data.csv
docs/                   # exported figures
```

## How it works

1. **Environment** — `BatteryEnv` models state-of-charge, solar input, and forecast demand, exposing `hold / charge / discharge` actions with a reward that rewards low grid draw and penalizes over-charge / depletion.
2. **Forecasting** — a scikit-learn model estimates next-hour demand as an input signal.
3. **Agent** — a TensorFlow DQN learns a charge/discharge policy over repeated episodes (one episode = one simulated day, 96 fifteen-minute steps).
4. **Evaluation** — notebooks chart training reward and compare grid draw *with* the agent against a no-control baseline.

## Simulated results

Measured in simulation against a no-control baseline — **not on production hardware**:

| Metric | Result |
|---|---|
| Peak grid draw | **−30%** |
| Precharge detection | **+92%** |
| Battery utilization | **+18%** |
| Energy waste | **−25%** |

## Designed, not built

The deployment architecture was designed but deliberately left out of scope for this academic build, and is **not** in this repository:

> Terraform-provisioned AWS (IoT Core for device streams, Lambda for the control loop), with Grafana + InfluxDB for live telemetry and multi-home edge coordination.

Calling that out keeps the scope honest: this repo contains the simulation, models, and analysis — not the cloud stack.

## Getting started

```bash
git clone https://github.com/andre-rowe/Project-Volta.git
cd Project-Volta

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook   # then open notebooks/train_dqn.ipynb
```

---

<sub>Built by <a href="https://github.com/andre-rowe">Andre Rowe</a> · part of my <a href="https://andrerowe.com">portfolio</a>.</sub>
