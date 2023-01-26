import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Read the stops.txt file into a DataFrame
stops_df = pd.read_csv("stops.txt")

# Convert the stop_lat and stop_lon columns to a Shapely Point object
stops_df["geometry"] = stops_df.apply(lambda x: Point(x.stop_lon, x.stop_lat), axis=1)

# Convert the DataFrame to a GeoDataFrame
stops_gdf = gpd.GeoDataFrame(stops_df, geometry="geometry")

# Write the GeoDataFrame to a GeoJSON file
stops_gdf.to_file("stops.geojson", driver="GeoJSON")
