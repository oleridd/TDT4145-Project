import sqlite3 as sql 
from datetime import datetime


class TrainRoutes:

    def __init__(self):

        self.date_map = {
            1 : "mandag" ,
            2 : "tirsdag",
            3 : "onsdag" ,
            4 : "torsdag",
            5 : "fredag" ,
            6 : "lørdag" ,
            7 : "søndag"
        }
        

    def get_train_routes_at_date(self, date: str, time: str, startStasjonID : int, endeStasjonID : int) -> str:
        """
        Given a date, a start station and a end station, 
        returns all train routes which are available that day.
        
        Args:
            date        (string): date of the form YYYY-MM-DD
            time        (string): Time
            startStasjonID (int): ID of the start station for the route
            endeStasjonID  (int): ID of the end station for the route
        Returns:
            String of train routes which is available at that given date and which
            travels between the start and end station.
        """
        dt = datetime.strptime(date, '%Y-%m-%d').date()
        weekday_nr = dt.isoweekday()
        this_day, next_day = self.date_map[weekday_nr], self.date_map[weekday_nr+1]

        with sql.connect('Jernbanenett.db') as con:
            cursor = con.cursor()
            cursor.execute("""
                SELECT togruteForekomstID
                FROM TogruteForekomst
                WHERE togruteForekomstID IN (
                    SELECT togruteForekomstID
                    FROM TogruteForekomst NATURAL JOIN StoppPaa
                    WHERE StoppPaa.stasjonID = (:startStasjonID) OR StoppPaa.stasjonID = (:endeStasjonID)
                ) AS togruteStopp AND
                /* Hvordan får man rikig rekkefølge på start- og endestasjon */
                """,
                {'this_day': this_day, 'next_day': next_day, 'time': 'time'}
            )
            # WHERE (ukedag = (:this_day) AND CAST(StoppPaa.ankomst AS FLOAT) > cast((:time) AS FLOAT)) OR
            # ukedag = (:next_day) AND StoppPaa.stasjonID = (:startStasjonID)