import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'USER'

    id = Column(Integer, primary_key=True)
    User_name = Column(String(120), nullable=False)
    Name = Column(String(250), nullable=False)
    Password = Column(String(120), nullable=False)
    Email = Column(String(250), nullable=False)
    
class Characters(Base):
    __tablename__ ="CHARACTERS"

    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Birth = Column(String(120), nullable=False)
    Gender = Column(String(120), nullable=False)
    Heigth = Column(Integer)
    Skin_color = Column(String(120), nullable=False)
    Eyes_color = Column(String(120), nullable=False)
    

class Planets(Base):
    __tablename__ = "PLANETS"

    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Climate = Column(Integer)
    Population = Column(Integer)
    Orbital_period = Column(Integer)
    Rotation_period = Column(Integer)
    diameter = Column(Integer)

class Userfavorite(Base):
    __tablename__ = 'USER_FAVORITES'
    
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('USER.id'))
    Characters_id = Column(Integer, ForeignKey('CHARACTERS.id'))
    Planets_id = Column(Integer, ForeignKey('PLANETS.id'))
    user = relationship(User)
    Character = relationship(Characters)
    planets = relationship(Planets)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')