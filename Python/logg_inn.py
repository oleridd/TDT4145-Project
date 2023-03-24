import sqlite3 as sql
import numpy as np

def hent_innloggingsinfo(bruker_in: str) -> int:
    """
    Gitt e-post eller tlf for en bruker, returnerer kID.

    Argumenter:
        bruker_in (string)
    Returnerer:
        kID (int). Dersom brukeren ikke blir funnet, returneres -1.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT kID, epost, mobilnummer
            FROM Kunde
        """)
        kunde_info = np.array(cursor.fetchall())
    
    if bruker_in not in kunde_info.flatten():
        return -1
    else:
        row_ind = np.any(bruker_in == kunde_info[:, 1:], axis=1)
        return int(kunde_info[row_ind, 0])