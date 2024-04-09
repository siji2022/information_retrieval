import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors

from shapely.geometry import box
from shapely.plotting import plot_polygon, plot_points


st.title('Crime alert in D.C.')

# load data
all_crime_2023 = pd.read_csv('../data/crime_dc.csv')
# fill missing value: start_date filled by report_date if missing
all_crime_2023['start_date'] = all_crime_2023['start_date'].fillna(all_crime_2023['report_date'])
#seting up palette 
palette = ["#FAC8BE", "#80E1C6", "#FFB3E1", "#6CC3FC", "#FFD168", "#C894E1"]
sns.set(rc={"axes.facecolor":"#e6e6e6","figure.facecolor":"#f5f5f5"})
cmap = colors.ListedColormap( ["#FAC8BE", "#80E1C6", "#FFB3E1", "#6CC3FC", "#FFD168", "#C894E1"])


query_dt=st.date_input("Pick a date you want to know about crime in D.C.", value=None, min_value=pd.to_datetime('2023-01-01'), max_value=pd.to_datetime('2023-12-31'))
offense_types=all_crime_2023['offense'].value_counts().index
# add all option
offense_types = ['All'] + list(offense_types)
selected_offense_type = st.selectbox('Which type of crimes you want to see?',offense_types)
if query_dt is not None:
    st.write("The map below shows the crime incidents in D.C. on", query_dt,selected_offense_type)
    # filter data date date
    all_crime_2023['start_date'] = pd.to_datetime(all_crime_2023['start_date'])
    df = all_crime_2023[all_crime_2023['start_date'].dt.date == query_dt]
    # filter by offense type
    if selected_offense_type != 'All':
        df = df[df['offense'] == selected_offense_type]

    if df.shape[0] == 0:
        st.write("No crime incident on selected date. Only crime incidents in 2023 are available. Crime incidents after October 2023 are not completely reported.")
    else:
        ax = sns.jointplot(x=df['longitude'], y=df['latitude'], kind='hex', gridsize=20, 
                        color=palette[0]
                        )
        ax.ax_marg_y.set_yticks(np.linspace(min(df['latitude']), max(df['latitude']), 6))  
        ax.ax_marg_x.set_xticks(np.linspace(min(df['longitude']), max(df['longitude']), 6))  
        # plt.tight_layout()
        # plt.title("Crimes based on Latitude and Longitude")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.yticks(rotation=45)
        plt.xticks(rotation=45)
        # fig, ax1=plt.subplots()
        # ax1.plot(df['first column'])
        st.pyplot(ax)
        plt.close()