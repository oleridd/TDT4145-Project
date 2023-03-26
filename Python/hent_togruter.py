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

# def hent_generell_togruteforekomst_info(togruteforekomstID: int) -> str:
#     """
#     Gitt en togruteforekomstID, henter info på formen:
#     (Banestrekning, avgang (startstasjon), ankomst (endestasjon))
#     """
#     with sql.connect("Jernbanenett.db") as con:
#         cursor = con.cursor()
#         cursor.execute("""
#             SELECT Banestrekning.navn, startstasjon.navn, avgang, endestasjon.navn, ankomst
#             FROM Togruteforekomst NATURAL JOIN Togrute NATURAL JOIN Banestrekning
#                 INNER JOIN Stasjon AS startstasjon ON (Togruteforekomst.startStasjonID = startstasjon.stasjonID)
#                 INNER JOIN Stasjon AS endestasjon  ON (Togruteforekomst.endeStasjonID  = endestasjon.stasjonID)
#             WHERE togruteforekomstID = (:togruteforekomstID)
#         """,
#         {'togruteforekomstID': togruteforekomstID}
#         )
#         data = np.array(cursor.fetchall()).flatten()
#     return "{} | Avgang fra {}: {} | Ankomst til {}: {}".format(*data)


# def hent_ankomsttid(togruteForekomstID: int, stasjonID: int) -> tuple:
#     """
#     Henter ankomst til en stasjon for en gitt togruteforekomst
#     """
#     with sql.connect("Jernbanenett.db") as con:
#         cursor = con.cursor()
#         cursor.execute("""
#             SELECT ankomst
#             FROM StoppPaa
#             WHERE togruteForekomstID = (:togruteForekomstID) AND stasjonID = (:stasjonID)
#         """,
#         {'togruteForekomstID': togruteForekomstID, 'stasjonID': int(stasjonID)}
#         )
#         result = np.array(cursor.fetchall()).flatten()
    
#     return result

# def hent_togruter(stasjonID: int, ukedag: str) -> str:
#     """
#     Gitt en stasjonID og en ukedag, henter alle togruter som stopper
#     på den stasjonen den gitte ukedagen.
    
#     Argumenter:
#         stasjonID (int)
#         ukedag (string)
#     Returnerer:
#         Streng med togrutene som stopper på stasjonen
#     """
#     with sql.connect('Jernbanenett.db') as con:
#         cursor = con.cursor()
#         cursor.execute("""
#             SELECT tf.togruteforekomstID
#             FROM TogruteForekomst AS tf INNER JOIN StoppPaa AS sp ON (tf.togruteforekomstID = sp.togruteforekomstID)
#             WHERE tf.ukedag = (:ukedag) AND sp.stasjonID = (:stasjonID)
#         """,
#         {'ukedag': ukedag, 'stasjonID': stasjonID}
#         )

    return np.array(cursor.fetchall()).flatten()