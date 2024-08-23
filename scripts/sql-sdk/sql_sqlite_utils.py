from sqlite_utils import Database

db = Database("chickens.db")
db["chickens"].insert_all(  # type: ignore
    [
        {
            "name": "Azi",
            "color": "blue",
        },
        {
            "name": "Lila",
            "color": "blue",
        },
        {
            "name": "Suna",
            "color": "gold",
        },
        {
            "name": "Cardi",
            "color": "black",
        },
    ]
)

for row in db["chickens"].rows:
    print(row)
