import pandas as pd
import re

def Import(path, city):
    _path = "Data/" + path #"Data_intersections_QuebecCity.cvs"
    

    data_sheet = pd.read_csv(_path)

    x = []
    y = []
    streets = []
    
    

    for i in range(data_sheet.shape[0]):
        x.append(data_sheet.iat[i, 1])
        y.append(data_sheet.iat[i, 2])
        if city :
        
            raw = str(data_sheet.iat[i, 3])
            
            raw = re.split(r'\s*--\s*', raw)[0]
            
            parts = re.split(r'\s*/\s*', raw)
            
            # Nettoyer chaque nom de rue
            parts = [re.sub(r'\s+', ' ', p).strip() for p in parts]
            parts = [p for p in parts if len(p) > 2]
            
            streets.append(parts)
        
    return x, y, streets
