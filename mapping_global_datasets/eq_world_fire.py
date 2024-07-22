from pathlib import Path
import csv

import plotly.express as px

path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract data

lats, lons, bris = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bri = float(row[2])
    lats.append(lat)
    lons.append(lon)
    bris.append(bri)

title = 'World Fires'

fig = px.scatter_geo(lat=lats, lon=lons, title=title, color=bris,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth')

fig.show()