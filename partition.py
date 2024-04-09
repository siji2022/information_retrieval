# partition geopandas file
import geopandas as gpd
import pandas as pd
import numpy as np
import seaborn as sns
from shapely.geometry import box

# read the shape file
dc_boundary = gpd.read_file('./data/dc-maps/maps/dc-boundary.geojson')
crime_data=pd.read_csv('./data/crime_dc.csv')
libraries = gpd.read_file('./data/dc-maps/maps/libraries.geojson')
polygon=dc_boundary['geometry'][0]
# segment the polygon into 10 parts
n=10
def fishnet(geometry, step=0.01):
    bounds = geometry.bounds
    xmin,ymin,xmax,ymax=bounds
    result = []
    for i in np.arange(xmin, xmax, step):
        for j in np.arange(ymin, ymax, step):
            b = box(i, j, i+step, j+step)
            g = geometry.intersection(b)
            if g.is_empty:
                continue
            result.append(g)
    return result
res=fishnet(polygon, 0.01)
nets=gpd.GeoDataFrame(geometry=res)
# merge libraries into nets
nets.sjoin(libraries, how='left', op='within')

# save plot tight layout
plt.savefig('./data/fishnet.png',dpi=300,bbox_inches='tight')



