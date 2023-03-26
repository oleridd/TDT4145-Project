import sqlite3 as sql 
from datetime import datetime
from utility import get_weekday_from_date, get_next_weekday_from_date
import numpy as np
      
def get_train_routes_at_date(date: str, travel_at: str, startStasjonID : int, endeStasjonID : int) -> str:
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
    this_day, next_day = get_weekday_from_date(date), get_next_weekday_from_date(date)

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
            WHERE (time((:travel_at)) <= time(sp1.avgang) OR tg1.ukedag = (:next_day)) AND
            ((time(sp1.avgang) <= time(sp2.ankomst) OR
            (sp1.dagNr < sp2.dagNr))
            and (tg1.ukedag = (:this_day) OR tg1.ukedag = (:next_day))
            and sp1.stasjonID = (:startStasjonID)  and sp2.stasjonID = (:endeStasjonID)
            ORDER BY 
            CASE
                WHEN tg1.ukedag = 'søandag' THEN 1
                WHEN tg1.ukedag = 'mandag' THEN 2
                WHEN tg1.ukedag = 'tirsdag' THEN 3
                WHEN tg1.ukedag = 'onsdag' THEN 4
                WHEN tg1.ukedag = 'torsdag' THEN 5
                WHEN tg1.ukedag = 'fredag' THEN 6
                WHEN tg1.ukedag = 'lørdag' THEN 7
            END ASC, sp1.dagNr, sp1.avgang           
            """,
            {'this_day': this_day, 'next_day': next_day, 'travel_at': travel_at, "startStasjonID" : startStasjonID, "endeStasjonID" : endeStasjonID}
        )
        togruter = np.array(cursor.fetchall())
        return togruter