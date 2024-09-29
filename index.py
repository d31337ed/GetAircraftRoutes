import json
import operator
import os
import logging
from fastapi import FastAPI
from functools import reduce
from getAircraftHistory import get_history
from getAircraftRegs import get_regs
from getFleet import get_fleet
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


logging.basicConfig(
    filename="logs/logfile.log",
    format='%(asctime)s:%(levelname)s:%(message)s')
handler = logging.handlers.TimedRotatingFileHandler('logs/logfile_',
                                                    when='midnight',
                                                    interval=1,
                                                    backupCount=365)
logger = logging.getLogger("Rotating log")
logger.addHandler(handler)


app = FastAPI()
logging.info("Created an instance of FastAPI app")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/js", StaticFiles(directory="js"), name="js")


@app.get('/', response_class=HTMLResponse)
def homepage():
    """Method returns main HTML file with all corresponding frontend logic"""
    logging.info("Handling '/' resource request")
    with open(os.path.join(os.getcwd(), 'templates/index.html')) as fh:
        data = fh.read()
    return HTMLResponse(content=data, media_type="text/html")


@app.get('/airlines/')
def get_airlines_list(q: str | None = None):
    logging.info("Handling '/airlines' resource request")
    """Method returns list of airlines for dropdown menu. Also returns filtered list for search (if 'q is passed')"""
    # Reading cached list of airlines
    airlines = json.load(open("airlines.json"))
    if q:
        # if q param is passed - method returns filtered list of airlines for Dropdown element
        airlines_list = airlines['results']
        filtered_airlines = []
        # Filtering loop:
        for airline in airlines_list:
            # Conversion to upper case is made to make search case non-sensitive
            if q.upper() in airline["text"].upper():
                filtered_airlines.append(airline)
        # conversion of filtered list to format expected by Select2 Dropdown element
        query_result = '{"results": ' + json.dumps(filtered_airlines) + '}'
        return json.loads(query_result)
    # if q is not passed - method returns a full list of airlines for Dropdown element
    return airlines


@app.get('/airlines/timestamp')
def get_airlines_timestamp():
    logging.info("Handling '/airlines/timestamp' resource request")
    """Method returns time of last  caching of airlines list"""
    # As it is cached in a file, we are just reading last modification time
    raw_update_timestamp = os.path.getmtime("airlines.json")
    # Conversion of timestamp to human-readable format
    list_timestamp = datetime.fromtimestamp(raw_update_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return list_timestamp


@app.get('/airlines/{airline_code}/fleet/')
async def get_aircrafts_list(airline_code: str):
    logging.info("Handling '/airlines/{airline_code}/fleet/' resource request")
    """Method returns list of aircraft types for certain airline"""
    return get_fleet(airline_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/regs/')
async def get_aircrafts_regs(airline_code: str, aircraft_code: str):
    logging.info("Handling '/airlines/{airline_code}/fleet/{aircraft_code}/regs/' resource request")
    """Method returns list of Reg. ID's of certain airline for certain aircraft type"""
    return get_regs(airline_code, aircraft_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/routes/')
async def get_regs_routes_link(airline_code: str, aircraft_code: str):
    logging.info("Handling '/airlines/{airline_code}/fleet/{aircraft_code}/routes/' resource request")
    """Method returns the final result: list of routes, list of reg. numbers and GCMap Link"""
    planes = get_regs(airline_code, aircraft_code)
    # constructing list of lists of routes
    total_routes = []
    for aircraft in planes:
        total_routes.append(get_history(aircraft))
    total_routes = list(set(reduce(operator.iconcat, total_routes, []))) # list of unique routes among all aircrafts
    link = "http://www.gcmap.com/mapui?P=" + ','.join(total_routes)  # generating GCMap link
    # результат -- json с тремя подструктурами: routes, regs, link
    result = {'planes': planes, 'routes': total_routes, 'link': link}
    return result
