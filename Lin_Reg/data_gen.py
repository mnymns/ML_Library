import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Parameters for the linear relationship
n_samples = 100  # Number of samples
slope = 2.5      # True slope of the line
intercept = 5    # True intercept
noise_std = 3    # Standard deviation of the noise

# Generate independent variable (x)
x = np.random.uniform(0, 20, n_samples)  # Random values between 0 and 20

# Generate dependent variable (y) with added noise
noise = np.random.normal(0, noise_std, n_samples)  # Gaussian noise
y = slope * x + intercept + noise

# Combine into a DataFrame for convenience
data = pd.DataFrame({'x': x, 'y': y})

# Save to a CSV (optional)
data.to_csv('sample_data.csv', index=False)