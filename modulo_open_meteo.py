import requests
import pandas as pd
from pandas_gbq import to_gbq

class tablaAPI:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.lugares = {
            'Town': ['Berriz', 'Madrid', 'Barcelona'],
            'Latitude': [43.1759, 40.4168, 41.385],
            'Longitude': [-2.5768, -3.7038, 2.1686]
        }
    def datos(self):
        all_dfs = []

        for town, lat, lon in zip(
            self.lugares["Town"],
            self.lugares["Latitude"],
            self.lugares["Longitude"]
        ):
            params = {
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
                "timezone": "Europe/Madrid"
            }

            data = requests.get(self.url, params=params).json()

            df = pd.DataFrame({
                "town": [town] * len(data["hourly"]["time"]),
                "time": data["hourly"]["time"],
                "temp": data["hourly"]["temperature_2m"],
                "wind": data["hourly"]["wind_speed_10m"],
                "humidity": data["hourly"]["relative_humidity_2m"]
            })

            all_dfs.append(df)

        return pd.concat(all_dfs)

class BigQueryLoader:
    def __init__(self, project_id, table_name):
        self.table_name = table_name
        self.project_id = project_id
    def loader(self, df):
        to_gbq(
            df,
            destination_table = self.table_name,
            project_id = self.project_id,
            if_exists = 'replace'
        )
