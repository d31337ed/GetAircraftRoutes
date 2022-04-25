import requests
import bs4
import time
from itertools import filterfalse
# import random
# TODO: сделать рандомный таймаут запросов


def get_history(aircraft):
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    print('Fetching Aircraft Info: ' + aircraft[1:-1])
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/aircraft/' + aircraft[1:-1],
                                     headers=header).text

    routes_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')

    raw_from_data = routes_soup.find_all('label', text='FROM')
    froms = []
    for route in raw_from_data:
        fromTag = route.parent
        fromAirport = fromTag.findChild('a')
        if fromAirport is None:
            froms.append('-')
        else:
            froms.append(fromAirport.text[1:-2])

    raw_TO_data = routes_soup.find_all('label', text='TO')
    tos = []
    for route in raw_TO_data:
        toTag = route.parent
        toAirport = toTag.findChild('a')
        if toAirport is None:
            tos.append('-')
        else:
            tos.append(toAirport.text[1:-2])

    routes = [x + '-' + y for x, y in zip(froms, tos)]

    # TODO: удалить все строки с тирешечками
    print("Total: ", len(froms), " routes for Aircraft", aircraft)
    time.sleep(1)

    return routes
