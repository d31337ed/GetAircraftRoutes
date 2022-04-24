import requests
import bs4
from getAircraftRegs import get_regs
import time
# import random

airlineCode = 'ad-azu'
aircraftType = 'C208'
header = {'User-Agent': 'PostmanRuntime/7.29.0'}
NumPlanesLimit = 10

aircraftList = get_regs(airlineCode, aircraftType)
print(aircraftList[0:NumPlanesLimit])
# for aircraft in aircraftList:
for aircraft in aircraftList[0:NumPlanesLimit]:
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
    print(froms)

    raw_TO_data = routes_soup.find_all('label', text='TO')
    tos = []
    for route in raw_TO_data:
        toTag = route.parent
        toAirport = toTag.findChild('a')
        if toAirport is None:
            tos.append('-')
        else:
            tos.append(toAirport.text[1:-2])
    print(tos)

    print(len(froms))
    time.sleep(1)

    # TODO: извлечь коды аэропортов (желательно, по ИАТА)
