import requests
import bs4
import json


def get_airlines():
    """This function is used to obtain airlines list for input simplification"""
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/airlines',
                                     headers=header).text
    # parsing HTML
    airlines_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')
    raw_airlines_data = airlines_soup.find_all("td", {"class": "notranslate"})  # getting strings with airline data
    titles = []
    codes = []
    for raw_airline in raw_airlines_data:
        titles.append(raw_airline.find("a")['title'])
        codes.append(raw_airline.find("a")['href'].replace('/data/airlines/',''))
    airlines = dict(zip(titles, codes))
    with open('airlines.json', 'w') as file:
        file.write(json.dumps(airlines))
    return json.dumps(airlines)


get_airlines()
