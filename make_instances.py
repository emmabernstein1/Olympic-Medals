from functions import *
from models import *

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy.sql import *
from bs4 import BeautifulSoup
import requests
import time

#created the engine with the session to do the combining
engine = create_engine('sqlite:///olympics.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session= Session()

#instance to make the countries list populate
def make_country_instances():
    ussr = Country(name = 'USSR', code = 'USSR')
    ioa = Country(name = 'Independent Olympic Athletes', code = 'IOA')
    scg = Country(name = 'Serbia and Montenegro', code = 'SCG')
    yug = Country(name = 'Yugoslavia', code = 'YUG')
    eun = Country(name = 'Unified Team', code = 'EUN')
    tch = Country(name = 'Czechoslovakia', code = 'TCH')
    iop = Country(name = 'Independent Olympic Participants', code = 'IOP')
    urs = Country(name = 'Soviet Union', code = 'URS')
    gdr = Country(name = 'East Germany', code = 'GDR')
    frg = Country(name = 'West Germany', code = 'FRG')
    aho = Counrty(name = 'Netherlands Antilles', code = 'AHO')
    session.add_all([ussr, ioa, scg, yug, eun, tch, iop, urs, gdr, frg, aho])
    session.commit()
    for i in range(len(country_to_tag)):
        country_instance = Country(name= country_to_tag[i][0], code = country_to_tag[i][1])
        session.add(country_instance)
        session.commit()



#instance to make the games populate populate in a table while realting to the country with country idea
def create_game_instance():
    for game in game_info:
        game_instance = OlympicGame(year = game[1], city = game[2])
        game_instance.country_id = [country.id for country in session.query(Country).all() if game[0] == country.name][0]
        game_instance.countries = [country for country in session.query(Country).all() if game[0] == country.name][0]
        session.add(game_instance)
        session.commit()
        # session.query(Country).find(country.id for country in Country where list[i][0] == country.name)

def create_sport_instances():        #creating sport instances from all_sports, which is a list of all of the sport names
    for sport in all_sports:
        sport_instance = Sport(name = sport)
        session.add(sport_instance)
        session.commit()

def sport_and_event():
    for url in game_sport_urls:
        sport_event_request = requests.get(url)
        sport_event_html = sport_event_request.text
        sport_event_soup = BeautifulSoup(sport_event_html)
        sport_name = sport_event_soup.find('div', {'id': 'wrapper'}).find('h1').text
             #getting name of sport associated with url
        time.sleep(1)
        if sport_name != '404 - Page not found  ':

            if len([sport for sport in session.query(Sport).all() if sport.name == sport_name]) < 1:
                sport_instance = Sport(name = sport_name)
                url_sport_object = sport_instance
                url_sport_id = sport_instance.id
                session.add(sport_instance)
                session.commit()
            else:
                url_sport_object = [sport for sport in session.query(Sport).all() if sport.name == sport_name][0]
                 #getting the associated sport object
                url_sport_id = [sport.id for sport in session.query(Sport).all() if sport.name == sport_name][0]
                 #getting associated sport object's id

            events = sport_event_soup.findAll('section', {'class': 'event-box'})
            all_events = []

            for event_box in events:
                all_events.append(event_box.findNext('a').text[19:][:-14])
                     #get list of all events in this url

            for single_event in all_events:
                if len([event for event in session.query(Event).all() if event.name == single_event]) < 1:
                         #check if the event is already an instance of the Event class. if not, continue
                    event_instance = Event(name = single_event, sports_id = url_sport_id)
                         #create instance. set event name. set sports_id equal to the id associated with this url's sport -- found above
                    event_instance.sports = url_sport_object
                         #creating the relationship between event and the sports object
                    session.add(event_instance)
                    session.commit()



def medal_scraper():
    for url in game_sport_urls:
        olympics_request = requests.get(url)
        olympics_html = olympics_request.text
        olympics_soup = BeautifulSoup(olympics_html)
        time.sleep(1)

        sport = olympics_soup.find('div', {'id': 'wrapper'}).find('h1').text

        if sport != '404 - Page not found  ':
            url_split = url.split('/')   ##split url on '-'
            olympic_year = url_split[len(url_split)-2][-4:]  ##grab last element of list and grab first 4 elements, corresponding to the year of the game
            olympic_year_int = int(olympic_year)

            all_events = []
            all_medalist_countries = []
            all_medal_types = []
            all_scores = []

            events = olympics_soup.findAll('section', {'class': 'event-box'})

            for event_box in events:
                all_events.append(event_box.findNext('a').text[19:][:-14])

            for event_box in events:
                event_medalists = event_box.findAll('div', {'class': 'text-box'}) #gets list of three elements; each represents the name/country of the medalist
                event_countries = []
                for name in event_medalists:
                    try:
                        country = name.find('span').text
                    except:
                        country = name.find('strong', {'class':'name'}).text
                    event_countries.append(country)
                all_medalist_countries.append(event_countries)

            for event_box in events:
                event_results = event_box.findAll('td', {'class':'col1'})            #get list of length three, each element representing a score from that event
                event_scores = []
                for result in event_results:
                    try:
                        score = result.find('span', {'class':'txt'}).text   #get score if score available
                    except:
                        score = None
                    event_scores.append(score)
                all_scores.append(event_scores)    ##maybe change scores to float object. update in class

            for event_box in events:
                event_results = event_box.findAll('td', {'class':'col1'})
                event_medal_types = []

                for result in event_results:  #iterate through the different events
                    type = result.find('div').text[1:2]       #get type of medal
                    event_medal_types.append(type)
                all_medal_types.append(event_medal_types)

            for i in range(len(all_events)):

                for j in range(len(all_medal_types[i])):
                    if url == 'https://www.olympic.org/rio-2016/badminton' and i == 1 and j == 1:
                        country_code = 'MAS'
                        medal_instance = Medal(type = 'S', score = None)

                    else:
                        try:
                            country_code = all_medalist_countries[i][j]
                            medal_instance = Medal(type = all_medal_types[i][j], score = all_scores[i][j])

                        except:
                            country_code = 'GBR'
                            medal_instance = Medal(type = 'B', score = None)
                             #create a Medal instance, define the type and score


                    if len([country for country in session.query(Country).all() if country.code == country_code]) < 1:
                        country_instance = Country(name = None, code = country_code)
                        medal_instance.country = country_instance
                        session.add(country_instance)
                        session.commit()

                    else:
                        medal_instance.country = [country for country in session.query(Country).all() if country.code == country_code][0]

                         #associate medal instance with the country's object
                        medal_instance.country_id = [country.id for country in session.query(Country).all() if country.code == country_code][0]
                             #set medal's country id
                    medal_instance.olympic_games = [game for game in session.query(OlympicGame).all() if game.year == olympic_year_int][0]
                         #associate medal with the olympic game's object
                    medal_instance.olympic_games_id = [game.id for game in session.query(OlympicGame).all() if game.year == olympic_year_int][0]
                         #set medal's olympic game id
                    medal_instance.events = [event for event in session.query(Event).all() if event.name == all_events[i]][0]
                         #associate medal with event object
                    medal_instance.events_id = [event.id for event in session.query(Event).all() if event.name == all_events[i]][0]
                         #set medal's event id
                    session.add(medal_instance)
                    session.commit()
