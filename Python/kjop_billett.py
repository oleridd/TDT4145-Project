import sqlite3 as sql
import numpy as np


def is_member_of(arr: np.ndarray, lst: list) -> np.ndarray:
    """
    Iterates each element of arr and checks whether it is
    an element of lst. Returns the result as a boolean array.
    """
    arr = arr.flatten()
    result = np.zeros(len(arr), dtype=bool)
    for i, elem in enumerate(arr):
        result[i] = elem in lst
    return result


def hent_ledige_billetter(togruteForekomstID: int, dato: str, strekninger: list[int]) -> tuple:
    """
    Henter ledige billetter for en gitt togruteforekomst.
    Siden det ikke er snakk om billettkjøp, er disse identifisert
    av reiseDato, togruteForekomstID og seteNr eller kupeNr. Sitte-
    Billett er i tillegg identifisert av delStrekningsID

    Argumenter:
        togruteForekomstID (int)
        dato            (string)
        strekninger  (list[int]): En liste med delstrekningene billetten skal gjelde
    Returnerer:
        Liste av: (vognID, seteNr, delStrekningID)
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
        sovebilletter = np.array(cursor.fetchall())

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
        sittebilletter = np.array(cursor.fetchall())

    # Henter kun ut relevante delstrekninger:
    sittebilletter = sittebilletter[
        is_member_of(sittebilletter[:, 2], strekninger)
    ]

    return sovebilletter, sittebilletter


def registrer_billettkjop():
    pass