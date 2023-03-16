import sqlite3 as s

con = s.connect("Jernbanenett.db")

cursor = con.cursor()

cursor.execute("SELECT * FROM Stasjon")

rows = cursor.fetchall()
print("All rows in the table stasjon:")
print(rows)

con.close()


def train_stop_at_station_on_day(station, day):
    con = s.connect("Jernbanenett.db")
    cursor = con.cursor()