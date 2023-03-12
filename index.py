import json
import operator
import os
from fastapi import FastAPI
from functools import reduce
from flask import Flask, render_template, request, redirect, url_for
from getAircraftHistory import get_history
from getAircraftRegs import get_regs
from getFleet import get_fleet
from datetime import datetime
from getAirlinesList import get_airlines

# app = Flask(__name__, template_folder='templates')
app = FastAPI()


@app.get('/')
def homepage():
    return "HomePage template"


@app.get('/airlines/')
def get_airlines_list():
    return get_airlines()


@app.get('/airlines/{airline_code}/fleet/')
async def get_aircrafts_list(airline_code: str):
    return get_fleet(airline_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/regs/')
async def get_aircrafts_regs(airline_code: str, aircraft_code: str):
    return get_regs(airline_code, aircraft_code)


@app.get('/airlines/{airline_code}/fleet/{aircraft_code}/{routes}')
async def get_routes(airline_code: str, aircraft_code: str):
    return get_history(airline_code, aircraft_code)

# @app.route('/', methods=["GET", "POST"])
# def index():
    # airlines = get_airlines()
#    airlines = json.load(open("airlines.json"))
#    airline_titles = list(airlines.keys())
#    raw_update_timestamp = os.path.getmtime("airlines.json")
#    list_timestamp = datetime.fromtimestamp(raw_update_timestamp).strftime('%Y-%m-%d %H:%M:%S')
#    if request.method == "POST":
        # reading inputs
#        chosen_airline = request.form.get("airline")
#        airline_link = airlines[chosen_airline]
#        aircraft_type = request.form.get("aircraft_type")
#        fleet = get_fleet(airline_link)
#        if aircraft_type is None:
#            return render_template("pre-result.html",
#                                   chosen_airline=chosen_airline,
#                                   airline_titles=airline_titles,
#                                   fleet=fleet,
#                                   LinkText="Enter aircraft model to get link")
        # parsing reg numbers of aircrafts
#        planes = get_regs(airline_link, aircraft_type)
        # constructing list of lists of routes
#        total_routes = []
#        for aircraft in planes:
#            total_routes.append(get_history(aircraft))
#        total_routes = set(reduce(operator.iconcat, total_routes, []))  # list of unique routes among all aircrafts
#        link = "http://www.gcmap.com/mapui?P=" + ','.join(total_routes)  # generating GCMap link
#        return render_template("result.html",
#                               chosen_airline=chosen_airline,
#                               airline_titles=airline_titles,
#                               AircraftList=", ".join(planes),
#                               chosen_aircraft=aircraft_type,
#                               RoutesList=", ".join(total_routes),
#                               GCMapLink=link,
#                               fleet=fleet,
#                               LinkText="Click here to plot map")

#    return render_template("index.html",
#                           airline_titles=airline_titles,
#                           allist_timestamp=list_timestamp)


# if __name__ == '__main__':
#    app.run(debug=True)
