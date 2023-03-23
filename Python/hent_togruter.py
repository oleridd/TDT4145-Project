import sqlite3 as sql

def hent_togruter(stasjonID: int, ukedag: str) -> str:
    """
    Gitt en stasjonID og en ukedag, henter alle togruter som stopper
    på den stasjonen den gitte ukedagen.
    
    Argumenter:
        stasjonID (int)
        ukedag (string)
    Returnerer:
        Streng med togrutene som stopper på stasjonen
    """
    with sql.connect('Jernbanenett.db') as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT togruteForekomstID
            FROM Stasjon NATURAL JOIN StoppPaa NATURAL JOIN TogruteForekomst
            WHERE TogruteForekomst.ukedag = (:ukedag) AND StoppPaa.stasjonID = (:stasjonID)
            UNION
            SELECT togruteForekomstID
            FROM TogruteForekomst
            WHERE ukedag = (:ukedag) AND (startStasjonID = (:stasjonID) OR endestasjonID = (:stasjonID))
        """,
        {'ukedag': ukedag, 'stasjonID': stasjonID}
        )
    
    return cursor.fetchall()
