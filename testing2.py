import requests
from bs4 import BeautifulSoup
sport_year_request = requests.get('https://www.olympic.org/rio-2016/diving')
sport_year_html = sport_year_request.text
sport_year_soup = BeautifulSoup(sport_year_html)

events = sport_year_soup.findAll('section', {'class': 'event-box'})

def event_scores():
    event_scores = []
    for event in events:
        scores = event.findAll('span', {'class':'txt'})
        event_scores.append(scores)
    return event_scores

def event_names():
    event_names = []
    for event in events:
        names = event.findAll('strong', {'class':'name'})
        event_names.append(names)
    return event_names




# event_scores()
names = event_names()
scores = event_scores()

def get_score_lists():
    all_clean_scores = []
    for list in scores:
        clean_scores = []
        for score in list:
            clean_scores.append(score.text)
        all_clean_scores.append(clean_scores)
    return all_clean_scores
#list of scores grouped by event
####WHEN MAKING CLASS, HAVE SCORE BE N/A INIT


def get_name_lists():
    all_clean_names = []
    for list in names:
        clean_names = []
        for name in list:
            clean_names.append(name.text)
        all_clean_names.append(clean_names)
    return all_clean_names
#list of names grouped by event

name_lists = get_name_lists()
score_lists = get_score_lists()


sport_year_soup.findAll('section', {'class': 'event-box'})[4].findNext('a').text[19:][:-14]

def get_event_names():
    event_names = []
    for event in events:
        clean_event = event.findNext('a').text[19:][:-14]
        event_names.append(clean_event)
    return event_names
#list of events
game_events = get_event_names()

name_lists = get_name_lists()
score_lists = get_score_lists()

def associate_score_name():
    all_assoc = []
    for i in range(len(game_events)):
        all_assoc.append(list(zip(name_lists[i], score_lists[i])))
    return all_assoc
all = associate_score_name()
#gives a list of names and their scores grouped by event
game_events = get_event_names()

list_of_tags=('AFG', 'ALB', 'ALG', 'ASA', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'ARU', 'AUS', 'AUT',  'AZE', 'BAH', 'BRN', 'BAN', 'BAR', 'BLR',  'BEL', 'BIZ', 'BEN', 'BER', 'BHU', 'BOL', 'BIH','BOT', 'BRA', 'BRU', 'BUL', 'BUR',  'BDI',  'CAM', 'CMR', 'CAN', 'CPV', 'CAY', 'CAF', 'CHA', 'CHI', 'TPE', 'COL', 'COM', 'CGO', 'COK', 'CRC', 'CIV', 'CRO', 'CUB', 'CYP', 'CZE', 'PRK', 'COD', 'DEN', 'DJI', 'DOM', 'DMA', 'ECU', 'EGY', 'ESA', 'GEQ', 'ERI', 'EST', 'SWZ', 'ETH', 'FSM', 'FIJ', 'FIN', 'FRA', 'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GBR', 'GRE', 'GRN', 'GUM', 'GUA', 'GUI', 'GBS', 'GUY', 'HAI', 'HON', 'HKG', 'HUN', 'ISL', 'IND', 'INA', 'IRQ', 'IRL', 'IRI', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOS', 'KUW', 'KGZ', 'LAO', 'LAT', 'LBN', 'LES', 'LBR', 'LBA', 'LIE', 'LTU', 'LUX', 'MAD', 'MAW', 'MAS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTN', 'MRI', 'MEX', 'MON', 'MGL', 'MNE', 'MAR', 'MOZ', 'MYA',  'NAM', 'NRU', 'NEP', 'NED', 'NZL', 'NCA', 'NIG', 'NGR', 'NOR', 'OMA', 'PAK', 'PLW', 'PLE', 'PAN', 'PNG', 'PAR', 'CHN', 'PER', 'PHI', 'POL', 'POR', 'PUR', 'QAT', 'KOR', 'MDA', 'ROU', 'RUS', 'RWA', 'SKN', 'LCA', 'SAM', 'SMR', 'STP', 'KSA', 'SEN', 'SRB', 'SEY', 'SLE', 'SGP', 'SVK', 'SLO', 'SOL', 'SOM', 'RSA', 'SSD', 'ESP', 'SRI', 'VIN', 'SUD',
              'SUR', 'SWE', 'SUI', 'SYR', 'TJK', 'THA', 'MKD', 'TLS', 'TOG', 'TGA', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA', 'UKR', 'UAE', 'TAN', 'USA', 'URU', 'UZB', 'VAN', 'VEN', 'VIE', 'IVB','ISV', 'YEM', 'ZAM', 'ZIM' )
#the

def filter_out_countries():
    all_i = []
    for i in range(len(game_events)):
        if all[i][0][0] in list_of_tags:
            all_i.append(i)
    reverse_indexes = sorted(all_i, reverse = True)
    for i in reverse_indexes:
        all.pop(i)
    return all

def filter_out_events():
    all_i = []
    for i in range(len(game_events)):
        if all[i][0][0] in list_of_tags:
            all_i.append(i)
    reverse_indexes = sorted(all_i, reverse = True)
    for i in reverse_indexes:
        game_events.pop(i)
    return game_events



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
