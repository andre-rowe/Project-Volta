import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
homes = 10
hours = 24 * 7  # 1 week
start_time = datetime.now().replace(minute=0, second=0, microsecond=0)

# Simulate hourly data
data = []

for home_id in range(1, homes + 1):
    battery_pct = np.random.randint(20, 80)
    for hour in range(hours):
        timestamp = start_time + timedelta(hours=hour)
        hour_of_day = timestamp.hour

        # Simulate solar production (0 at night, peak at noon ~8kW)
        solar = max(0, np.sin((hour_of_day - 6) / 12 * np.pi)
                    * 8 + np.random.normal(0, 0.5))

        # Simulate demand (low overnight, peaks 6-9am & 6-10pm)
        if 6 <= hour_of_day <= 9 or 18 <= hour_of_day <= 22:
            demand = np.random.uniform(3, 6)
        elif 10 <= hour_of_day <= 16:
            demand = np.random.uniform(1, 3)
        else:
            demand = np.random.uniform(0.3, 2)

        # Battery discharges to cover demand if needed
        battery_kwh = battery_pct / 100 * 13.5  # Assume 13.5kWh Powerwall
        used_from_battery = min(battery_kwh, demand - solar)
        used_from_battery = max(0, used_from_battery)
        battery_kwh -= used_from_battery
        battery_pct = battery_kwh / 13.5 * 100

        # Solar covers part of demand
        remaining_demand = demand - solar - used_from_battery
        grid_draw = max(0, remaining_demand)

        data.append({
            "home_id": home_id,
            "timestamp": timestamp,
            "solar_generation_kw": round(solar, 2),
            "battery_level_pct": round(battery_pct, 2),
            "grid_demand_kw": round(demand, 2),
            "grid_draw_kw": round(grid_draw, 2)
        })

# Convert to DataFrame
df = pd.DataFrame(data)
df.to_csv("volta_simulated_data.csv", index=False)

print("✅ Simulated data saved to volta_simulated_data.csv")
