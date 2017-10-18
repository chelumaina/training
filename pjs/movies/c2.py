
from datetime import date
from pony.orm import *


db = Database()


class Movie(db.Entity):
    id = PrimaryKey(int, auto=True)
    genre = Required('Genre')
    age__rating = Required('Age_Rating')
    dvds = Set('Dvd')
    name = Optional(str)
    length = Optional(int)
    producer = Optional(str)
    description = Optional(LongStr)
    poster = Optional(LongStr)
    year = Required(date)


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    dvds = Set('Dvd')
    fisrt_name = Optional(str)
    last_name = Optional(str)
    email = Optional(str)
    address = Optional(LongStr)
    phone = Optional(str)
    family = Optional(bool)
    blacklisted = Optional(bool)


class Shelve(db.Entity):
    id = PrimaryKey(int, auto=True)
    dvds = Set('Dvd')
    rack = Optional(int)
    max_capacity = Optional(int)


class Genre(db.Entity):
    genre_id = PrimaryKey(int, auto=True)
    movies = Set(Movie)
    name = Optional(str)
    desccription = Optional(LongStr)


class Age_Rating(db.Entity):
    id = PrimaryKey(int, auto=True)
    movies = Set(Movie)
    name = Optional(str)
    min_age = Optional(int)


class Dvd(db.Entity):
    id = PrimaryKey(int, auto=True)
    movie = Required(Movie)
    shelve = Required(Shelve)
    customers = Set(Customer)




db.bind("postgres", host="localhost", user="cmaina",password="chelule", database="cmaina")



db.generate_mapping(create_tables=True)


