import requests
import bs4


def get_regs(airline_link: str, aircraft_type: str) -> list:
    """Function is used to get list of Aircraft REG numbers of plane model noticed last month by certain airline"""
    # getting raw html from flightradar
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/airlines/' + airline_link + '/fleet',
                                     headers=header).text
    # parsing HTML
    aircraft_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')
    # choosing block containing aircraft model code and extracting text from the next block
    raw_data = aircraft_soup.find('div', text=aircraft_type).parent.next_sibling
    reg_numbers_raw = raw_data.find_all('a')
    # filling list of REG numbers
    reg_numbers = []
    for aircraft in reg_numbers_raw:
        if aircraft is not None:
            reg_numbers.append(aircraft.string)
    reg_numbers = list(filter(None, reg_numbers))              # removing empty elements
    reg_numbers = list(map(lambda x: x.strip(), reg_numbers))  # cutting spaces in the edges of REGs

    return reg_numbers
