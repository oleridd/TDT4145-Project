import sqlite3 as sql

def get_train_routes(stasjonID: int, ukedag: str) -> str:
    """
    Given a station ID and a weekday, returns all train routes which stop
    at that station that day.
    
    Args:
        stasjonID (int): ID of the relevant station
        ukedag (string): The weekday in question
    Returns:
        String of train routes which stop at the station the given weekday.
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
