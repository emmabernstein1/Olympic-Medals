different sport:
water-polo
volleyball
tennis
swimming
synchronized-swimming
shooting
sailing
rugby
rowing
hockey
gymnastics-rhythmic
gymnastics-artistic
golf
football
fencing
diving
cycling-track
cycling-road
cycling-mountain

import requests

foo_request = requests.get('https://www.olympic.org/london-2012/foo')
foo_html = foo_request.text
from bs4 import BeautifulSoup
foo_soup = BeautifulSoup(foo_html)

foo_sport = foo_soup.findAll('section', {'class':'banner-box'})[0].findAll('h1')[0].text
#get the name of the sport from the sport's webpage

foo_events = foo_soup.findAll('section', {'class': 'event-box'})

foo_events[0].findNext('a').text[19:][:-14]
#gets the events, iterate through

foo_scores = foo_events.findAll('span', {'class':'txt'})
foo_names = foo_events.findAll('strong', {'class':'name'})

# def get_players_scores():
#     foo_names_text=[]
#     for name in foo_names:
#         names1_text.append(name.text)
#
#     foo_scores_text=[]
#     for score in foo_scores:
#         foo_scores_text.append(score.text)
#
#     return(set(zip(names1_text, scores1_text)))


foo_names_text=[]
for name in foo_names:
    names1_text.append(name.text)
#list of player names given sport

foo_scores_text=[]
for score in foo_scores:
    foo_scores_text.append(score.text)
#list of player scores given sport (corresponds with foo_names_text)

player_scores = set(zip(names1_text, scores1_text))
#list of player and scores as a tuple





#get beautiful soup of player's info
player_request = requests.get('https://www.olympic.org/player')
player_html = player_request.text
player_soup = BeautifulSoup(player_html)

##looking at each player's information
mich_soup.findAll('div', {'class': 'frame'})[0].findAll('strong', {'class': 'title'})
#gives the titles

mich_soup.findAll('div', {'class': 'frame'})[0].findAll('a')[0].text
#finding the information that matches




class Country(Base):
    __tablename__='countries'

    id = Column(Integer, primary_key = True)
    name = Column(Text)


for i in countries:
