import sqlite3 as sql
from get_train_routes import get_train_routes


def train_stop_at_station_on_day(station, day):
    con = sql.connect("Jernbanenett.db")
    cursor = con.cursor()


def main():
    print(
        get_train_routes(1, "mandag"),
        get_train_routes(6, "onsdag")
    )


if __name__ == "__main__":
    main()