
m datetime import datetime
from pony.orm import *


db = Database()


class Movie(db.Entity):
    id = PrimaryKey(int, auto=True)
    dvd = Optional(str)
    name = Optional(str)
    length = Optional(str)
    description = Optional(str)
    poster = Optional(str)
    producer = Optional(str)
    year_of_release = Optional(str)
    genre = Required('Genre')
    dvds = Set('Dvd')
    age_rating = Required('Age_rating')


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Optional(str)
    last_name = Optional(str)
    email = Optional(str)
    address = Optional(str)
    phone_number = Optional(str)
    family = Optional(str)
    blacklisted = Optional(bool)
    cust_dvds = Set('Cust_dvd')


class Shelf(db.Entity):
    id = PrimaryKey(int, auto=True)
    racks = Optional(str)
    max_capacity = Optional(str)
    dvds = Set('Dvd')


class Age_rating(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    min_age = Optional(str)
    movies = Set(Movie)


class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    movies = Set(Movie)


class Dvd(db.Entity):
    id = PrimaryKey(int, auto=True)
    movie = Required(Movie)
    shelf = Required(Shelf)
    cust_dvds = Set('Cust_dvd')


class Cust_dvd(db.Entity):
    dvds = Required(Dvd)
    customers = Required(Customer)
    date_out = Optional(datetime)
    date_in = Optional(datetime)
    PrimaryKey(dvds, customers)



db.bind("postgres", host="localhost", user="cmaina",password="chelule", database="movies")
db.generate_mapping(create_tables=True)
