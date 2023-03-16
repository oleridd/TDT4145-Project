import sqlite3 as s

con = s.connect("Jernbanenett.db")

cursor = con.cursor()

cursor.execute("SELECT * FROM Stasjon")

rows = cursor.fetchall()
print("All rows in the table stasjon:")
print(rows)

con.close()