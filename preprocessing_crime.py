# create crime data for model

import numpy as np
import pandas as pd
import os

jan_crimes=pd.read_csv('./jan_crimes.csv', index_col=0)
print(jan_crimes.head(5))
sel_columns=['PCA_location','ward','psa','day_of_week', 'hour', 'museums_count', 'gas',
       'metro_bus', 'atm', 'banks', 'grocery', 'metro_stations', 'post_office',
       'schools', 'libraries', 'shuttle_bus']
# make a time series of crimes
# get the number of crimes per day
jan_crimes['start_date']=pd.to_datetime(jan_crimes['start_date'])
jan_crimes['date']=jan_crimes['start_date'].dt.normalize() # keep only date
ts=jan_crimes.groupby(['date','index']).size()
ts.plot(style='.')