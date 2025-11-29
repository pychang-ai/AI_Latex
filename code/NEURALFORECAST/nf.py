# NeuralForecast Tutorial - Time Series Forecasting with Neural Networks

# Install the package first:
# pip install neuralforecast

import pandas as pd
import numpy as np
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS, NHITS
from neuralforecast.utils import AirPassengersDF

# 1. Load sample data
# NeuralForecast expects data with columns: unique_id, ds (datetime), y (target)
df = AirPassengersDF

print("Sample data:")
print(df.head())
# unique_id | ds         | y
# 1         | 1949-01-01 | 112
# 1         | 1949-02-01 | 118
# ...

# 2. Define forecasting models
horizon = 12  # Forecast next 12 periods

models = [
    NBEATS(input_size=24, h=horizon, max_steps=100),
    NHITS(input_size=24, h=horizon, max_steps=100)
]

# 3. Initialize NeuralForecast
nf = NeuralForecast(models=models, freq='M')

# 4. Train the models
nf.fit(df=df)

# 5. Generate forecasts
forecasts = nf.predict()

print("\nForecasts:")
print(forecasts.head())
# Contains columns: unique_id, ds, NBEATS, NHITS

# 6. Plot results (optional)
# from neuralforecast.losses.numpy import mae
# from neuralforecast.utils import AirPassengersPanel
# nf.plot(df=AirPassengersPanel, forecasts_df=forecasts)

# Simple example with custom data:
custom_df = pd.DataFrame({
    'unique_id': [1] * 100,
    'ds': pd.date_range('2020-01-01', periods=100, freq='D'),
    'y': np.random.randn(100).cumsum() + 100
})

# Train and predict
nf_custom = NeuralForecast(
    models=[NBEATS(input_size=30, h=7, max_steps=50)],
    freq='D'
)
nf_custom.fit(df=custom_df)
predictions = nf_custom.predict()

print("\nCustom predictions:")
print(predictions)