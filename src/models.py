import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id          = Column(Integer, primary_key=True)
    name        = Column(String(250), nullable=False)
    mass        = Column(String(30), nullable=False)
    hair_color	= Column(String(10), nullable=False)
    skin_color	= Column(String(10), nullable=False)
    eye_color	= Column(String(10), nullable=False)
    birth_year	= Column(String(10), nullable=False)
    gender	    = Column(String(30), nullable=False)
    height      = Column(String(10), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id              = Column(Integer, primary_key=True)
    name            = Column(String(250), nullable=False)
    diameter        = Column(Integer(), nullable=False)
    rotation_period	= Column(Integer(), nullable=False)
    orbital_period	= Column(Integer(), nullable=False)
    gravity	        = Column(String(20), nullable=False)
    population	    = Column(Integer(), nullable=False)
    climate	        = Column(String(30), nullable=False)
    terrain         = Column(String(10), nullable=False)
    surface_water   = Column(Integer(), nullable=False)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(250), nullable=False)
    model                   = Column(String(50), nullable=False)
    vehicle_class	        = Column(String(50), nullable=False)
    manufacturer	        = Column(String(50), nullable=False)
    cost_in_credits	        = Column(Integer(), nullable=False)
    length	                = Column(Integer(), nullable=False)
    crew	                = Column(Integer(), nullable=False)
    max_atmosphering_speed  = Column(Integer(), nullable=False)
    cargo_capacity          = Column(Integer(), nullable=False)
    consumables             = Column(String(20), nullable=False)
    films                   = Column(Integer(), nullable=False)
    pilots                  = Column(Integer(), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(250), nullable=False)
    model                   = Column(String(50), nullable=False)
    starship_class	        = Column(String(50), nullable=False)
    manufacturer	        = Column(String(50), nullable=False)
    cost_in_credits	        = Column(Integer(), nullable=False)
    length	                = Column(Integer(), nullable=False)
    crew	                = Column(Integer(), nullable=False)
    passengers              = Column(Integer(), nullable=False)
    max_atmosphering_speed  = Column(Integer(), nullable=False)
    cargo_capacity          = Column(Integer(), nullable=False)
    consumables             = Column(String(30), nullable=False)
    films                   = Column(Integer(), nullable=False)
    pilots                  = Column(Integer(), nullable=False)
    hyperdrive_rating       = Column(Integer(), nullable=False)
    MGLT                    = Column(Integer(), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id            = Column(Integer, primary_key=True)
    name          = Column(String(250))
    last_name     = Column(String(250))
    email         = Column(String(50))
    password      = Column(String(50))
    Fech_subscrip = Column(String(50))
    Activo        = Column(String(1))
    

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id            = Column(Integer, primary_key=True)
    personaje_id  = Column(Integer, ForeignKey('personajes.id'))
    vehiculo_id   = Column(Integer, ForeignKey('vehiculos.id'))
    planeta_id    = Column(Integer, ForeignKey('planetas.id'))
    usuario_id    = Column(Integer, ForeignKey('usuario.id'))
    starships_id  = Column(Integer, ForeignKey('starships.id'))
    usuario       = relationship(Usuario)
    person        = relationship(Personajes)
    Vehi          = relationship(Vehiculos)
    plane         = relationship(Planetas)
    star          = relationship(Starships)


  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
