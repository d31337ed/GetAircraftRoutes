from getAircraftRegs import get_regs
from getAircraftHistory import get_history
from flask import Flask, render_template, request
from functools import reduce
import operator

app = Flask(__name__, template_folder='templates')
# TODO: показывать прогресс

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # reading inputs
        airline_code = request.form.get("airline")
        aircraft_type = request.form.get("aircraft_type ")
        # parsing reg numbers of aircrafts
        planes = get_regs(airline_code, aircraft_type)
        # constructing list of lists of routes
        total_routes = []
        for aircraft in planes:
            total_routes.append(get_history(aircraft))
        total_routes = set(reduce(operator.iconcat, total_routes, []))  # list of unique routes among all aircrafts
        link = "http://www.gcmap.com/mapui?P=" + ",".join(total_routes)  # generating GCMap link
        return render_template("index.html",
                               AircraftList=", ".join(planes),
                               RoutesList=", ".join(total_routes),
                               GCMapLink=link)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
