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
    select_list = []
    for raw_airline in raw_airlines_data:
        current_title = raw_airline.find("a")['title']
        titles.append(current_title)
        current_code = raw_airline.find("a")['href'].replace('/data/airlines/', '')
        codes.append(current_code)
        select_list.append({"id": current_code, "text": current_title})

    with open('/routes-app/airlines.json', 'w') as file:
        file.write('{"results": ' + json.dumps(select_list) + '}')


if __name__ == '__main__':
    get_airlines()
    print(get_airlines())
