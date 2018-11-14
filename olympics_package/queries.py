# from final_testing import *
from olympics_package.models import *
from olympics_package.__init__ import *


##below returns list of all country objects
# def all_countries():
#     return Country.query.all()
#
# def countries_with_many_medals():
#     return [country.name for country in Country.query.all() if len(country.medals) > 10]


def country_medal_counts():
    all_country_medal_counts = []
    countries = Country.query.all()
    for country in countries:
        medals = [medal.id for medal in Medal.query.all() if medal.country == country]
        medal_count = len(medals)
        country_medal_dict = {country.name: medal_count}
        all_country_medal_counts.append(country_medal_dict)
    return all_country_medal_counts[0:10]


def country_medal_totals():
    country_medal_list = country_medal_counts()
    x = []
    y = []
    for country in country_medal_list:
        name = list(country.keys())[0]
        count = list(country.values())[0]
        x.append(name)
        y.append(count)
    return [{'x': x, 'y': y, 'type': 'bar', 'name': 'Top 10'}]
