import sqlite3 as sql 
from datetime import datetime


class TrainRoutes:

    def __init__(self):

        self.date_map = {
            0 : "mandag" ,
            1 : "tirsdag",
            2 : "onsdag" ,
            3 : "torsdag",
            4 : "fredag" ,
            5 : "lørdag" ,
            6 : "søndag"
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
        this_day, next_day = self.date_map[weekday_nr-1], self.date_map[weekday_nr % 7]

        with sql.connect('Jernbanenett.db') as con:
            cursor = con.cursor()
            
            # New not ready yet version
            cursor.execute("""
                SELECT tg1.togruteForekomstID
                FROM (TogruteForekomst AS tg1 INNER JOIN StoppPaa as sp1 on
                tg1.togruteForekomstID = sp1.togruteForekomstID)
                INNER JOIN 
                (TogruteForekomst AS tg2 INNER JOIN StoppPaa as sp2 on
                tg2.togruteForekomstID = sp2.togruteForekomstID)
                ON tg1.togruteForekomstID = tg2.togruteForekomstID
                WHERE ((time(sp1.avgang) <= time(sp2.ankomst) OR
                (sp1.dayNr < sp2.dagNr))
                and (tg1.ukedag = (:this_day) OR tg1.ukedag = (:next_day))
                and sp1.stasjonID = (:startStasjonID)  and sp2.stasjonID = (:endeStasjonID) 
                ORDER BY tg1.avgang           
                """,
                {'this_day': this_day, 'next_day': next_day, 'time': time, "startStasjonID" : startStasjonID, "endeStasjonID" : endeStasjonID}
            )