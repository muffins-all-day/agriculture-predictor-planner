import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Step 2: Load Data ---
# Replace with your actual data loading code.
@st.cache_data
def load_data():
    # Replace with your actual data loading code
    df = pd.read_csv('data/merged/crop_soil_weather_merged.csv')
    return df

# Load the dataframe once
df = load_data()
# --- Step 3: Sidebar for User Input ---
st.sidebar.header("Crop Predictor Inputs")
selected_state = st.sidebar.selectbox("Select State",df['State Name'].unique())
selected_district = st.sidebar.selectbox("Select District", df[df['State Name'] == selected_state]['Dist Name'].unique())
selected_month = st.sidebar.selectbox("Select Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Optional: add additional sliders/inputs for scenario simulation
weather_adjustment = st.sidebar.slider("Adjust Temperature (°C)", -5, 5, 0)

# --- Step 4: Filter Data Based on Inputs ---
#filtered_df = df[(df['Dist Name'] == selected_district) & (df['Month'] == selected_month)]

# Simulated crop recommendations based on a simple ranking of yields
# In a real scenario, you'll plug in your model predictions here.
if not filtered_df.empty:
    rice_yield = filtered_df['RICE YIELD (Kg per ha)'].mean() + weather_adjustment
    wheat_yield = filtered_df['WHEAT YIELD (Kg per ha)'].mean() + weather_adjustment
    recommendations = {
        'RICE': rice_yield,
        'WHEAT': wheat_yield,
        # You can add more crops and simulated scores here.
    }
    # Sort crops based on yield (higher is better)
    sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
else:
    sorted_recs = []

# --- Step 5: Main Panel Display ---
st.title("Crop Predictor Dashboard")

st.subheader("Current Inputs")
st.write("District:", selected_district)
st.write("Month:", selected_month)
st.write("Weather Adjustment:", weather_adjustment, "°C")

st.subheader("Top Crop Recommendations")
if sorted_recs:
    for idx, (crop, score) in enumerate(sorted_recs, start=1):
        st.write(f"{idx}. {crop} - Predicted Yield: {score:.0f} Kg per ha")
else:
    st.write("No data available for the selected inputs.")

# --- Step 5: Visualizations ---
st.subheader("Historical Yield Trend (Simulated)")

# Create a sample plot for demonstration
fig, ax = plt.subplots(figsize=(6, 4))


# Simulated historical yield data
months = ['January', 'February', 'March', 'April', 'May', 'June']
rice_yields = np.random.randint(2800, 3500, size=len(months))
ax.plot(months, rice_yields, marker='o', label='Rice Yield')
ax.set_title("Historical Rice Yield Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Yield (Kg per ha)")
ax.legend()

st.pyplot(fig)
