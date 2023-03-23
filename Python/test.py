import sqlite3 as sql
from get_train_routes import get_train_routes
from register_customer import register_customer


def test_get_train_routes() -> None:
    print(
        get_train_routes(1, "mandag"),
        get_train_routes(6, "onsdag")
    )


def test_register_customer() -> None:
    register_customer("Gard Strom"     , "xXgard69@msn.no"               , "00000000")
    register_customer("Jonas Nordstrom", "northstream_dankmaster@live.no", "00000001")