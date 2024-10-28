import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the Excel file
file_path = 'dataset.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Extract columns
chemical_shifts = df['Chemical Shift (ppm)'].values
your_data = df['50-50'].values
Q1 = df['Q1(sodium pyrophosphate)'].values
Q2 = df['Q2 (LiPO3)'].values

# Step 1: Normalize each dataset
def normalize(data):
    return (data / np.max(data)) * 100

your_data_norm = normalize(your_data)
Q1_norm = normalize(Q1)
Q2_norm = normalize(Q2)

# Step 2: Try different ratios of Q1 and Q2 and combine them
ratios = np.linspace(0, 1, 11)  # Ratios from 0:1 to 1:0 with increments of 0.1

# Plot your data
plt.plot(chemical_shifts, your_data_norm, label='Your Data', marker='o', color='blue')

# Plot combined Q1 + Q2 for different ratios
for ratio in ratios:
    combined_data = ratio * Q1_norm + (1 - ratio) * Q2_norm
    combined_data_norm = normalize(combined_data)
    plt.plot(chemical_shifts, combined_data_norm, label=f'Q1:{ratio:.1f} | Q2:{1 - ratio:.1f}', linestyle='--')

# Customize the plot
plt.xlabel('Chemical Shift')
plt.ylabel('Normalized Intensity')
plt.title('Comparison of Your Data and Q1 + Q2 Combinations')
plt.legend(loc='best')
plt.grid(True)
plt.show()
