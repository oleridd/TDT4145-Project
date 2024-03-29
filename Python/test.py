import sqlite3 as sql
from hent_togruter import hent_togruter
from registrer_kunde import registrer_kunde
from kjop_billett import hent_ledige_billetter, registrer_sittebillettkjop, registrer_sovebillettkjop
from UI import hovedmeny
from TrainRoutes import get_train_routes_at_date
import get_orders
from sql_util import hent_delstrekninger_mellom_stasjoner

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
    registrer_sittebillettkjop(1, 10, "03.03.2023", 3, 11, [10, 8])
    # registrer_sovebillettkjop(2, 4, "23/03/2023", 5, 3, 2)
    # registrer_sittebillettkjop()


def test_UI():
    running = True
    while running:
        running = hovedmeny()
    
def test_get_train_routes_at_date() -> None:
    print(get_train_routes_at_date("25/03/2023", "01:00:00", startStasjonID= 6, endeStasjonID = 1))
    print(get_train_routes_at_date("28/03/2023", "08:00:00", startStasjonID= 2, endeStasjonID = 4))
    

def test_get_orders() -> None:
    print(get_orders.get_all_tickets_for_person(2))


def test_hent_delstrekninger_mellom_stasjoner():
    startstasjon = 4 # Bodø
    endestasjon = 1  # Mosjøen
    baneStrekningID = 1
    print(
        hent_delstrekninger_mellom_stasjoner(baneStrekningID, startstasjon, endestasjon)
    )