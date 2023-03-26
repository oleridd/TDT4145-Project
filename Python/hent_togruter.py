import sqlite3 as sql
import numpy as np


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
            SELECT Banestrekning.navn, startstasjon.navn, tf.avgang, endestasjon.navn, tf.ankomst
            FROM TogruteForekomst AS tf INNER JOIN StoppPaa AS sp ON (tf.togruteforekomstID = sp.togruteforekomstID)
            NATURAL JOIN Banestrekning
            INNER JOIN Stasjon AS startstasjon ON (tf.startStasjonID = startstasjon.stasjonID)
            INNER JOIN Stasjon AS endestasjon  ON (tf.endeStasjonID  = endestasjon.stasjonID)
            WHERE tf.ukedag = (:ukedag) AND sp.stasjonID = (:stasjonID)
        """,
        {'ukedag': ukedag, 'stasjonID': stasjonID}
        )

    return np.array(cursor.fetchall())
