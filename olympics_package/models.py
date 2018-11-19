from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy.sql import *


Base = declarative_base()

from olympics_package import db

class Country(db.Model):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.String)
    olympic_games = db.relationship('OlympicGame', back_populates='country')
    medals= db.relationship('Medal', back_populates='country')

class OlympicGame(db.Model):
    __tablename__='olympic_games'
    id = db.Column(db.Integer, primary_key=True)
    year= db.Column(db.Integer)
    city= db.Column (db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country', back_populates = 'olympic_games')
    medals= db.relationship('Medal', back_populates='olympic_games')


class Sport(db.Model):
    __tablename__='sports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    events = db.relationship('Event', back_populates='sports')
    medals= db.relationship('Medal', secondary='events', back_populates='sport')


class Event(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    # sports.id     which sports its assocaited with
    sports_id= db.Column(db.Integer, db.ForeignKey('sports.id'))
    sports = db.relationship('Sport', back_populates='events')
    medals= db.relationship('Medal', back_populates='events')

class Medal(db.Model):
    __tablename__ = 'medals'
    id = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String) #gold,silver,bronze
    score = db.Column(db.Integer)
#country.id    which country
    country_id= db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country', back_populates='medals')
  #olympic_id    which olympic game
    olympic_games_id= db.Column(db.Integer, db.ForeignKey('olympic_games.id'))
    olympic_games= db.relationship('OlympicGame', back_populates='medals')
  #events.id    which ebents have these Medals
    events_id= db.Column(db.Integer, db.ForeignKey('events.id'))
    events = db.relationship('Event', back_populates='medals')
    sport = db.relationship('Sport', secondary = 'events', back_populates = 'medals')
    sport = db.relationship('Sport', secondary = 'events', back_populates = 'medals')

db.create_all()
