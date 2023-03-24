import sqlite3 as sql
import numpy as np


def hent_alle_stasjonID() -> np.ndarray:
    """
    Henter ID på alle stasjoner.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT stasjonID
            FROM Stasjon
        """)
        return np.array(cursor.fetchall()).flatten()


def hent_stasjonID(stasjonnavn: str) -> int:
    """
    Henter stasjonID gitt navn på en stasjon.
    Denne funksjonen antar at alle stasjoner har unike navn.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT stasjonID
            FROM Stasjon
            WHERE navn = (:stasjonnavn)
        """,
        {'stasjonnavn': stasjonnavn}
        )
        stasjonID = np.array(cursor.fetchall())
    
    if len(stasjonID) > 1:
        raise RuntimeError("Fant ikke unik stasjon")
    else: 
        return int(stasjonID[0])


def hent_togruteforekomst_info(togruteforekomstID: int) -> str:
    """
    Gitt en togruteforekomstID, henter info på formen:
    (Banestrekning, avgang (startstasjon), ankomst (endestasjon))
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT Banestrekning.navn, startstasjon.navn, avgang, endestasjon.navn, ankomst
            FROM Togruteforekomst NATURAL JOIN Togrute NATURAL JOIN Banestrekning
                                  INNER JOIN Stasjon AS startstasjon ON (Togruteforekomst.startStasjonID = startstasjon.stasjonID)
                                  INNER JOIN Stasjon AS endestasjon  ON (Togruteforekomst.endeStasjonID  = endestasjon.stasjonID)
            WHERE togruteforekomstID = (:togruteforekomstID)
        """,
        {'togruteforekomstID': togruteforekomstID}
        )
        data = np.array(cursor.fetchall()).flatten()
    
    return "Togrute {}, avgang fra {}: {}, ankomst til {}: {}".format(*data)