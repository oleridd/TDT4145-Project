import sqlite3 as sql 
from datetime import datetime
from datetime import timedelta
from utility import get_weekday_from_date, get_next_weekday_from_date
import numpy as np
from utility import *
      
def get_train_routes_at_date(date: str, travel_at: str, startStasjonID : int, endeStasjonID : int, id = False) -> str:
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
        travels between the start and end station, ordered earliest to latest.
    """
    date = try_parsing_date(date)
    next_date = date + timedelta(days = 1)
    this_day, next_day = get_weekday_from_date(date), get_next_weekday_from_date(date)
    with sql.connect('Jernbanenett.db') as con:
        cursor = con.cursor()
        
        cursor.execute("""
            SELECT st1.navn, sp1.avgang, st2.navn, sp2.ankomst, tg1.ukedag, tg1.togruteForekomstID
            FROM (TogruteForekomst AS tg1 INNER JOIN (StoppPaa as sp1 NATURAL JOIN Stasjon AS st1) ON
            tg1.togruteForekomstID = sp1.togruteForekomstID)
            INNER JOIN 
            (TogruteForekomst AS tg2 INNER JOIN (StoppPaa as sp2 NATURAL JOIN Stasjon AS st2) ON
            tg2.togruteForekomstID = sp2.togruteForekomstID)
            ON tg1.togruteForekomstID = tg2.togruteForekomstID
            WHERE (time((:travel_at)) <= time(sp1.avgang) OR tg1.ukedag = (:next_day)) AND
            ((time(sp1.avgang) <= time(sp2.ankomst) OR
            (sp1.dagNr < sp2.dagNr))
            and (tg1.ukedag = (:this_day) OR tg1.ukedag = (:next_day))
            and (sp1.stasjonID = (:startStasjonID)  and sp2.stasjonID = (:endeStasjonID)))
            ORDER BY 
            CASE
                WHEN tg1.ukedag = (:this_day) THEN 0
                WHEN tg1.ukedag = (:next_day) THEN 1
            END ASC, sp1.dagNr, sp1.avgang           
            """,
            {'this_day': this_day, 'next_day': next_day, 'travel_at': travel_at, "startStasjonID" : startStasjonID, "endeStasjonID" : endeStasjonID}
        )
        togruter = list(cursor.fetchall())
        togrute_id = list()
        for i in range(len(togruter)):
            togrute_list = list(togruter[i])
            togrute_id.append(togrute_list[5])
            togruter[i] = togrute_list[:4]
        for i in range(len(togruter)):
            if togruter[i][4] == this_day:
                togruter[i][4] = str(date)
            else:
                togruter[i][4] = str(next_date)
        if id:
            return togrute_id, np.array(togruter)
        else:
            return np.array(togruter)