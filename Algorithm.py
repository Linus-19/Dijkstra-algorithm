import Grid as G

import pandas as pd

grid = G.Grid([100, 100])



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