from sqlalchemy import *
from sqlalchemy.sql import *
from bs4 import BeautifulSoup
import requests

###sports- gets the sports info from the website

def get_sports():   ###retrieving the sports
    sports_web= 'https://www.olympic.org/sports'
    sports_re= requests.get(sports_web)
    sports_page = sports_re.text
    sports_soup = BeautifulSoup(sports_page, "lxml")
    sports=[]
    dirty_sports = sports_soup.findAll("div", { "class" : "select-box" })[0].findAll('a')
    for sport in dirty_sports:
        sports.append(sport.text[22:])

    clean_sports = []
    for sport in sports:
        clean_sports.append(sport.split('\r')[0])
    return clean_sports
all_sports= get_sports()



#####this code below scrapes the website to get the olympic games from 1980-2016.
games_web= 'https://www.olympic.org/summer-games'
games_re= requests.get(games_web)
games_page = games_re.text
games_soup = BeautifulSoup(games_page, "lxml")
games_table = games_soup.findAll("ul", { "class" : "game-boxes" })

def clean_games():    ### returns a list of game names in the format: City Year
    dirty_games = games_table[0].findAll('p')
    cleaned_games = []
    for game in dirty_games:
        cleaned_games.append(game.text)
    return cleaned_games[3:13]      ##filters down to the olympic games that we are interested in
#filter down to 1980 - 2016
cleaned_games = clean_games()
def filtered_url_games():    ##returns a list of urls, where each url takes us to the olympic game page
    urls = []
    for game in cleaned_games:
        tog = game.replace(' ', '-')
        lower = tog.lower()
        urls.append('https://www.olympic.org/' + lower)
    return urls
#getting the urls for each olympic game
game_urls = filtered_url_games()
def game_sports_urls():    ##returns a list of urls that point to every sport page from every game
    game_sport_urls = []
    for game_url in game_urls:   ##looking at each game url
        for sport in all_sports:    ##appending the sport name to the game url
            tog = sport.replace(' ', '-')
            lower = tog.lower()
            if lower == 'equestrian-/-dressage':      ##equestrian / dressage was not a typical format. accounted for the variation
                equest = lower.replace('-/-', '-')
                game_sport_urls.append(game_url + '/' + equest)
            else:
                game_sport_urls.append(game_url + '/' + lower)
    return game_sport_urls
game_sport_urls = game_sports_urls()

def get_games_info():
    games_info = []
    for game in game_urls:
        #goes through urls pointing to each game
        games_info_request = requests.get(game)
        games_info_html = games_info_request.text
        games_info_soup = BeautifulSoup(games_info_html)
        #set up beautiful soup for each url
        game_country = games_info_soup.findAll('div', {'class':"text-box"})[2].find('a').text
        #get country name
        game_year = game[(len(game)-4):]
        #get last four characters in the url, which represent the game's year
        game_city = game[24:(len(game)-5)].replace('-', ' ')
        #get characters between beginning of url and the game's year in the url
        games_info.append([game_country, game_year, game_city])
    return games_info
game_info = get_games_info()

## country code tags and country list to make country table below##
list_of_tags=('AFG', 'ALB', 'ALG', 'ASA', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'ARU', 'AUS', 'AUT',  'AZE', 'BAH', 'BRN', 'BAN', 'BAR', 'BLR',  'BEL', 'BIZ', 'BEN', 'BER', 'BHU', 'BOL', 'BIH','BOT', 'BRA', 'BRU', 'BUL', 'BUR',  'BDI',  'CAM', 'CMR', 'CAN', 'CPV', 'CAY', 'CAF', 'CHA', 'CHI', 'TPE', 'COL', 'COM', 'CGO', 'COK', 'CRC', 'CIV', 'CRO', 'CUB', 'CYP', 'CZE', 'PRK', 'COD', 'DEN', 'DJI', 'DOM', 'DMA', 'ECU', 'EGY', 'ESA', 'GEQ', 'ERI', 'EST', 'SWZ', 'ETH', 'FSM', 'FIJ', 'FIN', 'FRA', 'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GBR', 'GRE', 'GRN', 'GUM', 'GUA', 'GUI', 'GBS', 'GUY', 'HAI', 'HON', 'HKG', 'HUN', 'ISL', 'IND', 'INA', 'IRQ', 'IRL', 'IRI', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOS', 'KUW', 'KGZ', 'LAO', 'LAT', 'LBN', 'LES', 'LBR', 'LBA', 'LIE', 'LTU', 'LUX', 'MAD', 'MAW', 'MAS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTN', 'MRI', 'MEX', 'MON', 'MGL', 'MNE', 'MAR', 'MOZ', 'MYA',  'NAM', 'NRU', 'NEP', 'NED', 'NZL', 'NCA', 'NIG', 'NGR', 'NOR', 'OMA', 'PAK', 'PLW', 'PLE', 'PAN', 'PNG', 'PAR', 'CHN', 'PER', 'PHI', 'POL', 'POR', 'PUR', 'QAT', 'KOR', 'MDA', 'ROU', 'RUS', 'RWA', 'SKN', 'LCA', 'SAM', 'SMR', 'STP', 'KSA', 'SEN', 'SRB', 'SEY', 'SLE', 'SGP', 'SVK', 'SLO', 'SOL', 'SOM', 'RSA', 'SSD', 'ESP', 'SRI', 'VIN', 'SUD',
              'SUR', 'SWE', 'SUI', 'SYR', 'TJK', 'THA', 'MKD', 'TLS', 'TOG', 'TGA', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA', 'UKR', 'UAE', 'TAN', 'USA', 'URU', 'UZB', 'VAN', 'VEN', 'VIE', 'IVB','ISV', 'YEM', 'ZAM', 'ZIM' )

def get_countries():
    import requests
    countries_request = requests.get('https://www.olympic.org/national-olympic-committees')
    countries_html = countries_request.text
    from bs4 import BeautifulSoup
    countries_soup = BeautifulSoup(countries_html)
    countries = []
    dirty_countries = countries_soup.findAll('div', {'class': 'countries'})[0].findAll('a')
    all_clean_countries= []
    for country in dirty_countries:
        all_clean_countries.append(country.text[22:].split('\r'))

    for country in all_clean_countries:
        countries.append(country[0])
    return countries

countries = get_countries()
country_to_tag = list(zip(countries, list_of_tags))
