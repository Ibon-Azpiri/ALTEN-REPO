import requests
import pandas as pd
from pandas_gbq import to_gbq

def run(url: str, project_id: str, table_name: str):

    lugares = {
        'Town': ['Berriz', 'Madrid', 'Barcelona'],
        'Latitude': [43.1759, 40.4168, 41.385],
        'Longitude': [-2.5768, -3.7038, 2.1686]
    }

    all_dfs = []

    for town, lat, lon in zip(lugares["Town"], lugares["Latitude"], lugares["Longitude"]):
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
            "timezone": "Europe/Madrid"
        }

        data = requests.get(url, params=params).json()

        df = pd.DataFrame({
            "town": [town] * len(data["hourly"]["time"]),
            "time": data["hourly"]["time"],
            "temp": data["hourly"]["temperature_2m"],
            "wind": data["hourly"]["wind_speed_10m"],
            "humidity": data["hourly"]["relative_humidity_2m"],
        })

        all_dfs.append(df)

    df_final = pd.concat(all_dfs)

    to_gbq(
        df_final,
        destination_table = table_name,
        project_id = project_id,
        if_exists = 'replace',
    )
