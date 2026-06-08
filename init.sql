CREATE TABLE IF NOT EXISTS earthquakes (
    id        TEXT PRIMARY KEY,
    place     TEXT,
    magnitude REAL,
    time      TIMESTAMPTZ,
    longitude REAL,
    latitude  REAL,
    depth     REAL
);