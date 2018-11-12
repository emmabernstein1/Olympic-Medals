from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Medals(Base):
    __tablename__= 'medals'
    id = Column(Integer, primary_key=True)
    type= Column(Text) #gold,silver,bronze
 #athlete.id   which athlete
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    athlete = relationship("Athlete", back_populates='medals')
#country.id    which country
    country_id= Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', back_populates='medals')
  #olympic_id    which olympic game
    olympic_games_id= Column(Integer, ForeignKey('olympic_games.id'))
    olympic_games= relationship('OlympicGame', back_populates='medals')
  #events.id    which ebents have these Medals
    events_id= Column(Integer, ForeignKey('events.id'))
    events = relationship('Events', back_populates='events')



class Athlete(Base):
    __tablename__= 'athletes'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    dob = Column(Text)                 #check wheter string or type

     #country.id
    country_id= Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', back_populates='athletes')

     # medals backref relationship
    medals_id= Column(Integer, ForeignKey('medals.id'))
    medals = relationship('Medals', back_populates='athlete')

     #backref olympic games
    olympic_games_id= Column(Integer, ForeignKey('olympic_games.id'))
    olympic_games = relationship('OlympicGame', back_populates='athletes')


class Country(Base):
    __tablename__= 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    olympic_games_id= Column(Integer, ForeignKey('olympic_games.id'))
    olympic_games = relationship('OlympicGame', back_populates= 'country')
    #backref athletes
    athletes_id= Column(Integer, ForeignKey('athletes.id'))
    athletes = relationship('Athlete', back_populates= 'country')

class Events(Base):
    __tablename__='events'
    id = Column(Integer, primary_key=True)
    # sports.id     which sports its assocaited with
    sports_id= Column(Integer, ForeignKey('sports.id'))
    sports = relationship('Sport', back_populates='events')
     # backref to Medals
    medals_id= Column(Integer, ForeignKey('medals.id'))
    medals = relationship('Medals', back_populates='medals')

class Sport(Base):
    __tablename__='sports'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    #backref to evets
    events_id= Column(Integer, ForeignKey('events.id'))
    events = relationship('Events', back_populates='sports')

class OlympicGame(Base):
    __tablename__='olympic_games'
    id = Column(Integer, primary_key=True)
    year= Column(Integer)
    city= Column (Text)
#country.id
    country_id= Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', back_populates='olympic_games')



engine = create_engine('sqlite:///olympics.db')
Base.metadata.create_all(engine)
