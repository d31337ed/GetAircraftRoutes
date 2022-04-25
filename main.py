from getAircraftHistory import get_history
from getAircraftRegs import get_regs
from functools import reduce
import operator

airlineCode = 'ad-azu'
aircraftType = 'C208'
header = {'User-Agent': 'PostmanRuntime/7.29.0'}
NumPlanesLimit = 3

aircraftList = get_regs(airlineCode, aircraftType)
# generating list of routes. Iterating over aircraft, then making flat list
total_routes = []
for aircraft in aircraftList[0:NumPlanesLimit]:
    total_routes.append(get_history(aircraft))
total_routes = reduce(operator.iconcat, total_routes, [])




print(total_routes)
