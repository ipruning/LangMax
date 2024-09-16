from typing import Optional

from sqlite_utils import Database
from sqlmodel import Field, Session, SQLModel, create_engine, select

animals_data = [
    {"name": "Azi", "color": "blue", "age": 2},
    {"name": "Lila", "color": "blue", "age": 3},
    {"name": "Suna", "color": "gold"},
    {"name": "Cardi", "color": "black", "age": 1},
]


def test_sqlmodel():
    class Animal(SQLModel, table=True):  # type: ignore
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str
        color: str
        age: Optional[int] = None

    sqlmodel_engine = create_engine("sqlite:///animals_sqlmodel.db")
    SQLModel.metadata.create_all(sqlmodel_engine)

    with Session(sqlmodel_engine) as session:
        for animal_data in animals_data:
            animal = Animal(**animal_data)
            session.add(animal)
        session.commit()

    print("Animals added using SQLModel:")
    with Session(sqlmodel_engine) as session:
        statement = select(Animal)
        animals = session.exec(statement).all()
        for _ in animals:
            print(_.model_dump())


def test_sqlite_utils():
    sqlite_utils_db = Database("animals_sqlite.db")

    sqlite_utils_db["animals"].insert_all(animals_data)

    print("\nAnimals added using sqlite-utils:")
    for _ in sqlite_utils_db["animals"].rows:
        print(_)


test_sqlmodel()
test_sqlite_utils()
