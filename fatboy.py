import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# Read the stops.txt file into a DataFrame
stops_df = pd.read_csv("stops.txt")

# Read the stop_times.txt file into a DataFrame
stop_times_df = pd.read_csv("stop_times.txt")

# Merge the stops and stop_times DataFrames on the stop_id column
merged_df = pd.merge(stops_df, stop_times_df, on="stop_id")

# Read the trips.txt file into a DataFrame
trips_df = pd.read_csv("trips.txt")

# Merge the merged_df and trips_df DataFrames on the trip_id column
merged_df = pd.merge(merged_df, trips_df, on="trip_id")

# Convert the stop_lat and stop_lon columns to a Shapely Point object
merged_df["geometry"] = merged_df.apply(lambda x: Point(x.stop_lon, x.stop_lat), axis=1)

# Convert the DataFrame to a GeoDataFrame
stops_gdf = gpd.GeoDataFrame(merged_df, geometry="geometry")

# Create a new 'routes' column in the GeoDataFrame, which contains a list of routes that stop at each stop
stops_gdf['routes'] = stops_gdf.groupby('stop_id')['route_id'].apply(list)

# Create a new 'times' column in the GeoDataFrame, which contains a list of times that stop at each stop
stops_gdf['times'] = stops_gdf.groupby('stop_id')['arrival_time'].apply(list)

# Write the GeoDataFrame to a GeoJSON file
stops_gdf.to_file("stops.geojson", driver="GeoJSON", columns=["stop_id", "stop_name", "routes","times", "geometry"])
