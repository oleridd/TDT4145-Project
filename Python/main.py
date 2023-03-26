import sqlite3 as sql
from test import *
import get_orders


def train_stop_at_station_on_day(s1tation, day):
    con = sql.connect("Jernbanenett.db")
    cursor = con.cursor()


def main():
    # test_hent_togruter()
    # test_registrer_kunde()
    # #test_kjop_billett()
    # test_UI()
    test_get_train_routes_at_date()


if __name__ == "__main__":
    main()