import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Configuration for real-time sensor data: 60 days, every 30 minutes
START_DATE = datetime(2025, 6, 1, 0, 0, 0)
DURATION_DAYS = 60
MEASUREMENT_INTERVAL_MINUTES = 30
NUM_DATA_POINTS = int((DURATION_DAYS * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)

# Water quality parameters based on SANS 241:2015
PH_MEAN = 7.5
PH_STD_DEV = 0.3
PH_MIN = 4.0
PH_MAX = 10.0

TURBIDITY_NORMAL_MEAN = 0.8
TURBIDITY_NORMAL_STD_DEV = 0.2
TURBIDITY_MIN = 0.1
TURBIDITY_MAX = 100.0

TDS_MEAN = 500.0
TDS_STD_DEV = 100.0
TDS_MIN = 50.0
TDS_MAX = 2500.0

CONDUCTIVITY_NORMAL_MEAN = 100.0
CONDUCTIVITY_STD_DEV = 15.0
CONDUCTIVITY_MIN = 10.0
CONDUCTIVITY_MAX = 400.0

COLOUR_NORMAL_MEAN = 10.0
COLOUR_STD_DEV = 3.0
COLOUR_MIN = 0.0
COLOUR_MAX = 70.0

CHLORINE_NORMAL_MEAN = 0.5
CHLORINE_STD_DEV = 0.1
CHLORINE_MIN = 0.0
CHLORINE_MAX = 1.0

NITRATE_NORMAL_MEAN = 2.0
NITRATE_STD_DEV = 0.5
NITRATE_MIN = 0.0
NITRATE_MAX = 15.0

AMMONIA_NORMAL_MEAN = 0.1
AMMONIA_STD_DEV = 0.05
AMMONIA_MIN = 0.0
AMMONIA_MAX = 2.0

TOC_NORMAL_MEAN = 3.0
TOC_STD_DEV = 0.5
TOC_MIN = 0.0
TOC_MAX = 20.0

# Anomaly events to simulate real-world issues
ANOMALY_TURBIDITY_START_DAY = 15
ANOMALY_TURBIDITY_DURATION_HOURS = 24
ANOMALY_TURBIDITY_SPIKE_VALUE = 70.0

ANOMALY_PH_START_DAY = 45
ANOMALY_PH_DURATION_HOURS = 6
ANOMALY_PH_HIGH_VALUE = 9.8
ANOMALY_PH_LOW_VALUE = 4.5
ANOMALY_PH_SEVERITY_AMPLITUDE = 1.0

ANOMALY_TDS_CONDUCTIVITY_START_DAY = 25
ANOMALY_TDS_CONDUCTIVITY_DURATION_HOURS = 36
ANOMALY_TDS_SPIKE_VALUE = 2800.0
ANOMALY_CONDUCTIVITY_SPIKE_VALUE = 380.0

ANOMALY_COLOUR_START_DAY = 50
ANOMALY_COLOUR_DURATION_HOURS = 12
ANOMALY_COLOUR_SPIKE_VALUE = 60.0

ANOMALY_CHLORINE_START_DAY = 20
ANOMALY_CHLORINE_DURATION_HOURS = 10
ANOMALY_CHLORINE_DROP_VALUE = 0.05

ANOMALY_NITRATE_START_DAY = 40
ANOMALY_NITRATE_DURATION_HOURS = 18
ANOMALY_NITRATE_SPIKE_VALUE = 13.0

ANOMALY_AMMONIA_START_DAY = 30
ANOMALY_AMMONIA_DURATION_HOURS = 8
ANOMALY_AMMONIA_SPIKE_VALUE = 1.8

ANOMALY_TOC_START_DAY = 10
ANOMALY_TOC_DURATION_HOURS = 20
ANOMALY_TOC_SPIKE_VALUE = 15.0

# Generate timestamps
timestamps = [START_DATE + timedelta(minutes=i * MEASUREMENT_INTERVAL_MINUTES)
              for i in range(NUM_DATA_POINTS)]
time_in_hours = np.array([(t - START_DATE).total_seconds() / 3600 for t in timestamps])

# Generate synthetic data with normal fluctuations
ph_data = np.zeros(NUM_DATA_POINTS)
turbidity_data = np.zeros(NUM_DATA_POINTS)
tds_data = np.zeros(NUM_DATA_POINTS)
conductivity_data = np.zeros(NUM_DATA_POINTS)
colour_data = np.zeros(NUM_DATA_POINTS)
chlorine_data = np.zeros(NUM_DATA_POINTS)
nitrate_data = np.zeros(NUM_DATA_POINTS)
ammonia_data = np.zeros(NUM_DATA_POINTS)
toc_data = np.zeros(NUM_DATA_POINTS)

for i in range(NUM_DATA_POINTS):
    ph_data[i] = np.random.normal(PH_MEAN, PH_STD_DEV)
    turbidity_data[i] = np.random.normal(TURBIDITY_NORMAL_MEAN, TURBIDITY_NORMAL_STD_DEV)
    tds_data[i] = np.random.normal(TDS_MEAN, TDS_STD_DEV)
    conductivity_data[i] = np.random.normal(CONDUCTIVITY_NORMAL_MEAN, CONDUCTIVITY_STD_DEV)
    colour_data[i] = np.random.normal(COLOUR_NORMAL_MEAN, COLOUR_STD_DEV)
    chlorine_data[i] = np.random.normal(CHLORINE_NORMAL_MEAN, CHLORINE_STD_DEV)
    nitrate_data[i] = np.random.normal(NITRATE_NORMAL_MEAN, NITRATE_STD_DEV)
    ammonia_data[i] = np.random.normal(AMMONIA_NORMAL_MEAN, AMMONIA_STD_DEV)
    toc_data[i] = np.random.normal(TOC_NORMAL_MEAN, TOC_STD_DEV)

# Inject anomalies
# Turbidity spike (e.g., heavy rainfall)
anomaly_turb_start_idx = int((ANOMALY_TURBIDITY_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_turb_end_idx = min(anomaly_turb_start_idx + int((ANOMALY_TURBIDITY_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_turb_start_idx < NUM_DATA_POINTS:
    turb_spike_indices = np.arange(anomaly_turb_start_idx, anomaly_turb_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(turb_spike_indices)))
    turbidity_data[turb_spike_indices] = ANOMALY_TURBIDITY_SPIKE_VALUE * spike_profile + np.random.normal(0, 5, len(turb_spike_indices))

# pH fluctuation (e.g., chemical spill)
anomaly_ph_start_idx = int((ANOMALY_PH_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_ph_end_idx = min(anomaly_ph_start_idx + int((ANOMALY_PH_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_ph_start_idx < NUM_DATA_POINTS:
    ph_fluct_indices = np.arange(anomaly_ph_start_idx, anomaly_ph_end_idx)
    ph_oscillation = ANOMALY_PH_SEVERITY_AMPLITUDE * np.sin(2 * np.pi * np.linspace(0, 2, len(ph_fluct_indices)))
    for j, idx in enumerate(ph_fluct_indices):
        ph_data[idx] = (ANOMALY_PH_HIGH_VALUE if j % 2 == 0 else ANOMALY_PH_LOW_VALUE) + ph_oscillation[j] * 0.5 + np.random.normal(0, 0.1)

# TDS & Conductivity spike (e.g., saline intrusion)
anomaly_tds_cond_start_idx = int((ANOMALY_TDS_CONDUCTIVITY_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_tds_cond_end_idx = min(anomaly_tds_cond_start_idx + int((ANOMALY_TDS_CONDUCTIVITY_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_tds_cond_start_idx < NUM_DATA_POINTS:
    tds_cond_spike_indices = np.arange(anomaly_tds_cond_start_idx, anomaly_tds_cond_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(tds_cond_spike_indices)))
    tds_data[tds_cond_spike_indices] = ANOMALY_TDS_SPIKE_VALUE * spike_profile + np.random.normal(0, 50, len(tds_cond_spike_indices))
    conductivity_data[tds_cond_spike_indices] = ANOMALY_CONDUCTIVITY_SPIKE_VALUE * spike_profile + np.random.normal(0, 10, len(tds_cond_spike_indices))

# Colour spike (e.g., algal bloom)
anomaly_colour_start_idx = int((ANOMALY_COLOUR_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_colour_end_idx = min(anomaly_colour_start_idx + int((ANOMALY_COLOUR_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_colour_start_idx < NUM_DATA_POINTS:
    colour_spike_indices = np.arange(anomaly_colour_start_idx, anomaly_colour_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(colour_spike_indices)))
    colour_data[colour_spike_indices] = ANOMALY_COLOUR_SPIKE_VALUE * spike_profile + np.random.normal(0, 5, len(colour_spike_indices))

# Free Chlorine drop (e.g., disinfection failure)
anomaly_chlorine_start_idx = int((ANOMALY_CHLORINE_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_chlorine_end_idx = min(anomaly_chlorine_start_idx + int((ANOMALY_CHLORINE_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_chlorine_start_idx < NUM_DATA_POINTS:
    chlorine_drop_indices = np.arange(anomaly_chlorine_start_idx, anomaly_chlorine_end_idx)
    drop_profile = 1 - np.sin(np.linspace(0, np.pi, len(chlorine_drop_indices)))
    chlorine_data[chlorine_drop_indices] = ANOMALY_CHLORINE_DROP_VALUE + (CHLORINE_NORMAL_MEAN - ANOMALY_CHLORINE_DROP_VALUE) * drop_profile + np.random.normal(0, 0.05, len(chlorine_drop_indices))

# Nitrate spike (e.g., agricultural runoff)
anomaly_nitrate_start_idx = int((ANOMALY_NITRATE_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_nitrate_end_idx = min(anomaly_nitrate_start_idx + int((ANOMALY_NITRATE_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_nitrate_start_idx < NUM_DATA_POINTS:
    nitrate_spike_indices = np.arange(anomaly_nitrate_start_idx, anomaly_nitrate_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(nitrate_spike_indices)))
    nitrate_data[nitrate_spike_indices] = ANOMALY_NITRATE_SPIKE_VALUE * spike_profile + np.random.normal(0, 0.5, len(nitrate_spike_indices))

# Ammonia spike (e.g., sewage ingress)
anomaly_ammonia_start_idx = int((ANOMALY_AMMONIA_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_ammonia_end_idx = min(anomaly_ammonia_start_idx + int((ANOMALY_AMMONIA_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_ammonia_start_idx < NUM_DATA_POINTS:
    ammonia_spike_indices = np.arange(anomaly_ammonia_start_idx, anomaly_ammonia_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(ammonia_spike_indices)))
    ammonia_data[ammonia_spike_indices] = ANOMALY_AMMONIA_SPIKE_VALUE * spike_profile + np.random.normal(0, 0.1, len(ammonia_spike_indices))

# TOC spike (e.g., organic pollution)
anomaly_toc_start_idx = int((ANOMALY_TOC_START_DAY * 24 * 60) / MEASUREMENT_INTERVAL_MINUTES)
anomaly_toc_end_idx = min(anomaly_toc_start_idx + int((ANOMALY_TOC_DURATION_HOURS * 60) / MEASUREMENT_INTERVAL_MINUTES), NUM_DATA_POINTS)
if anomaly_toc_start_idx < NUM_DATA_POINTS:
    toc_spike_indices = np.arange(anomaly_toc_start_idx, anomaly_toc_end_idx)
    spike_profile = np.sin(np.linspace(0, np.pi, len(toc_spike_indices)))
    toc_data[toc_spike_indices] = ANOMALY_TOC_SPIKE_VALUE * spike_profile + np.random.normal(0, 1.0, len(toc_spike_indices))

# Clip data to ensure realistic bounds
ph_data = np.clip(ph_data, PH_MIN, PH_MAX)
turbidity_data = np.clip(turbidity_data, TURBIDITY_MIN, TURBIDITY_MAX)
tds_data = np.clip(tds_data, TDS_MIN, TDS_MAX)
conductivity_data = np.clip(conductivity_data, CONDUCTIVITY_MIN, CONDUCTIVITY_MAX)
colour_data = np.clip(colour_data, COLOUR_MIN, COLOUR_MAX)
chlorine_data = np.clip(chlorine_data, CHLORINE_MIN, CHLORINE_MAX)
nitrate_data = np.clip(nitrate_data, NITRATE_MIN, NITRATE_MAX)
ammonia_data = np.clip(ammonia_data, AMMONIA_MIN, AMMONIA_MAX)
toc_data = np.clip(toc_data, TOC_MIN, TOC_MAX)

# Create DataFrame and save to CSV
data = {
    'timestamp': timestamps,
    'pH': ph_data,
    'turbidity_NTU': turbidity_data,
    'tds_mg_L': tds_data,
    'conductivity_mS_m': conductivity_data,
    'colour_Pt_Co': colour_data,
    'free_chlorine_mg_L': chlorine_data,
    'nitrate_mg_L': nitrate_data,
    'ammonia_mg_L': ammonia_data,
    'toc_mg_L': toc_data
}

df = pd.DataFrame(data)
output_filename = '/Users/alhena/Downloads/Virtual_Intern_Water/real_time_simulated_sensor_data_SANS_adapted_v3.csv'
df.to_csv(output_filename, index=False)

# Print confirmation and data preview
print(f"Real-time synthetic sensor data (SANS-adapted v3) saved to {output_filename}")
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print(f"\nTotal data points generated: {len(df)}")