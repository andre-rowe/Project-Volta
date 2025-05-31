import numpy as np


class BatteryEnv:
    def __init__(self):
        self.max_battery_kwh = 13.5
        self.reset()

    def reset(self):
        self.battery_kwh = np.random.uniform(
            3.0, 10.0)  # start with partial battery
        self.solar_kw = np.random.uniform(0.0, 8.0)
        self.forecast_kw = np.random.uniform(1.0, 6.0)
        self.time_step = 0
        return self._get_state()

    def _get_state(self):
        battery_pct = self.battery_kwh / self.max_battery_kwh * 100
        return np.array([battery_pct, self.solar_kw, self.forecast_kw], dtype=np.float32)

    def step(self, action):
        grid_draw = 0
        reward = 0
        done = False

        # Action: 0=hold, 1=charge, 2=discharge
        if action == 1:  # charge
            charge_kw = min(self.solar_kw, 3.0)  # limit charging rate
            self.battery_kwh += charge_kw * 0.25  # 15 minutes worth
            reward -= 0.1  # slight penalty to avoid overcharging
        elif action == 2:  # discharge
            needed_kw = max(0, self.forecast_kw - self.solar_kw)
            discharge_kw = min(needed_kw, self.battery_kwh, 3.0)
            self.battery_kwh -= discharge_kw * 0.25
            grid_draw = max(0, needed_kw - discharge_kw)
        else:
            # hold = rely on solar and grid
            grid_draw = max(0, self.forecast_kw - self.solar_kw)

        # Reward = encourage low grid draw
        reward += (1.0 - (grid_draw / max(self.forecast_kw, 0.01))) * 10

        # Battery overflow or depletion penalties
        if self.battery_kwh > self.max_battery_kwh:
            reward -= 5
            self.battery_kwh = self.max_battery_kwh
        if self.battery_kwh < 0:
            reward -= 10
            self.battery_kwh = 0

        self.time_step += 1
        if self.time_step >= 96:  # simulate 1 day (15-min steps)
            done = True

        # New solar and demand for next step
        self.solar_kw = np.random.uniform(0.0, 8.0)
        self.forecast_kw = np.random.uniform(1.0, 6.0)

        return self._get_state(), reward, done, {}
