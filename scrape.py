import requests
from bs4 import BeautifulSoup
sport_year_request = requests.get('https://www.olympic.org/rio-2016/diving')
sport_year_html = sport_year_request.text
sport_year_soup = BeautifulSoup(sport_year_html)

events = sport_year_soup.findAll('section', {'class': 'event-box'})

list_of_tags=('AFG', 'ALB', 'ALG', 'ASA', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'ARU', 'AUS', 'AUT',  'AZE', 'BAH', 'BRN', 'BAN', 'BAR', 'BLR',  'BEL', 'BIZ', 'BEN', 'BER', 'BHU', 'BOL', 'BIH','BOT', 'BRA', 'BRU', 'BUL', 'BUR',  'BDI',  'CAM', 'CMR', 'CAN', 'CPV', 'CAY', 'CAF', 'CHA', 'CHI', 'TPE', 'COL', 'COM', 'CGO', 'COK', 'CRC', 'CIV', 'CRO', 'CUB', 'CYP', 'CZE', 'PRK', 'COD', 'DEN', 'DJI', 'DOM', 'DMA', 'ECU', 'EGY', 'ESA', 'GEQ', 'ERI', 'EST', 'SWZ', 'ETH', 'FSM', 'FIJ', 'FIN', 'FRA', 'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GBR', 'GRE', 'GRN', 'GUM', 'GUA', 'GUI', 'GBS', 'GUY', 'HAI', 'HON', 'HKG', 'HUN', 'ISL', 'IND', 'INA', 'IRQ', 'IRL', 'IRI', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOS', 'KUW', 'KGZ', 'LAO', 'LAT', 'LBN', 'LES', 'LBR', 'LBA', 'LIE', 'LTU', 'LUX', 'MAD', 'MAW', 'MAS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTN', 'MRI', 'MEX', 'MON', 'MGL', 'MNE', 'MAR', 'MOZ', 'MYA',  'NAM', 'NRU', 'NEP', 'NED', 'NZL', 'NCA', 'NIG', 'NGR', 'NOR', 'OMA', 'PAK', 'PLW', 'PLE', 'PAN', 'PNG', 'PAR', 'CHN', 'PER', 'PHI', 'POL', 'POR', 'PUR', 'QAT', 'KOR', 'MDA', 'ROU', 'RUS', 'RWA', 'SKN', 'LCA', 'SAM', 'SMR', 'STP', 'KSA', 'SEN', 'SRB', 'SEY', 'SLE', 'SGP', 'SVK', 'SLO', 'SOL', 'SOM', 'RSA', 'SSD', 'ESP', 'SRI', 'VIN', 'SUD',
              'SUR', 'SWE', 'SUI', 'SYR', 'TJK', 'THA', 'MKD', 'TLS', 'TOG', 'TGA', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA', 'UKR', 'UAE', 'TAN', 'USA', 'URU', 'UZB', 'VAN', 'VEN', 'VIE', 'IVB','ISV', 'YEM', 'ZAM', 'ZIM' )

def get_score_lists():
    all_clean_scores = []
    event_scores = []

    for event in events:
        scores = event.findAll('span', {'class':'txt'})
        event_scores.append(scores)

    for list in event_scores:
        clean_scores = []
        for score in list:
            clean_scores.append(score.text)
        all_clean_scores.append(clean_scores)
    return all_clean_scores
#cleaned list of scores grouped by event
####WHEN MAKING CLASS, HAVE SCORE BE N/A INIT

def get_name_lists():
    all_clean_names = []
    event_names = []

    for event in events:
        names = event.findAll('strong', {'class':'name'})
        event_names.append(names)

    for list in event_names:
        clean_names = []
        for name in list:
            clean_names.append(name.text)
        all_clean_names.append(clean_names)
    return all_clean_names
#cleaned list of names grouped by event


def get_event_names():
    event_names = []
    for event in events:
        clean_event = event.findNext('a').text[19:][:-14]
        event_names.append(clean_event)
    return event_names
#returns cleaned list of events

game_events = get_event_names()
score_lists = get_score_lists()
name_lists = get_name_lists()

def dictionaries():
    all = []
    for i in range(len(game_events)):
        if len(score_lists[i])<1:
            all.append([{name_lists[i][0]: None}, {name_lists[i][1]: None}, {name_lists[i][2]: None}])
        else:
            all.append([{name_lists[i][0]: score_lists[i][0]}, {name_lists[i][1]: score_lists[i][1]}, {name_lists[i][2]: score_lists[i][2]}])
    return all
#creates list of dictionaries, where each list consists of dictionaries of the name of medalist as key and their score as the value

name_score_dictionary = dictionaries()
name_score_dict = name_score_dictionary.copy()
game_events1 = game_events.copy()

def filter_out_events():
    all_i = []
    for i in range(len(game_events)):
        if list(name_score_dict[i][0].keys())[0] in list_of_tags:
            all_i.append(i)
    reverse_indexes = sorted(all_i, reverse = True)
    for i in reverse_indexes:
        game_events1.pop(i)
    return game_events1
#returns any events whose medalists aren't countries
filtered_events = filter_out_events()

def filter_out_countries():
    all_i = []
    for i in range(len(game_events)):
        if list(name_score_dict[i][0].keys())[0] in list_of_tags:
            all_i.append(i)
    reverse_indexes = sorted(all_i, reverse = True)
    for i in reverse_indexes:
        name_score_dict.pop(i)
    return name_score_dict
#returns list of medalists and scores where medalists are not countries

filtered_dict = filter_out_countries()


# def associate_score_name():
#     all_assoc = []
#     for i in range(len(game_events)):
#         all_assoc.append(list(zip(name_lists[i], score_lists[i])))
#     return all_assoc
# all = associate_score_name()
#gives a list of names and their scores grouped by event



# def filter_out_countries():
#     all_i = []
#     for i in range(len(game_events)):
#         if all[i][0][0] in list_of_tags:
#             all_i.append(i)
#     reverse_indexes = sorted(all_i, reverse = True)
#     for i in reverse_indexes:
#         all.pop(i)
#     return all
#

#
# def filter_out_events():
#     all_i = []
#     for i in range(len(game_events)):
#         if all[i][0][0] in list_of_tags:
#             all_i.append(i)
#     reverse_indexes = sorted(all_i, reverse = True)
#     for i in reverse_indexes:
#         game_events.pop(i)
#     return game_events



##Gets rid of the results and events associated with a country




sports_web= 'https://www.olympic.org/sports'
sports_re= requests.get(sports_web)
sports_page = sports_re.text
sports_soup = BeautifulSoup(sports_page, "lxml")
sports_table = games_soup.findAll("div", { "class" : "select-box" })

dirty_sports = sports_table[0].findAll('a')

def get_sports():
    clean_sports = []
    for sport in dirty_sports:
        clean_sports.append(sport.text[22:])
    return clean_sports

sports= get_sports()

def clean_sports():
    clean_sports = []
    for sport in sports:
        clean_sports.append(sport.split('\r')[0])
    return clean_sports

cleaned_sports = clean_sports()


games_web= 'https://www.olympic.org/summer-games'
games_re= requests.get(games_web)
games_page = games_re.text
games_soup = BeautifulSoup(games_page, "lxml")
games_table = games_soup.findAll("ul", { "class" : "game-boxes" })

dirty_games = games_table[0].findAll('p')

def clean_games():
    cleaned_games = []
    for game in dirty_games:
        cleaned_games.append(game.text)
    return cleaned_games[3:13]
#filter down to 1980 - 2016
cleaned_games = clean_games()

def filtered_url_games():
    urls = []
    for game in cleaned_games:
        tog = game.replace(' ', '-')
        lower = tog.lower()
        urls.append('https://www.olympic.org/' + lower)
    return urls
#getting the urls for each olympic game

game_urls = filtered_url_games()

def game_sports_urls():
    game_sport_urls = []
    for game_url in game_urls:
        for sport in cleaned_sports:
            tog = sport.replace(' ', '-')
            lower = tog.lower()
            if lower == 'equestrian-/-dressage':
                equest = lower.replace('-/-', '-')
                game_sport_urls.append(game_url + '/' + equest)
            else:
                game_sport_urls.append(game_url + '/' + lower)
    return game_sport_urls





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
#gives list of lists - each list consists of the game's country, game's year, and game's city

games_info = get_games_info()
