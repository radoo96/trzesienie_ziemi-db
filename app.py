from flask import Flask, jsonify, send_file
import psycopg2
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_earthquakes():
    conn = psycopg2.connect(
        host="localhost", dbname="earthquakes",
        user="app", password="secret",
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT place, magnitude, time, longitude, latitude, depth
        FROM earthquakes
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        ORDER BY time DESC
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "place": r[0], "magnitude": r[1],
            "time": r[2].isoformat() if r[2] else None,
            "longitude": r[3], "latitude": r[4], "depth": r[5],
        }
        for r in rows
    ]

@app.route("/api/earthquakes")
def api_earthquakes():
    return jsonify(get_earthquakes())

@app.route("/")
def index():
    return send_file(os.path.join(BASE_DIR, "index.html"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)