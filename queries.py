# from final_testing import *
from olympics_package.models import *
from olympics_package import db
import numpy as np



def all_countries():
    return Country.query.all()

all_countries = all_countries()

total_countries=[]
for country in all_countries:
    total_countries.append(country.name)

def all_games():
    return OlympicGame.query.all()

all_games = all_games()

def games_city_year():
    games = ['{}, {}'.format(game.city, game.year) for game in all_games]
    return games[::-1]  #reverse list

ordered_games = games_city_year()



def all_sports():
    return Sport.query.all()
total_sports=[]
for sport in all_sports():
    total_sports.append(sport.name)
all_sports = all_sports()
# def total_sports = []
# for sport in all_sports():
#     total_sports.append(sport.name)



# def countries_with_many_medals():
#     return [country.name for country in Country.query.all() if len(country.medals) > 10]
# SELECT countries.name, count(medals.id) FROM medals JOIN countries ON medals.country_id = countries.id WHERE country_id = countries.id GROUP BY countries.id ORDER BY count(medals.id) DESC

# def country_medals_sorted():
#     all_medals_by_country = []
#     for country in all_countries:
#         country_medals = total_country_medals(country)
#         all_medals_by_country.append(country_medals)
#     return all_medals_by_country

# country_medals = country_medals_sorted()



#return a list of a country's medals
def country_medals(country):
    return [medal for medal in Medal.query.all() if medal.country == country]

#return a list of an olympic game's medals
def total_game_medals(game):
    return [medal for medal in Medal.query.all() if medal.olympic_games.city == game.city]

#return a list of a country's medals by sport
def country_medals_sport(country):
    all = []
    country_sports = list(set([medal.sport for medal in country.medals]))
    for sport in country_sports:
        sport_medals = [medal for medal in Medal.query.all() if medal.events.sports == sport and medal.country == country]
        all.append(sport_medals)
    return all

#lists of medals for each country from the specified olympic game
def game_medals_by_country(game):
    game_medals_by_country = []
    game_medals = total_game_medals(game)
    for country in all_countries:
        game_medals_by_country.append([medal for medal in game_medals if medal.country.name == country.name])
    return game_medals_by_country
        ##returns a list of lists





##COUNTRY MEDAL AVERAGES:

#gets the average number of medals per country for a specified olympic game. Automatically gets the mean and filters for only countries with at least one medal
#to get the median, change to 'mean=False'
#to get unfiltered medals, change to 'filter_nonmedals=False'
def game_medal_average(game, mean=True, filter_nonmedals=True):
    list_of_medals = game_medals_by_country(game)
    all_medal_counts = []
    for country in list_of_medals:
        if filter_nonmedals==False:
            if len(country) > 0:     #filter out countries with no medals
                all_medal_counts.append(len(country))     #appending the number of medals associated with the country
        else:
            all_medal_counts.append(len(country))     #appending the number of medals associated with the country
    if mean==False:
        return np.median(all_medal_counts)     #return the median if mean set to false
    else:
        return np.mean(all_medal_counts)


#gets lists associating each game with their medal average per country
#to get the median, change to 'mean=False'
#to get unfiltered medals, change to 'filter_nonmedals=False'
def medal_averages_all_games(mean=True, filter_nonmedals=True):
    all_averages = []
    for game in all_games:
        game_average = game_medal_average(game)
        all_averages.append(['{}, {}'.format(game.city, game.year), game_average])
    return all_averages



#gets number of medals for each olympic game given specified country
def country_medals_by_game(country):
    country_medals = [country1.medals for country1 in Country.query.all() if country1.name == country][0]
    medals_by_game = []
    for game in all_games:
        medals = [medal for medal in country_medals if medal.olympic_games.city == game.city]
        medals_by_game.append(['{}, {}'.format(game.city, game.year), len(medals)])
    return medals_by_game

def country_game_medals(type):
    medals_count = [country_medals_by_game(type)[9][1], country_medals_by_game(type)[8][1], country_medals_by_game(type)[7][1], country_medals_by_game(type)[6][1], country_medals_by_game(type)[5][1], country_medals_by_game(type)[4][1], country_medals_by_game(type)[3][1], country_medals_by_game(type)[2][1], country_medals_by_game(type)[1][1], country_medals_by_game(type)[0][1]]
    return medals_count

