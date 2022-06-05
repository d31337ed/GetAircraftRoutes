from getAircraftRegs import get_regs
from getAircraftHistory import get_history
from getFleet import get_fleet
from getAirlinesList import get_airlines
from flask import Flask, render_template, request, redirect, url_for
from functools import reduce
import operator

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["GET", "POST"])
def index():
    airlines = get_airlines()
    airline_titles = list(airlines.keys())
    if request.method == "POST":
        # reading inputs
        input = request.form.get("airline")
        airline_link = airlines[input]
        aircraft_type = request.form.get("aircraft_type ").upper()
        if aircraft_type == '':
            fleet = get_fleet(airline_link)
            fleet_string = '''Okay, here's a list of aircraft types for ''' \
                           + input + ': ' + ', '.join(fleet)
            return render_template("result.html",
                                   airline_titles=airline_titles,
                                   FleetList=fleet_string,
                                   LinkText="Enter aircraft model to get link")
        # parsing reg numbers of aircrafts
        planes = get_regs(airline_link, aircraft_type)
        # constructing list of lists of routes
        total_routes = []
        for aircraft in planes:
            total_routes.append(get_history(aircraft))
        total_routes = set(reduce(operator.iconcat, total_routes, []))  # list of unique routes among all aircrafts
        link = "http://www.gcmap.com/mapui?P=" + ','.join(total_routes)  # generating GCMap link
        return render_template("result.html",
                               airline_titles=airline_titles,
                               AircraftList=", ".join(planes),
                               RoutesList=", ".join(total_routes),
                               GCMapLink=link,
                               LinkText="Click here to plot map",)

    return render_template("index.html", airline_titles=airline_titles)


if __name__ == '__main__':
    app.run(debug=True)
