import sqlite3 as sql
import numpy as np


def get_smallest_elem_without_successor(arr: np.ndarray) -> int:
    """
    Given a numpy array of integers, returns the smallest element
    in the array which does not have a successor.
    If array is empty, returns 0.
    """

    if len(arr > 0):

        arr.sort()
        indicator = np.append(
            np.invert(arr[:-1] == (arr-1)[1:]), # Indexes elements without successors (except the last)
            [True]                              # Last element will never have a successor
        )
        return arr[indicator].min()
    
    return 0 # Array is empty


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