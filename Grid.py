import math
import matplotlib.pyplot as plt
import numpy as np

class Grid :
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.links = []
        

    def AddNode(self, x, y, w = 100000000, exp = 0, previous_in_path = None) :
        self.nodes.append([x,y,w, exp, previous_in_path])

    def AddLink(self, node1, node2) :
        if not [node1, node2] in self.links and not [node2, node1] in self.links : 
            self.links.append([node1, node2, math.sqrt((self.nodes[node1] [0] - self.nodes[node2] [0])**2 + (self.nodes[node1] [1] - self.nodes[node2] [1])**2 )])

    def UpdateWeight(self, node, weight, origin = None) :
        node[2] = weight
        node[4] = origin
        
    
    def Visualise(self, path, start, end) :
        x_list = [] 
        y_list = []
        for node in self.nodes :
            x_list.append(node[0])
            y_list.append([node[1]])
        x = np.array(x_list)
        y = np.array(y_list)
    
        for link in self.links :
            plt.plot([self.nodes[link[0]] [0], self.nodes[link[1]] [0]], [self.nodes[link[0]] [1], self.nodes[link[1]] [1]], 'o:k', ms =4)
        #plt.scatter(x, y, marker = 'o')

        x_list = []
        y_list = []
        for index in path :
            x_list.append(self.nodes[index][0])
            y_list.append([self.nodes[index][1]])
        x = np.array(x_list)
        y = np.array(y_list)
        i = 0
        while i < len(x) -1 :
            plt.plot([x[i], x[i+1]], [y[i], y[i+1]], 'o:c', ms=7)
            i+=1
        
        plt.plot(start[0], start[1], "sg", ms = 10)
        plt.plot(end[0], end[1], "sr", ms = 10)

        plt.show()
        
    def VisualizeGrid(self) :
        x_list = [] 
        y_list = []
        for node in self.nodes :
            x_list.append(node[0])
            y_list.append([node[1]])
        plt.scatter(x_list,y_list)
        for link in self.links :
            plt.plot([self.nodes[link[0]] [0], self.nodes[link[1]] [0]], [self.nodes[link[0]] [1], self.nodes[link[1]] [1]], 'o:k', ms =4)
        plt.show()

