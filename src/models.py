import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(String(8), nullable=False, unique=True)
    email = Column(String(40), nullable=False)
    suscription = Column(DateTime(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "user_last_name": self.last_name,
            "suscription": self.suscription
            # do not serialize the password, its a security breach
        }

class Character(Base):
    __tablename__='Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    birth_date = Column(String(15), nullable=True)
    gender = Column(String(10), nullable=True)
    height = Column(String(6), nullable=True)
    eye_color = Column(String(15), nullable=True)
    skin_color = Column(String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
        }

class Planet(Base):
    __tablename__='Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    diameter = Column(String(15), nullable=True)
    weather = Column(String(10), nullable=True)
    gravity = Column(String(6), nullable=True)
    cityzens = Column(String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "diameter": self.diameter,
            "weather": self.weather,
            "gravity": self.gravity,
            "cityzens": self.cityzens
        }

class Spaceship(Base):
    __tablename__='Spaceship'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    credit_cost = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=True)
    load_capacity = Column(Integer, nullable=True)
    kind = Column(String(15), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "credit_cost": self.credit_cost,
            "passengers": self.passengers,
            "load_capacity": self.load_capacity,
            "kind": self.kind
        }

class FavCharacter(Base):
    __tablename__='FavCharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    character_id = Column(Integer, ForeignKey(Character.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }

class FavPlanet(Base):
    __tablename__='FavPlanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    planet_id = Column(Integer, ForeignKey(Planet.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }

class FavSpaceship(Base):
    __tablename__='FavSpaceship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    spaceship_id = Column(Integer, ForeignKey(Spaceship.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "spaceship_id": self.spaceship_id,
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
