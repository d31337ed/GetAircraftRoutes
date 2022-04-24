import pandas as pd

dataPath = 'AzulCessna_FEB2022.csv'
rawData = pd.read_csv(dataPath)

FROM_Codes = rawData.FROM.str.slice(start=-4, stop=-1)
TO_Codes = rawData.TO.str.slice(start=-4, stop=-1)

routesRaw = TO_Codes + '-' + FROM_Codes
routesList = routesRaw.drop(routesRaw[routesRaw.str.len() < 6].index).unique().tolist()
routesString = ','.join(routesList)

destinationsList = pd.concat([TO_Codes, FROM_Codes]).unique().tolist()
destinationsString = ','.join(destinationsList).replace(',,', ',')

print(routesString)