def all_game_medals():
    medals_count = [medal_averages_all_games()[9][1], medal_averages_all_games()[8][1], medal_averages_all_games()[7][1], medal_averages_all_games()[6][1], medal_averages_all_games()[5][1], medal_averages_all_games()[4][1], medal_averages_all_games()[3][1], medal_averages_all_games()[2][1], medal_averages_all_games()[1][1], medal_averages_all_games()[0][1]]
    return medals_count



# def country_medal_count():
#     all = []
#     for country in total_countries:
#         all.append({'{}'.format(country): country_game_medals(country)})
#     return all
# all = country_medal_count()
#
all = [{'USSR': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Independent Olympic Athletes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 2]}, {'Serbia and Montenegro': [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}, {'Yugoslavia': [9, 18, 12, 0, 2, 2, 0, 0, 0, 0]}, {'Unified Team': [0, 0, 0, 112, 0, 0, 0, 0, 0, 0]}, {'Czechoslovakia': [14, 0, 7, 7, 0, 0, 0, 0, 0, 0]}, {'Independent Olympic Participants': [0, 0, 0, 3, 0, 0, 0, 0, 0, 0]}, {'Soviet Union': [195, 0, 133, 0, 0, 0, 0, 0, 0, 0]}, {'East Germany': [126, 0, 102, 0, 0, 0, 0, 0, 0, 0]}, {'West Germany': [0, 59, 39, 0, 0, 0, 0, 0, 0, 0]}, {'Netherlands Antilles': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {'Afghanistan': [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]}, {'Albania': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Algeria': [0, 2, 0, 2, 2, 4, 0, 2, 1, 2]}, {'American Samoa': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Andorra': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Angola': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Antigua and Barbuda': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Argentina': [0, 0, 2, 1, 0, 0, 6, 6, 4, 4]}, {'Armenia': [0, 0, 0, 0, 1, 1, 0, 5, 0, 2]}, {'Aruba': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Australia': [9, 24, 13, 27, 10, 42, 47, 45, 24, 28]}, {'Austria': [4, 3, 1, 2, 3, 1, 7, 3, 0, 1]}, {'Azerbaijan': [0, 0, 0, 0, 1, 2, 5, 6, 3, 9]}, {'Bahamas': [0, 0, 0, 1, 1, 3, 2, 2, 1, 2]}, {'Bahrain': [0, 0, 0, 0, 0, 0, 0, 0, 1, 2]}, {'Bangladesh': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Barbados': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {'Belarus': [0, 0, 0, 0, 10, 14, 13, 13, 8, 6]}, {'Belgium': [1, 4, 2, 3, 1, 3, 3, 2, 1, 6]}, {'Belize': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Benin': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Bermuda': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Bhutan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Bolivia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Bosnia and Herzegovina': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Botswana': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {'Brazil': [4, 8, 5, 3, 1, 5, 10, 16, 16, 19]}, {'Brunei Darussalam': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Bulgaria': [41, 0, 38, 16, 10, 10, 12, 5, 2, 2]}, {'Burkina Faso': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Burundi': [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]}, {'Cambodia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Cameroon': [0, 1, 0, 0, 0, 0, 1, 1, 0, 0]}, {'Canada': [0, 43, 8, 16, 5, 8, 12, 20, 14, 20]}, {'Cape Verde': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Cayman Islands': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Central African Republic': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Chad': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Chile': [0, 0, 1, 0, 0, 0, 3, 1, 0, 0]}, {'Chinese Taipei': [0, 1, 0, 0, 1, 5, 5, 4, 2, 3]}, {'Colombia': [0, 1, 1, 1, 0, 2, 2, 3, 7, 8]}, {'Comoros': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Congo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Cook Islands': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Costa Rica': [0, 0, 1, 0, 0, 2, 0, 0, 0, 0]}, {"Côte d'Ivoire": [0, 1, 0, 0, 0, 0, 0, 0, 0, 2]}, {'Croatia': [0, 0, 0, 3, 1, 1, 5, 5, 5, 10]}, {'Cuba': [20, 0, 0, 30, 8, 9, 26, 27, 12, 8]}, {'Cyprus': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {'Czech Republic': [0, 0, 0, 0, 4, 6, 9, 6, 11, 10]}, {"Democratic People's Republic of Korea": [5, 0, 0, 9, 4, 1, 5, 5, 5, 7]}, {'Democratic Republic of the Congo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Denmark': [5, 6, 4, 6, 1, 4, 8, 7, 8, 14]}, {'Djibouti': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {'Dominican Republic': [0, 1, 0, 0, 0, 0, 1, 2, 2, 1]}, {'Dominique': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Ecuador': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]}, {'Egypt': [0, 1, 0, 0, 0, 0, 5, 1, 2, 3]}, {'El Salvador': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Equatorial Guinea': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Eritrea': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]}, {'Estonia': [0, 0, 0, 2, 0, 1, 3, 2, 1, 1]}, {'Eswatini': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Ethiopia': [4, 0, 0, 3, 3, 8, 7, 7, 8, 8]}, {'Federated States of Micronesia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Fiji': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}, {'Finland': [8, 12, 2, 5, 2, 2, 2, 4, 2, 1]}, {'France': [14, 28, 16, 29, 6, 16, 33, 43, 28, 39]}, {'Gabon': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {'Gambia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Georgia': [0, 0, 0, 0, 1, 2, 4, 6, 1, 4]}, {'Germany': [0, 0, 0, 82, 27, 33, 48, 40, 40, 35]}, {'Ghana': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]}, {'Great Britain': [21, 37, 24, 20, 8, 17, 31, 48, 54, 64]}, {'Greece': [3, 2, 1, 2, 7, 12, 16, 3, 2, 6]}, {'Grenada': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]}, {'Guam': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Guatemala': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {'Guinea': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Guinea-Bissau': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Guyana': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Haiti': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Honduras': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Hong Kong, China': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]}, {'Hungary': [32, 0, 23, 30, 4, 14, 17, 10, 13, 15]}, {'Iceland': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]}, {'India': [1, 0, 0, 0, 0, 1, 1, 3, 2, 1]}, {'Indonesia': [0, 0, 1, 5, 3, 6, 4, 5, 2, 3]}, {'Iraq': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Ireland': [2, 1, 0, 2, 1, 1, 0, 3, 5, 2]}, {'Islamic Republic of Iran': [0, 0, 1, 3, 3, 2, 6, 2, 6, 3]}, {'Israel': [0, 0, 0, 2, 0, 1, 2, 1, 0, 2]}, {'Italy': [15, 32, 14, 19, 9, 19, 32, 27, 24, 27]}, {'Jamaica': [3, 3, 2, 4, 6, 9, 5, 10, 12, 11]}, {'Japan': [0, 30, 12, 19, 2, 6, 32, 23, 24, 32]}, {'Jordan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}, {'Kazakhstan': [0, 0, 0, 0, 6, 4, 8, 8, 6, 15]}, {'Kenya': [0, 3, 8, 8, 8, 7, 7, 14, 13, 13]}, {'Kiribati': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Kosovo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}, {'Kuwait': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {'Kyrgyzstan': [0, 0, 0, 0, 0, 0, 0, 3, 0, 0]}, {"Lao People's Democratic Republic": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Latvia': [0, 0, 0, 3, 0, 2, 3, 3, 2, 0]}, {'Lebanon': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Lesotho': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Liberia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Libya': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Liechtenstein': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Lithuania': [0, 0, 0, 2, 0, 3, 3, 5, 5, 4]}, {'Luxembourg': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Madagascar': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Malawi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Malaysia': [0, 0, 0, 1, 2, 0, 0, 1, 2, 5]}, {'Maldives': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Mali': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Malta': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Marshall Islands': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Mauritania': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Mauritius': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]}, {'Mexico': [4, 6, 2, 1, 1, 4, 4, 3, 7, 5]}, {'Monaco': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Mongolia': [4, 0, 1, 2, 0, 0, 1, 4, 4, 2]}, {'Montenegro': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {'Morocco': [0, 2, 2, 3, 2, 5, 3, 2, 1, 1]}, {'Mozambique': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]}, {'Myanmar': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Namibia': [0, 0, 0, 2, 2, 0, 0, 0, 0, 0]}, {'Nauru': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Nepal': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Netherlands': [3, 13, 9, 15, 5, 18, 21, 16, 13, 19]}, {'New Zealand': [0, 11, 13, 10, 0, 1, 5, 9, 12, 18]}, {'Nicaragua': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Niger': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}, {'Nigeria': [0, 2, 0, 4, 4, 4, 2, 4, 0, 1]}, {'Norway': [0, 3, 5, 7, 2, 7, 6, 9, 4, 3]}, {'Oman': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Pakistan': [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]}, {'Palau': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Palestine': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Panama': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]}, {'Papua New Guinea': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Paraguay': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]}, {"People's Republic of China": [0, 32, 28, 54, 33, 51, 63, 92, 74, 66]}, {'Peru': [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]}, {'Philippines': [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]}, {'Poland': [32, 0, 16, 19, 6, 11, 10, 10, 7, 10]}, {'Portugal': [0, 3, 1, 0, 1, 1, 3, 2, 1, 1]}, {'Puerto Rico': [0, 2, 0, 1, 0, 0, 0, 0, 1, 1]}, {'Qatar': [0, 0, 0, 1, 0, 1, 0, 0, 1, 1]}, {'Republic of Korea': [0, 19, 33, 29, 11, 11, 30, 31, 24, 20]}, {'Republic of Moldova': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]}, {'Romania': [25, 53, 24, 18, 12, 20, 15, 8, 8, 3]}, {'Russian Federation ': [0, 0, 0, 0, 35, 62, 86, 57, 59, 45]}, {'Rwanda': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Saint Kitts and Nevis': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Saint Lucia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Samoa (until 1996 Western Samoa)': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'San Marino': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Sao Tome and Principe': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Saudi Arabia': [0, 0, 0, 0, 0, 2, 0, 0, 0, 0]}, {'Senegal': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {'Serbia': [0, 0, 0, 0, 0, 0, 0, 3, 4, 7]}, {'Seychelles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Sierra Leone': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Singapore': [0, 0, 0, 0, 0, 0, 0, 1, 2, 1]}, {'Slovakia': [0, 0, 0, 0, 0, 5, 6, 6, 3, 4]}, {'Slovenia': [0, 0, 0, 2, 1, 2, 4, 5, 3, 4]}, {'Solomon Islands': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Somalia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'South Africa': [0, 0, 0, 2, 3, 5, 6, 1, 4, 10]}, {'South Sudan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Spain': [6, 5, 4, 22, 2, 6, 19, 16, 10, 17]}, {'Sri Lanka': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {'St Vincent and the Grenadines': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Sudan': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]}, {'Suriname': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]}, {'Sweden': [12, 19, 9, 12, 2, 9, 7, 5, 3, 8]}, {'Switzerland': [2, 8, 4, 1, 1, 4, 5, 7, 2, 7]}, {'Syrian Arab Republic': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]}, {'Tajikistan': [0, 0, 0, 0, 0, 0, 0, 2, 1, 1]}, {'Thailand': [0, 1, 1, 1, 0, 1, 8, 5, 4, 6]}, {'The Former Yugoslav Republic of Macedonia': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Timor-Leste': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Togo': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]}, {'Tonga': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Trinidad and Tobago': [0, 0, 0, 0, 2, 2, 1, 2, 4, 1]}, {'Tunisia': [0, 0, 0, 0, 0, 0, 0, 1, 2, 2]}, {'Turkey': [0, 3, 2, 6, 4, 1, 11, 7, 2, 3]}, {'Turkmenistan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Tuvalu': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Uganda': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]}, {'Ukraine': [0, 0, 0, 0, 13, 12, 22, 22, 18, 10]}, {'United Arab Emirates': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]}, {'United Republic of Tanzania': [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'United States of America': [0, 174, 90, 106, 52, 65, 95, 108, 78, 115]}, {'Uruguay': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {'Uzbekistan': [0, 0, 0, 0, 1, 0, 5, 4, 2, 10]}, {'Vanuatu': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Venezuela': [1, 3, 0, 0, 0, 0, 2, 1, 1, 3]}, {'Vietnam': [0, 0, 0, 0, 0, 0, 0, 1, 0, 2]}, {'Virgin Islands, British': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Virgin Islands, US': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {'Yemen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'Zambia': [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]}, {'Zimbabwe': [1, 0, 0, 0, 0, 0, 3, 4, 0, 0]}]

#
def get_country_medal_count(type):
    counts = []
    keys = list(map(lambda key: list(key.keys()), all))
    key_index = keys.index(['{}'.format(type)])
    key_values = list(all[key_index].values())
    return key_values[0]
#     for dictionary in all:
#         keys.append(dictionary.keys())
#     key_index = keys.index(type)
#
#     for key in all:
#         if key.keys() == type:
#             counts.append(key.values())
#     return counts
#     for dictionary in all:
#         return
# for dictionary in all:
#     keys.append(dictionary.keys())

# country_medals = [country.medals for country in Country.query.all() if country.name == country]
# for game in all_games:
#     medals =




##get events for given sport
def sport_events(sport):
    return [event.name for event in Event.query.all() if event.sports.name == sport]

def sport_event_medals(event):
    all_event_medals = db.session.query(Medal).join(Event).filter(Medal.events == event).all()
    for medal in all_event_medals:
        for game in all_games:
            game_medals = [medal for medal in Medal.query.all() if medal.olympic_games == game]
        all_event_medals.append(['{}'.format(game), game_medals])
    return all_event_medals






##gives list of lists. first element of each sublist points to the olympic game. second element is a list of all of the medals associated with that game and the event
# def event_medals(event):
#     all_event_medals = []
#     medals = [events.medals for events in Event.query.all() if events == event][0]
#     event_games = list(set([medal.olympic_games for medal in medals]))  #get unique list of olympic games that the
#     for game in all_games:
#         all_medals = [[medal.type, medal.score, medal.country.code] for medal in medals if medal.olympic_games == game]
#         medals_by_type = [medal for medal in all_medals if medal.] #get medal type, score and country
#         all_event_medals.append(['{}, {}'.format(game.city, game.year), all_medals])
#     return all_event_medals

# def event_medals(event):
#     scores = []
#     text = []
#     medals = [events.medals for events in Event.query.all() if events == event][0]
#     for game in all_games:
#         game_medals = [medal for medal in medals if medal.olympic_games == game]
#         # game_medal_types = list(set([medal.type for medal in game_medals]))
#         for type in ['G', 'S', 'B']:
#             type_medals = [medal for medal in game_medals if medal.type == type]
#             if len(type_medals) > 1:
#                 foo = '{}: {}, {}'.format(type, type_medals[0].country, type_medals[1].country.name)
#                 text.append(foo)
#                 scores.append(medals_score[0])
#             else:
#                 foo = '{}: {}'.format(type, type_medals[0].country.name)
#                 text.append(foo)
#                 scores.append(type_medals[0].score)
#     return [scores, text]

test_event = all_sports[2].events[0]
# test = event_medals(test_event)

# selector = test_event
# selector = '400m men'

def event_medals(selector):
    all_medals = []
    medals = [events.medals for events in Event.query.all() if events.name == selector][0]
    for game in all_games:
        game_medals = [medal for medal in medals if medal.olympic_games.city == game.city]
        scores = []
        text = []
        if len(game_medals) < 1:
            scores.append([None, None, None])
            text.append([None, None, None])
        for type in ['G', 'S', 'B']:
            type_medals = [medal for medal in game_medals if medal.type == type]
            if len(type_medals) == 0:
                text.append(None)
                scores.append(None)
            elif len(type_medals) > 1:
                foo = '{}: {}, {}'.format(type, type_medals[0].country.code, type_medals[1].country.code)
                text.append(foo)
                scores.append(type_medals[0].score)
            else:
                foo = '{}: {}'.format(type, type_medals[0].country.code)
                text.append(foo)
                scores.append(type_medals[0].score)
        all_medals.append([scores, text])
    return all_medals

def y_gold(selector):
    y = [event_medals(selector)[0][0][0],event_medals(selector)[1][0][0],event_medals(selector)[2][0][0],event_medals(selector)[3][0][0],event_medals(selector)[4][0][0],event_medals(selector)[5][0][0],event_medals(selector)[6][0][0],event_medals(selector)[7][0][0],event_medals(selector)[8][0][0],event_medals(selector)[9][0][0]]
    return y[::-1]
# y_gold = y_gold(selector)

def text_gold(selector):
    text = [event_medals(selector)[0][1][0],event_medals(selector)[1][1][0],event_medals(selector)[2][1][0],event_medals(selector)[3][1][0],event_medals(selector)[4][1][0],event_medals(selector)[5][1][0],event_medals(selector)[6][1][0],event_medals(selector)[7][1][0],event_medals(selector)[8][1][0],event_medals(selector)[9][1][0]]
    return text[::-1]
# text_gold = text_gold(selector)

def y_silver(selector):
    y = [event_medals(selector)[0][0][1],event_medals(selector)[1][0][1],event_medals(selector)[2][0][1],event_medals(selector)[3][0][1],event_medals(selector)[4][0][1],event_medals(selector)[5][0][1],event_medals(selector)[6][0][1],event_medals(selector)[7][0][1],event_medals(selector)[8][0][1],event_medals(selector)[9][0][1]]
    return y[::-1]
# y_silver = y_silver(selector)

def text_silver(selector):
    text = [event_medals(selector)[0][1][1],event_medals(selector)[1][1][1],event_medals(selector)[2][1][1],event_medals(selector)[3][1][1],event_medals(selector)[4][1][1],event_medals(selector)[5][1][1],event_medals(selector)[6][1][1],event_medals(selector)[7][1][1],event_medals(selector)[8][1][1],event_medals(selector)[9][1][1]]
    return text[::-1]
# text_silver = text_silver(selector)

def y_bronze(selector):
    y = [event_medals(selector)[0][0][2],event_medals(selector)[1][0][2],event_medals(selector)[2][0][2],event_medals(selector)[3][0][2],event_medals(selector)[4][0][2],event_medals(selector)[5][0][2],event_medals(selector)[6][0][2],event_medals(selector)[7][0][2],event_medals(selector)[8][0][2],event_medals(selector)[9][0][2]]
    return y[::-1]
# y_bronze = y_bronze(selector)

def text_bronze(selector):
    text = [event_medals(selector)[0][1][2],event_medals(selector)[1][1][2],event_medals(selector)[2][1][2],event_medals(selector)[3][1][2],event_medals(selector)[4][1][2],event_medals(selector)[5][1][2],event_medals(selector)[6][1][2],event_medals(selector)[7][1][2],event_medals(selector)[8][1][2],event_medals(selector)[9][1][2]]
    return text[::-1]
# text_bronze = text_bronze(selector)

        #
        # type_medals = [[medal.score, medal.country.code] for medal in medals if medal.type == type order by medal.olympic_games.year]
        #
        # all_medals.append(type_medals)
#
# def test_medals(event):
#     games = ordered_games
#     medal_scores =
#
#     for game in all_games:
#         all_game_medals = [medal.type, medal.score, medal.country.code] for medal in medals if medal.olympic_games == game]
#         medal_types = list(set([medal.type for medal in medals]))  #grabs if there are gold, silver or bronze medals
#         for type in medal_type:
#             type_medals = [[medal.score, medal.country] for medal in all_game_medals if medal.type == type]
#         for type in ['G', 'S', 'B']:



def country_total_medal_count():
    country_count = []
    for dictionary in all:
        values = list(dictionary.values())[0]
        total_val = sum(values)
        country_count.append({'{}'.format(list(dictionary.keys())[0]): total_val})
    return sorted(country_count, key=lambda d: list(d.values())[0], reverse=True)[:10]

top_10 = [{'United States of America': 883}, {"People's Republic of China": 493}, {'Russian Federation ': 344}, {'Soviet Union': 328}, {'Great Britain': 324}, {'Germany': 305}, {'Australia': 269}, {'France': 252}, {'East Germany': 228}, {'Italy': 218}]
def get_10_countries():
    return list(map(lambda dictionary: list(dictionary.keys())[0], top_10))

def get_10_counts():
    return list(map(lambda dictionary: list(dictionary.values())[0], top_10))

# top_10_countries = list(top_10.keys())[0]
# top_10_counts = list(top_10.values())[0]
# sorted(counts, key=lambda d: list(d.values())[0], reverse=True)[:10]
# def top_10():
#     counts = []
#
#
#     counts = []
#     keys = list(map(lambda key: list(key.keys()), all))
#     key_index = keys.index(['{}'.format(type)])
#     key_values = list(all[key_index].values())
#     return key_values[0]
# def all_event_medals():


def unique_medal_countries():
    medal_countries = [medal.country_id for medal in Medal.query.all()]
    unique_countries = set(medal_countries)
    return len(unique_countries)
