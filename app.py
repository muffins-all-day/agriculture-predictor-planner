import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(layout="wide")

#Code for data loading
@st.cache_data
def load_top5(path="data/final/top5crops_per_district.csv"):
    #This file has top five crops per district
    df = pd.read_csv(path)
    return df

@st.cache_data
def load_main(path="data/final/crop_produce_data.csv"):
    # this file has your year‑wise yields, weather columns, etc.
    df = pd.read_csv(path)
    return df

# Load the dataframe once
df_main = load_main()
df_top_five = load_top5()


#Display the sidebar
st.sidebar.header("Crop Predictor Inputs")
selected_state = st.sidebar.selectbox("Select State",sorted(df_main['State Name'].unique()))
selected_district = st.sidebar.selectbox("Select District", sorted(df_main[df_main['State Name'] == selected_state]['Dist Name'].unique()))

# Optional: add additional sliders/inputs for scenario simulation
weather_adjustment = st.sidebar.slider("Adjust Temperature (°C)", -5, 5, 0)



#Main Panel Display
st.title("Crop Predictor Dashboard")
st.subheader("Current Inputs")
st.write("District:", selected_district)
st.write("Weather Adjustment:", weather_adjustment, "°C")


#_______Part 1 - Displaying the top five crops____________
def main():
  if selected_district:
        #Filtering the data for the selected district
        top5 = (df_top_five[df_top_five["Dist Name"] == selected_district]
                .sort_values("Yield", ascending=False)
                .reset_index(drop=True))

        # shift index to start at 1 instead of 0
        top5.index = top5.index + 1

        # rename the columns for user's clarity
        top5 = top5.rename(columns={
        "Crop": "Top Five Crops",
        "Yield": "Average Yield (kg/ha)"})

        #display the top five crops
        st.subheader(f"Top 5 crops in {selected_district}")
        st.dataframe(top5[["Top Five Crops","Average Yield (kg/ha)"]], use_container_width=True)

        #call the function for displaying the historical trends
        show_trends(top5['Top Five Crops'].tolist())


#_________Part 2 - Interactive Historical trends visualisation_____
def show_trends(df_top5):
    
    #Filter the crop produce dataset
    df_d = df_main[df_main["Dist Name"] == selected_district]

    # build the list of yield‑column names
    yield_cols = [f"{crop} YIELD (Kg per ha)" for crop in df_top5]

    #melt to long format
    df_trends = df_d[["Year"] + yield_cols].melt(
        id_vars="Year",
        value_vars=yield_cols,
        var_name="Crop",
        value_name="Yield")

    #clean up the Crop names (strip off the suffix)
    df_trends["Crop"] = df_trends["Crop"].str.replace(
       r"\s*YIELD*\s*\(Kg\sper\sha\)", "", regex=True)


    # plot with Plotly for hover + legend interactivity
    fig = px.line(
        df_trends,
        x="Year",
        y="Yield",
        color="Crop",
        markers=True,
        title=f"25‑Year Yield Trends for Top 5 Crops in {selected_district}")

    fig.update_layout(legend_title_text="Crop",
    height=600,      
    width=1400,       
    margin=dict(l=40, r=40, t=80, b=40))

    #display in Streamlit
    st.plotly_chart(fig, use_container_width=False)



if __name__ == "__main__":
    main()


