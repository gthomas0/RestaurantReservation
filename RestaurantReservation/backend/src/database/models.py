import os
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'restaurants')
database_path = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    if not database_exists(database_path):
        create_database(database_path)
    migrate = Migrate(app, db)


class Reservation(db.Model):
    __tablename__ = 'reservation'

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), primary_key=True)
    patron_id = Column(Integer, ForeignKey('patron.id'), primary_key=True)
    start_time = Column(DateTime, primary_key=True)
    restaurant = relationship('Restaurant', back_populates='patrons')
    patron = relationship('Patron', back_populates='restaurants')

    def __init__(self, restaurant_id, patron_id, start_time):
        self.restaurant_id = restaurant_id,
        self.patron_id = patron_id
        self.start_time = start_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'restaurant_id': self.restaurant_id,
            'patron_id': self.patron_id,
            'start_time': self.start_time,
        }


class Patron(db.Model):
    __tablename__ = 'patron'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    restaurants = relationship('Reservation', back_populates='patron')

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sunday = Column(String)
    monday = Column(String)
    tuesday = Column(String)
    wednesday = Column(String)
    thursday = Column(String)
    friday = Column(String)
    saturday = Column(String)
    hours = Column(String)
    patrons = relationship('Reservation', back_populates='restaurant')

    def __init__(self, name, sunday, monday, tuesday, wednesday, thursday, friday, saturday, hours):
        self.name = name
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.hours = hours

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'name': self.name,
            'Sun': self.sunday,
            'Mon': self.monday,
            'Tues': self.tuesday,
            'Wed': self.wednesday,
            'Thur': self.thursday,
            'Fri': self.friday,
            'Sat': self.saturday,
            'hours': self.hours,
        }
