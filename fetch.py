import requests
import psycopg2
from datetime import datetime, timezone

# Trzęsienia z ostatniej doby, magnituda 2.5+ (format GeoJSON)
URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

def fetch():
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    return r.json()["features"]

def save(features):
    conn = psycopg2.connect(
        host="localhost", dbname="earthquakes",
        user="app", password="secret",
    )
    cur = conn.cursor()
    for f in features:
        p = f["properties"]
        lon, lat, depth = f["geometry"]["coordinates"]  # GeoJSON: [lon, lat, głębokość]
        cur.execute(
            """
            INSERT INTO earthquakes
                (id, place, magnitude, time, longitude, latitude, depth)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                f["id"], p["place"], p["mag"],
                datetime.fromtimestamp(p["time"] / 1000, tz=timezone.utc),
                lon, lat, depth,
            ),
        )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    data = fetch()
    save(data)
    print(f"Zapisano {len(data)} trzęsień ziemi")