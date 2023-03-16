import sqlite3 as sql 
from datetime import datetime

class train_routes:
    def __init__(self):
        self.date_map = {1 : "mandag",
                    2 : "tirsdag",
                    3 : "onsdag",
                    4 : "torsdag",
                    5 : "fredag",
                    6 : "lørdag",
                    7 : "søndag"}


    def get_train_routes_at_date(self, dato: str, startStasjonID : int, endeStasjonID : int) -> str:
        """
        Given a date, a start station and a end station, 
        returns all train routes which are available that day.
        
        Args:
            dato (str): date of the form YYYY-MM-DD
            startStasjonID (int): ID of the start station for the route
            endeStasjonID (int): ID of the end station for the route
        Returns:
            String of train routes which is available at that given date and which
            travels between the start and end station.
        """
        
        dt= datetime.strptime(dato, '%Y-%m-%d').date()
        weekday_nr = dt.isoweekday()
        weekday = self.date_map[weekday_nr]
        with sql.connect('Jernbanenett.db') as con:
            cursor = con.cursor()
            cursor.execute("""
                "SELECT togruteForekomstID
                FROM 
                """,
            )