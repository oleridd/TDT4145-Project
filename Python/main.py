import sqlite3 as sql
#from test import *
import get_orders


def train_stop_at_station_on_day(station, day):
    con = sql.connect("Jernbanenett.db")
    cursor = con.cursor()


def main():
    # test_hent_togruter()
    # test_registrer_kunde()
    # #test_kjop_billett()
    test_UI()
    get_orders.get_all_tickets_for_person(2)
    return


if __name__ == "__main__":
    main()