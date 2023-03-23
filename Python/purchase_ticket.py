import sqlite3 as sql
import numpy as np


def hent_ledige_billetter(togruteForekomstID: int, dato: str) -> tuple:
    """
    Henter ledige billetter for en gitt togruteforekomst.
    Siden det ikke er snakk om billettkjøp, er disse identifisert
    av reiseDato, togruteForekomstID og seteNr eller kupeNr. Sitte-
    Billett er i tillegg identifisert av delStrekningsID

    Argumenter:
        togruteForekomstID (int)
        dato            (string)
    Returnerer:
        Liste av: (vognID, seteNr)
              og: (vognID, kupeNr)
    """
    # NOTE: Husk å passe på at ordreID for billetter er unikt
    with sql.connect("Jernbanenett.db") as con:

        # Sovebillett:
        cursor = con.cursor()
        cursor.execute("""
            SELECT vognID, kupeNr  /* Alle kupeer i den gitte togruteforekomsten */
            FROM TogruteForekomst NATURAL JOIN VognITog
                                  NATURAL JOIN Kupe
            WHERE togruteForekomstID = (:togruteForekomstID) AND (vognID, kupeNr) NOT IN (
                SELECT vognID, kupeNr  /* Kupeer som er opptatt i den gitte togruteforekomsten */
                FROM SoveBillett
                WHERE reiseDato = (:dato) AND togruteForekomstID = (:togruteForekomstID)
            );
        """,
        {'togruteForekomstID': togruteForekomstID, 'dato': dato}
        )
        print(len(cursor.fetchall()))


        # Sittebillett:
        cursor = con.cursor()
        cursor.execute("""
            SELECT vognID, seteNr, delStrekningID  /* Alle seter på alle delstrekninger i den gitte togruteforekomsten */
            FROM TogruteForekomst AS mainTF NATURAL JOIN VognITog
                                            NATURAL JOIN Sete
                                            CROSS   JOIN (
                                                SELECT delStrekningID /* Alle delstrekninger på den gitte togruteforekomsten */
                                                FROM TogruteForekomst AS delTF NATURAL JOIN Togrute
                                                                               NATURAL JOIN StrekningPaaBanestrekning
                                                WHERE delTF.togruteForekomstID = (:togruteForekomstID)
                                            )
            WHERE mainTF.togruteForekomstID = (:togruteForekomstID) AND (vognID, seteNr, delStrekningID) NOT IN (
                SELECT vognID, seteNr, delStrekningID  /* Seter som er opptatt i den gitte togruteforekomsten */
                FROM SitteBillett sb NATURAL JOIN SitteBillettPaaDelstrekning
                WHERE sb.reiseDato = (:dato) AND sb.togruteForekomstID = (:togruteForekomstID)
            )
        """,
        {'togruteForekomstID': togruteForekomstID, 'dato': dato}
        )