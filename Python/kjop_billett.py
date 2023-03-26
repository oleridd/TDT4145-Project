import sqlite3 as sql
import numpy as np
from utility import get_smallest_elem_without_successor, is_member_of, list_in


def hent_ledige_billetter(togruteForekomstID: int, dato: str, strekninger: list = None) -> tuple:
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
    # NOTE: Må kanskje verifisere at togruteforekomst går på den gitte datoen
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
        sittebilletter = None
        if strekninger is not None: # None hvis vi kun ønsker sovebilletter
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
                    FROM SitteBillett AS sb NATURAL JOIN SitteBillettPaaDelstrekning
                    WHERE sb.reiseDato = (:dato) AND sb.togruteForekomstID = (:togruteForekomstID)
                )
            """,
            {'togruteForekomstID': togruteForekomstID, 'dato': dato}
            )
            sittebilletter = np.array(cursor.fetchall())

            # Henter kun ut relevante delstrekninger:
            if len(sittebilletter) > 0:
                sittebilletter = sittebilletter[
                    is_member_of(sittebilletter[:, 2], strekninger)
                ]

    return sovebilletter, sittebilletter


def hent_vognNr(vognID: int) -> int:
    """
    Gitt en vognID, henter ut vognnummer.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT vognNr
            FROM VognITog
            WHERE vognID = (:vognID)
        """,
        {'vognID': int(vognID)}
        )
        vognNr = np.array(cursor.fetchall()).flatten()[0]
    
    return int(vognNr)


def registrer_sovebillettkjop(kID: int, togruteForekomstID: int, dato: str, vognID, kupeNR, antallSeng) -> None:
    """
    Registrerer kjøp av sovebillett for en registrert kunde.

    Argumenter:
        kID                 (int): Kunde ID
        togruteForekomstID  (int)
        dato             (string)
        vognID              (int)
        kupeNR              (int)
        antallSeng          (int): Antall senger i kupeen
    Returnerer:
        None
    """
    # NOTE: Innfør logikk på å ta utgangspunkt i vognNr når man spør kunden

    # Sjekk at billetten som skal bestilles er ledig:
    ledige_billetter, _ = hent_ledige_billetter(togruteForekomstID, dato)
    try:
        assert list_in([vognID, kupeNR], ledige_billetter)
    except AssertionError:
        raise RuntimeError("Billetter på dette setet er allerede registrert eller delstrekningen er ikke i togruten")


    with sql.connect("Jernbanenett.db") as con:

        # Sjekker at kunden er registrert:
        cursor = con.cursor()
        cursor.execute("""
            SELECT kID
            FROM Kunde
        """)
        if not kID in np.array(cursor.fetchall()).flatten():
            raise RuntimeError("Kunde er ikke registrert")

        # Bestem unik ordreID:
        cursor = con.cursor()
        cursor.execute("""
            SELECT ordereID
            FROM KundeOrdere
        """)
        brukt_ordreID = np.array(cursor.fetchall())
        ordreID = get_smallest_elem_without_successor(brukt_ordreID) + 1

        # Insertering i KundeOrdre:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO KundeOrdere
            VALUES
            ((:ordreID), (:dato), (:kID));
        """,
        {'ordreID': ordreID, 'dato': dato, 'kID': kID}
        )

        # Insertering i SitteBillett og SittebillettPaaDelstrekning:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO SoveBillett
            VALUES
            ((:ordreID), (:billettNR), (:vognID), (:kupeNR), (:togruteForekomstID), (:dato), (:antallSeng));
        """,
        {'ordreID': ordreID, 'billettNR': 1, 'vognID': vognID, 'kupeNR': kupeNR, 'togruteForekomstID': togruteForekomstID, 'dato': dato, 'antallSeng': antallSeng}
        )


def registrer_sittebillettkjop(kID: int, togruteForekomstID: int, dato: str, vognID, seteNR, strekninger) -> None:
    """
    Registrerer kjøp av sittebillett for en registrert kunde.

    Argumenter:
        kID                 (int): Kunde ID
        togruteForekomstID  (int)
        dato             (string)
        vognID (int or list[int])
        seteNR (int or list[int])
        strekninger   (list[int]): Delstrekninger som billetten går over
    Returnerer:
        None
    """
    # NOTE: Innfør logikk på å ta utgangspunkt i vognNr når man spør kunden

    # Pass på riktig listestruktur:
    if not isinstance(vognID, list): vognID = [vognID]
    if not isinstance(seteNR, list): seteNR = [seteNR]
    assert len(vognID) == len(seteNR)

    # Sjekk at billetten som skal bestilles er ledig:
    _, ledige_billetter = hent_ledige_billetter(togruteForekomstID, dato, strekninger)
    try:
        for vID, sNR in zip(vognID, seteNR):
            for delStrk in strekninger:
                assert list_in([vID, sNR, delStrk], ledige_billetter)
    except AssertionError:
        raise RuntimeError("Billetter på dette setet er allerede registrert")


    with sql.connect("Jernbanenett.db") as con:

        # Sjekker at kunden er registrert:
        cursor = con.cursor()
        cursor.execute("""
            SELECT kID
            FROM Kunde
        """)
        if not kID in np.array(cursor.fetchall()).flatten():
            raise RuntimeError("Kunde er ikke registrert")

        # Bestem unik ordreID:
        cursor = con.cursor()
        cursor.execute("""
            SELECT ordereID
            FROM KundeOrdere
        """)
        brukt_ordreID = np.array(cursor.fetchall())
        ordreID = get_smallest_elem_without_successor(brukt_ordreID) + 1

        # Insertering i KundeOrdre:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO KundeOrdere
            VALUES
            ((:ordreID), (:dato), (:kID));
        """,
        {'ordreID': ordreID, 'dato': dato, 'kID': kID}
        )

        # Insertering i SitteBillett og SittebillettPaaDelstrekning:
        for i, (vID, sNR) in enumerate(zip(vognID, seteNR)):
            cursor = con.cursor()
            cursor.execute("""
                INSERT INTO SitteBillett
                VALUES
                ((:ordreID), (:billettNR), (:vognID), (:seteNR), (:togruteForekomstID), (:dato));
            """,
            {'ordreID': ordreID, 'billettNR': i+1, 'vognID': vID, 'seteNR': sNR, 'togruteForekomstID': togruteForekomstID, 'dato': dato}
            )
            
            for delStrk in strekninger:
                cursor = con.cursor()
                cursor.execute("""
                    INSERT INTO SittebillettPaaDelstrekning
                    VALUES
                    ((:delStrekningID), (:ordreID), (:billettNR));
                """,
                {'delStrekningID': delStrk, 'ordreID': ordreID, 'billettNR': i+1}
                )