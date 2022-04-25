from getAircraftRegs import get_regs
from getAircraftHistory import get_history
from flask import Flask, render_template, request
from functools import reduce
import operator

app = Flask(__name__, template_folder='templates')
# TODO показывать прогресс

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        airline_code = request.form.get("fname")
        aircraft_type = request.form.get("aircraft_type ")
        planes = get_regs(airline_code, aircraft_type)

        total_routes = []
        for aircraft in planes:
            total_routes.append(get_history(aircraft))
        total_routes = reduce(operator.iconcat, total_routes, [])
        link = "http://www.gcmap.com/mapui?P=" + ",".join(total_routes)
        return render_template("index.html",
                               AircraftList=", ".join(planes),
                               RoutesList=", ".join(total_routes),
                               GCMapLink=link)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
