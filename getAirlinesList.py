import requests
import bs4


def get_airlines() -> dict:
    """This function is used to obtain airlines list for input simplification"""
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/airlines',
                                     headers=header).text
    # parsing HTML
    airlines_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')
    raw_airlines_data = airlines_soup.find_all("td", {"class": "notranslate"})
    titles = []
    links = []
    for raw_airline in raw_airlines_data:
        titles.append(raw_airline.find("a")['title'])
        links.append(raw_airline.find("a")['href'])
    airlines = dict(zip(titles, links))
    return airlines
