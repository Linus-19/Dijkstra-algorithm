import Grid as G
import pandas as pd

import Import_Data as ID
import math

data = "Data_intersections_QuebecCity.csv"

print("Dijsktra's algorithm small demo")

own_data = input("Voulez-vous importer vos propres données? Il vous faudra formater votre fichier cvs de manière appropriée. (y/n)  ") == "y"
if own_data :
    
    city = input("Vos données représentent-elles une ville (si c'est le cas, l'agorithme pourra automatiquement générer une approximation des routes à l'aide du nom des route de l'intersection, sinon vous devrez fournir le fichier des liens) (y/n)  ") == "y"
    if city :
        print("Assurez vous que votre fichier soit organiser de manière à ce que la 2e et 3e colonnes soient les coordonnées et que la colonne suivante contiennent les rues qui composent l'intersection (il suffit de séparé les rues d'un / et de mettre toute autre information après --, elle sera ignorée)")
    else :
        print("Assurez vous que votre fichier soit organiser de manière à ce que la 2e et 3e colonnes soient les coordonnées")
    data = input("Veuillez entrer le nom du fichier qui contient les données. Il est important que celui-ci soit placé dans le fichier [Data]. (exemple.csv)  ")

    if not city :
         
        links = input(data = input("Veuillez entrer le nom du fichier qui contient les liens. Il est important que celui-ci soit placé dans le fichier [Liens]. Il doit contenir l'index de la première intersection dans la 1e colone et celui de la deuxième dans la 2e. Il important que les index correspondent à ceux dans le fichier d'intersections (exemple.csv)  "))


if not city :
    x, y  = ID.Import(data, False)
    data_sheet = pd.read_csv(links)
else : 
    x, y, streets = ID.Import(data, True)



grid = G.Grid([100, 100])

for coords in range(len(x)) :
    #Creating the nodes corresponding to the intersection using longitude and latitude
    grid.AddNode(x[coords], y [coords]) 

if city :

    streets_tuple = [tuple(s) for s in streets]
    street_to_indices = {}
    for i, s in enumerate(streets_tuple):
        street_to_indices[s] = i

    for coords in range(len(x)) : 
            #Getting every intersection matching the current street
        intersections_of_street = []
        for street in streets[coords]:  
            for i, s in enumerate(streets):
                if street in s and i != coords:
                    intersections_of_street.append(i)
        intersections_of_street = list(set(intersections_of_street)) 
        distances = []
        max_distance_for_link = 0.014 #1 km
        for idx in intersections_of_street:
            d = math.sqrt((x[coords] - x[idx])**2 + (y[coords] - y[idx])**2)
            if 0 < d < max_distance_for_link:
                distances.append((d, idx))

        if not distances:
            continue
        #Getting the two closest intersection to the current one, those are the most likely to be linked
        distances.sort()
        closest = distances[:2] 
        #Making sure the current intersection is not a dead end, if both intersection a situated in the same direction, only link to one of them
        
        if len(closest) == 2:
            d1, idx1 = closest[0]
            d2, idx2 = closest[1]

            v1 = (x[idx1] - x[coords], y[idx1] - y[coords])
            v2 = (x[idx2] - x[coords], y[idx2] - y[coords])

            dot = v1[0]*v2[0] + v1[1]*v2[1]
            mag = math.sqrt(v1[0]**2 + v1[1]**2) * math.sqrt(v2[0]**2 + v2[1]**2)
            cosine = dot / mag if mag > 0 else 0

            if cosine > 0.7:
                grid.AddLink(coords, idx1)  # seulement le plus proche
            else:
                grid.AddLink(coords, idx1)
                grid.AddLink(coords, idx2)
        elif len(closest) == 1:
            grid.AddLink(coords, closest[0][1])
else :
    for i in range(data_sheet.shape(0)) :
        grid.AddLink(data_sheet.iat[i, 0], data_sheet.iat[i, 1])




starting_index = 0
end_index = 9
starting_node = grid.nodes[starting_index]
end_node = grid.nodes[end_index]

grid.UpdateWeight(starting_node, 0) 

def Explore(node) :
    for link in grid.links :
        if grid.nodes.index(node) in link : #Checking if the link as the current node
            #print(f" {link} - {link[abs(link.index(grid.nodes.index(node))-1)]} : {grid.nodes[link[abs(link.index(grid.nodes.index(node))-1)]] [2]}")
            if link[2] + node[2] < grid.nodes[link[abs(link.index(grid.nodes.index(node))-1)]] [2]: #checking if weight is lower the the current link
                grid.UpdateWeight(grid.nodes[link [abs(link.index(grid.nodes.index(node))-1)]], link[2] + node[2], grid.nodes.index(node)) #taking the other node and updating it's weight to the distance between them and the other node + the weight of the first node
                print("changing weight")
    

def SerchGrid () :
    
    while True :
        weights = []
        unexplored_nodes = []
        
        for node in grid.nodes :
            if node[3] == 0 :
                unexplored_nodes.append(node)
                weights.append(node[2])
        if grid.nodes.index(unexplored_nodes[weights.index(min(weights))]) == end_index : 
            break
        Explore(unexplored_nodes[weights.index(min(weights))])    
        print(f"Node {grid.nodes.index(unexplored_nodes[weights.index(min(weights))])} explored")
        unexplored_nodes[weights.index(min(weights))] [3] = 1

def GetPath() :
    x = end_index
    path = [x]
    while not x == starting_index :
        x = grid.nodes[x] [4]
        path.append(x)
    return path[::-1]

        

SerchGrid()
#print(grid.nodes[end_index] [4])
#for node in grid.nodes :
    #print(f"Node : {grid.nodes.index(node)}, weight : {node[2]}")

grid.Visualise(GetPath(), starting_node, end_node)

#grid.VisualizeGrid()