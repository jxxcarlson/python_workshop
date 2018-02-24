from network import Network
import numpy as np



net = Network()

net.add_nodes(["A", "B", "C", "D"])

net.add_edges(1, [2,3,4])
net.add_edges(2, [3,4])
net.add_edges(3, [1])
net.add_edges(4, [1, 3])

print "Nodes: " + str(net.nodes)
print "Edges: " + str(net.edges )
print "Valence of node 1 = " + str(net.valence(1))
print "2 points to 1 = " + str(net.points_to(2,1 ))
print "1 points to 2 = " + str(net.points_to(1,2 ))
print "ITEMS: " + str(net.edges.items())
print "MATRIX: " + str(net.matrix())
print "BMATRIX: " + str(net.bmatrix())
