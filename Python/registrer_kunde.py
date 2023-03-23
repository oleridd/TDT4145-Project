import sqlite3 as sql
import numpy as np
from utility import get_smallest_elem_without_successor


def registrer_kunde(navn: str, epost: str, mobilnummer: str) -> None:
    """
    Registrerer kunden i databasen

    Args:
        navn        (string)
        epost       (string)
        mobilnummer (string)
    Returns:
        None
    """
    # Retrieving existing customer IDs:
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT kID
            FROM Kunde
        """)
        IDs = np.array(cursor.fetchall()).flatten()

    new_ID = get_smallest_elem_without_successor(IDs) + 1

    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO Kunde
            VALUES
            ((:new_ID), (:navn), (:epost), (:mobilnummer));
        """,
        {'new_ID': int(new_ID), 'navn': navn, 'epost': epost, 'mobilnummer': mobilnummer}
        )