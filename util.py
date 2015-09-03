import pandas as pd # importing dataframes (pandas is a package for datframes and related)
import numpy as np

def load_data(path):
    raw_data = pd.read_csv(path)
    data = pd.DataFrame(index=raw_data.index)
    data['name'] = raw_data[' Player Display Name']
    data['time'] = pd.to_datetime(raw_data[' Time'])


corners = [
    (41.381443, 2.122964),
    (41.380567, 2.123427),
    (41.381217, 2.122211),
    (41.380343, 2.122677),
]

def lat_long_to_x_y(lat, long, corners, length=100, width=68):
    corners = np.asarray(corners)
    center = corners.mean(axis=0)
    centered_corners = corners =
    










