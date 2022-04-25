import requests
import bs4
import time
from itertools import filterfalse
import random


def get_history(aircraft: str) -> list:
    """Provides routes history for aircraft REG specified in "aircraft" argument """
    # requesting
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    print('Fetching Aircraft Info: ' + aircraft)
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/aircraft/' + aircraft,
                                     headers=header).text
    # parsing
    routes_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')

    def get_destinations(key: str) -> list:
        """Sub-function to extract airport code from labels on page of Aircraft. "Key" must be "FROM" or "TO" """
        if key == "TO" or key == "FROM":
            raw_from_data = routes_soup.find_all('label', text=key)
            destinations = []
            for route in raw_from_data:
                fromTag = route.parent
                fromAirport = fromTag.findChild('a')
                if fromAirport is None:
                    destinations.append('-')
                else:
                    destinations.append(fromAirport.text[1:-2])
            return destinations
        else:
            raise ValueError

    froms = get_destinations('FROM')
    tos = get_destinations('TO')

    routes = [x + '-' + y for x, y in zip(froms, tos)]  # uniting destinations into routes ("FROM, "TO" -> "FROM-TO")
    routes = list(map(lambda s: s.strip("--"), routes))  # removing empty and semi-empty routes
    routes[:] = [x for x in routes if x]                # cleaning empty elements from list

    print("Total: ", len(froms), " routes for Aircraft", aircraft)
    time.sleep(random.randrange(3, 8)/10)

    return routes
