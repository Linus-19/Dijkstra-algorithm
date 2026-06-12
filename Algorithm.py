import Grid as G
import pandas as pd

import Import_Data as ID
import math
import heapq

data = "Data_intersections_QuebecCity.csv"
links = "links_quebec.csv"
x, y, streets = ID.Import(data) #Import intersection data
data_sheet = pd.read_csv(links)

grid = G.Grid([100, 100])

for coords in range(len(x)) :
    #Creating the nodes corresponding to the intersection using longitude and latitude
    grid.AddNode(x[coords], y [coords]) 

for i in range (data_sheet.shape[0]) :
    grid.AddLink(data_sheet.iat[i, 0],data_sheet.iat[i, 1])


for coords in range(len(x)) : 
    for street in streets[coords] :
        #Getting every intersection matching the current street
        intersections_of_street = [sublist for sublist in streets if street in sublist] 
    distances = []
    for intersection in intersections_of_street :
        #Getting the distance to those intersenction
        distance = math.sqrt((x[coords] - x[streets.index(intersection)])**2 + (y[coords] - y[streets.index(intersection)])**2 ) #Getting the distance to those intersenction
        if distance == 0 : 
            distances.append(None)
        else:
            distances.append(distance)
    #Getting the two closest intersection to the current one, those are the most likely to be linked
    valid_links = heapq.nsmallest(2, heapq.nsmallest(2, (x for x in distances if x is not None)))
    #Making sure the current intersection is not a dead end, if both intersection a situated in the same direction, only link to one of them
    
    if len(valid_links) > 1 :
        if abs(grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[0])])] [0] - grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[1])])] [0]) < grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[0])])] [0] and abs(grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[0])])] [1] - grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[1])])] [1]) < grid.nodes[streets.index(intersections_of_street[distances.index(valid_links[0])])] [1] : 
        
            valid_link = min(valid_links)
            grid.AddLink(coords, distances.index(valid_link))
        else : 
            
            grid.AddLink(coords, distances.index(valid_links[0]))
            grid.AddLink(coords, distances.index(valid_links[1]))

        
    elif len(valid_links) > 0 :
        valid_link = valid_links[0]
        grid.AddLink(coords, distances.index(valid_link))
    





grid.AddNode(11, 12)
grid.AddNode(76, 13)
grid.AddLink(0, 1)
grid.AddNode(30, 33)
grid.AddLink(0, 2)
grid.AddNode(14, 63)
grid.AddNode(41, 81)
grid.AddLink(3,4)
grid.AddNode(85, 57)
grid.AddLink(4,5)
grid.AddNode(58, 50)
grid.AddLink(4, 6)
grid.AddNode(65, 32)
grid.AddLink(1, 7)
grid.AddLink(2, 7)
grid.AddLink(5,7)
grid.AddLink(6, 7)
grid.AddNode(11, 42)
grid.AddLink(2, 8)
grid.AddLink(3, 8)
grid.AddLink(6, 8)
grid.AddNode(75, 96)
grid.AddLink(5, 9)
grid.AddLink(4, 9)



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

#for node in grid.nodes :
    #print(f"Node : {grid.nodes.index(node)}, weight : {node[2]}")

grid.Visualise(GetPath(), starting_node, end_node)

#grid.VisualizeGrid()