# VRP

The capacitated vehicle routing problem (CVRP or simply VRP) is one of the most studied combinatorial optimization problems in the literature of operations research. The main reason for this much attention is the abundance of its real-life applications in distribution logistics and transportation.

# Problem Description
Consider a central warehouse (Node with id: 0) and a set of 𝑛 = 100 customers (Nodes with id: 1,…, 𝑛 = 100).
Vehicles are based in the central warehouse.
The aim is to build a route for each of the vehicles in order to serve the customers.
Each route starts from the central warehouse and visits the various customers. The route ends at the last customer visiting the vehicle.
Each order must be satisfied by one and only one visit of a vehicle. Therefore, when a vehicle visits a customer, it carries to him all the products of his order.
Each vehicle has a specific product capacity, so the goods carried by the vehicle must not exceed the maximum capacity it.
Assume that the vehicles travel at 35 km/hr and that for each customer, the time to unload the goods is 15 minutes.

The following vehicles are available in the warehouse: <br/>
a) 15 trucks with a maximum capacity of 1500 kg <br/>
b) 15 trucks with a maximum capacity of 1200 kg<br/>

Each route has a total time limit of 3.5 ℎ𝑟.
The goal is that the routes generated minimize the total distance traveled by the trucks.

# How to run the code:
    python Main.py
