import random
import math

class Model:

    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []

    def BuildModel(self):
        # birthday = 03/11/2000
        birthday = 3112000
        random.seed(birthday)
        depot = Node(0, 0, 0, 50, 50)
        self.allNodes.append(depot)
        random.seed(1)
        for i in range(0, 100):
            id = i + 1
            dem = random.randint(1, 5) * 100
            xx = random.randint(0, 100)
            yy = random.randint(0, 100)
            st = 0.25
            cust = Node(id, st, dem, xx, yy)
            self.allNodes.append(cust)
            self.customers.append(cust)
        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]
        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist

class Node:
    def __init__(self, id, st, dem, xx, yy):
        self.id = id
        self.service_time = st
        self.demand = dem
        self.x = xx
        self.y = yy
        self.isRouted = False

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.capacity = cap
        self.load = 0
        self.time = 0
        self.dist = 0
