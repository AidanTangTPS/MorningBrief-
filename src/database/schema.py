import sqlite3
conn = sqlite3.connect('plant_database')
def init_db():

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_readings ( id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, light_lux INTEGER, soil_moisture INTEGER, temperature REAL, humidity REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS decisions (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, decision_type TEXT NOT NULL, -- 'light' or 'water' action TEXT NOT NULL, duration_seconds INTEGER, confidence REAL, reasoning TEXT)
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS logbook ( id INTEGER PRIMARY KEY AUTOINCREMENT, day INTEGER NOT NULL, timestamp TEXT NOT NULL, entry TEXT NOT NULL)''')

    conn.commit()
    return conn
