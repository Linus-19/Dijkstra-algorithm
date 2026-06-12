import pandas as pd

def Import(path):
    _path = path #"Data_intersections_QuebecCity.cvs"

    data_sheet = pd.read_csv(path)

    #data_sheet.drop(columns=["ID", "NOM_INTERSECTION"])

    x = []
    y = []
    streets = []
    
    for i in range (data_sheet.shape[0]) :

        x.append(data_sheet.iat[i, 1])
        y.append(data_sheet.iat[i, 2]) 
        streets.append(str(data_sheet.iat[i, 3]).split("    /   "))
    
    return x, y, streets
