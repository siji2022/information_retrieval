import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors

from shapely.geometry import box
from shapely.plotting import plot_polygon, plot_points

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors

from shapely.geometry import box
from shapely.plotting import plot_polygon, plot_points

import geopandas as gpd

from shapely import STRtree,buffer

import warnings
warnings.simplefilter(action='ignore', category=Warning)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import OneHotEncoder

import pointpats
from shapely import Point

#seting up palette 
palette = ["#FAC8BE", "#80E1C6", "#FFB3E1", "#6CC3FC", "#FFD168", "#C894E1"]
sns.set(rc={"axes.facecolor":"#e6e6e6","figure.facecolor":"#f5f5f5"})
cmap = colors.ListedColormap( ["#FAC8BE", "#80E1C6", "#FFB3E1", "#6CC3FC", "#FFD168", "#C894E1"])


st.title('Crime in D.C.')

# load data
df = pd.read_csv('../data/crime_dc.csv')
# fill missing value: start_date filled by report_date if missing
df['start_date'] = df['start_date'].fillna(df['report_date'])
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# df=df[df['start_date'].dt.year>2022]
df.index=pd.RangeIndex(start=0,stop=df.shape[0])
df['day_of_week'] = df['start_date'].dt.dayofweek
df['hour'] = df['start_date'].dt.hour
# make crime_data a geopanda frame
df['geometry'] = gpd.points_from_xy(df['longitude'], df['latitude'])
crime_data = gpd.GeoDataFrame(df, crs="EPSG:4326")

tree=STRtree(crime_data['geometry'])
#DC MAP
# dc_boundary = gpd.read_file('../data/dc-maps/maps/dc-boundary.geojson')
# polygon=dc_boundary['geometry'][0]

# random_location=pointpats.random.poisson(polygon, size=1)


# dc_boundary.plot()

# plt.scatter(random_location[0],random_location[1],marker='o',s=15,c='r')


## start construct page
# input location lat and long
st.text("Please enter a location in D.C. to search for crime events.")
lat = st.number_input('Enter a latitude', value=38.9140,step=0.001,format="%.4f")
long = st.number_input('Enter a longitude', value=-77.0290,step=0.001,format="%.4f")

# radius selection
radius = st.slider('Select a radius for the search (miles)', 0.1, 3.0, 0.1,0.05)
radius_degree=radius/69.0
print(f'radius_degree: {radius_degree}')
events=tree.query(Point(long,lat),predicate='dwithin',distance=radius_degree).tolist()
history_crime_events=crime_data.iloc[events]

worst_hours=history_crime_events['hour'].value_counts().sort_values(ascending=False).index[0]
worst_days=history_crime_events['day_of_week'].value_counts().sort_values(ascending=False).index[0]
dict_day_of_week={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

# first section: highlight the selected location and background of DC all crimes
st.write(f"For the selected location, lat =  {lat:.4f},  long =  {long:.4f}, shows as blue start in the map below. ")
st.write(f"Worst day of the week is {dict_day_of_week[worst_days]}, and worst hour is {worst_hours}.")
st.write(f"Total crime events in the selected location: {len(events)}")


ax = sns.jointplot(x=df['longitude'], y=df['latitude'], kind='hex', gridsize=30, 
                color=palette[0],marginal_ticks=False, ratio=90
                )
ax.ax_marg_y.set_yticks(np.linspace(min(df['latitude']), max(df['latitude']), 6))  
ax.ax_marg_x.set_xticks(np.linspace(min(df['longitude']), max(df['longitude']), 6))  

# fig,ax=plt.subplots()
sns.scatterplot(x=[long],y=[lat],marker='*',s=130,c='b')
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

# second section: show the crime events by offense type
fig, ax=plt.subplots()
plt.pie(history_crime_events['offense'].value_counts().values,labels=history_crime_events['offense'].value_counts().index,autopct='%.0f%%')
plt.title('Offense type')
st.pyplot(fig)
plt.close()

# third section: show the crime events by hour
fig, ax=plt.subplots()
plt.pie(history_crime_events['hour'].value_counts().sort_index().values,labels=history_crime_events['hour'].value_counts().sort_index().index,autopct='%.0f%%')
plt.title('Incident happened by hour')
st.pyplot(fig)
plt.close()

# fourth section: show the crime events by hour
fig, ax=plt.subplots()
plt.pie(history_crime_events['day_of_week'].value_counts().sort_index().values,labels= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],autopct='%.0f%%')
plt.title('Incident days of week')
st.pyplot(fig)
plt.close()



# loop through the crime events
st.write('details of the crime events:')
for i in history_crime_events.index:
    st.write(f"Crime event: {history_crime_events.loc[i,'offense']} at {history_crime_events.loc[i,'start_date']}")