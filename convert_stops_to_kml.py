import simplekml
import pandas as pd

stops_df = pd.read_csv("stops.txt")

kml = simplekml.Kml()

for i, stop in stops_df.iterrows():
    pnt = kml.newpoint(name=stop["stop_name"], coords=[(stop["stop_lon"], stop["stop_lat"])])

kml.save("stops.kml")
