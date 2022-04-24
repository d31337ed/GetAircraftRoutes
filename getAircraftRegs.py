import requests
import bs4


def get_regs(airline_code, aircraft_type):
    header = {'User-Agent': 'PostmanRuntime/7.29.0'}
    raw_aircraft_data = requests.get('https://www.flightradar24.com/data/airlines/' + airline_code + '/fleet',
                                     headers=header).text

    aircraft_soup = bs4.BeautifulSoup(raw_aircraft_data, 'html.parser')
    raw_cessna_data = aircraft_soup.find('div', text=aircraft_type).parent.next_sibling
    cessna_regs_raw = raw_cessna_data.find_all('a')
    cessna_regs = []
    for aircraft in cessna_regs_raw:
        if aircraft is not None:
            cessna_regs.append(aircraft.string)
#    if type(aircraft) != 'NoneType':
#        aircraft = aircraft.replace(' ','')
    cessna_regs = list(filter(None, cessna_regs))

    # TODO: убрать ебучие пробелы и вынести их обрезку из следующего метода
    # print(type(cessnaRegs))
    return cessna_regs

