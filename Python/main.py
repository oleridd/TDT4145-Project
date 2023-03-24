import sqlite3 as sql
from test import *


def train_stop_at_station_on_day(station, day):
    con = sql.connect("Jernbanenett.db")
    cursor = con.cursor()


def main():
    # test_hent_togruter()
    # test_registrer_kunde()
    # test_kjop_billett()
    test_UI()


if __name__ == "__main__":
    main()