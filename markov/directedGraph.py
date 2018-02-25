import numpy as np
import bmatrix

class DirectedGraph:

    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def number_of_nodes(self):
        return len(self.nodes)

    def add_node(self, label):
        n = self.number_of_nodes() + 1
        self.nodes[n] = label

    def add_edge(self, node_from, node_to):
        if node_from in self.edges:
            self.edges[node_from] = self.edges[node_from] + [node_to]
        else:
            self.edges[node_from] = [node_to]

    def add_nodes(self, node_list):
        for label in node_list:
            self.add_node(label)

    def add_edges(self, node, node_list):
        for terminal_node in node_list:
            self.add_edge(node, terminal_node)

    def number_of_nodes(self):
     return len(self.nodes)

    def valence(self,node):
        return len(self.edges[node])

    def points_to(self, source, target):
        if target in self.edges[source]:
            return True
        else:
            return False

    def matrix(self):
        nodes = self.edges.keys()
        rows = []
        for row_node in nodes:
            row = []
            print [row_node, self.edges[row_node]]
            for column_node in nodes:
                if self.points_to(column_node, row_node):
                    entry = 1.0/self.valence(column_node)
                else:
                    entry = 0
                row.append(entry)
            rows.append(row)
        return np.array(rows)

    def bmatrix(self):
        return bmatrix.bmatrix(self.matrix())
