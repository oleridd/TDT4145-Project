import sqlite3 as sql
from hent_togruter import hent_togruter
from registrer_kunde import registrer_kunde
from kjop_billett import hent_ledige_billetter, registrer_sittebillettkjop, registrer_sovebillettkjop
from UI import hovedmeny
from TrainRoutes import get_train_routes_at_date
import get_orders

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
    registrer_sittebillettkjop(2, 4, "23/03/2023", [4, 4], [7, 8], [2])
    # registrer_sovebillettkjop(2, 4, "23/03/2023", 5, 3, 2)
    # registrer_sittebillettkjop()


def test_UI():
    running = True
    while running:
        running = hovedmeny()
    
def test_get_train_routes_at_date() -> None:
    print(get_train_routes_at_date("2023-03-25", "01:00:00", startStasjonID= 6, endeStasjonID = 1))
    print(get_train_routes_at_date("2023-03-28", "08:00:00", startStasjonID= 2, endeStasjonID = 4))
    

def test_get_orders() -> None:
    print(get_orders.get_all_tickets_for_person(2))