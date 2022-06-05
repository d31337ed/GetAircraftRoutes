import requests
import bs4


def get_fleet(airline_link: str) -> list:
    """Function is used to get list of Aircraft REG numbers of plane model noticed last month by certain airline"""
    # getting raw html from flightradar
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    raw_aircraft_data = requests.get('https://www.flightradar24.com' + airline_link + '/fleet',
                                     headers=header).text
    # parsing HTML
    fleet_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')
    raw_data = fleet_soup.find_all('dt')[1:]
    fleet = list(map(lambda x: str(x.findChild("div")).lstrip('<div>').rstrip('</div>'), raw_data))
    return fleet
