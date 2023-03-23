import sqlite3 as sql
from test import *


def train_stop_at_station_on_day(station, day):
    con = sql.connect("Jernbanenett.db")
    cursor = con.cursor()


def main():
    # test_get_train_routes()
    # test_register_customer()
    test_purchase_ticket()


if __name__ == "__main__":
    main()