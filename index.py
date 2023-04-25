import json
import operator
import os
from fastapi import FastAPI
from functools import reduce
# from flask import Flask, render_template, request, redirect, url_for
from getAircraftHistory import get_history
from getAircraftRegs import get_regs
from getFleet import get_fleet
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
def homepage():
    with open(os.path.join(os.getcwd(), 'templates/result-API.html')) as fh:
        data = fh.read()
    return HTMLResponse(content=data, media_type="text/html")


@app.get('/airlines/')
def get_airlines_list(q: str | None = None):
    airlines = json.load(open("airlines.json"))
    if q:
        airlines_list = airlines['results']
        filtered_airlines = []
        for airline in airlines_list:
            if q.upper() in airline["text"].upper():
                filtered_airlines.append(airline)
        query_result = '{"results": ' + json.dumps(filtered_airlines) + '}'
        print(query_result)
        return json.loads(query_result)
    return airlines


@app.get('/airlines/timestamp')
def get_airlines_timestamp():
    raw_update_timestamp = os.path.getmtime("airlines.json")
    list_timestamp = datetime.fromtimestamp(raw_update_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return list_timestamp

@app.get('/airlines/{airline_code}/fleet/')
async def get_aircrafts_list(airline_code: str):
    return get_fleet(airline_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/regs/')
async def get_aircrafts_regs(airline_code: str, aircraft_code: str):
    return get_regs(airline_code, aircraft_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/routes/')
async def get_routes(airline_code: str, aircraft_code: str):
    planes = get_regs(airline_code, aircraft_code)
    print(planes)
    # constructing list of lists of routes
    total_routes = []
    for aircraft in planes:
        total_routes.append(get_history(aircraft))
    total_routes = set(reduce(operator.iconcat, total_routes, []))  # list of unique routes among all aircrafts
    link = "http://www.gcmap.com/mapui?P=" + ','.join(total_routes)  # generating GCMap link
    print(link)
    return total_routes


#    raw_update_timestamp = os.path.getmtime("airlines.json")
#    list_timestamp = datetime.fromtimestamp(raw_update_timestamp).strftime('%Y-%m-%d %H:%M:%S')

#    link = "http://www.gcmap.com/mapui?P=" + ','.join(total_routes)  # generating GCMap link
