import sqlite3 as sql
from hent_togruter import hent_togruter
from registrer_kunde import registrer_kunde
from kjop_billett import hent_ledige_billetter, registrer_sittebillettkjop


def test_hent_togruter() -> None:
    print(
        hent_togruter(1, "mandag"),
        hent_togruter(6, "onsdag")
    )


def test_registrer_kunde() -> None:
    registrer_kunde("Gard Strom"     , "xXgard69@msn.no"               , "00000000")
    registrer_kunde("Jonas Nordstrom", "northstream_dankmaster@live.no", "00000001")


def test_kjop_billett() -> None:
    # print(hent_ledige_billetter(4, "23/03/2023", strekninger=[2, 4]))
    registrer_sittebillettkjop(2, 4, "23/03/2023", [3, 3], [7, 8], [6, 4])
    registrer_sittebillettkjop()