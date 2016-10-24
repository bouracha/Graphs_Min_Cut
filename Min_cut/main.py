from edgeMap import edgeMap
from contraction import contraction_nodes
from contraction import contractionEdges

from random import randint

import numpy as np

### Main ###

result_file = r'input.txt'
with open(result_file) as file:
    Vertices = [[int(digit) for digit in line.split()] for line in file]

print "Creating Edge Map...."
Edges, m = edgeMap(Vertices)

print "Edge map created, starting iterations..."

minCut = 1000
for j in range(0, 40000):
    Edges, m = edgeMap(Vertices)
    for i in range(0, len(Vertices)-2):
        #print "Iteration Number: ", i, " with", m, "edges remaining."

        #Choose which edge to contract:
        r = randint(1, m-1)  #time is seed by default
        u = Edges[r][0]
        v = Edges[r][1]

        #Delete Edge being contracted
        Edges = np.delete(Edges, r, axis=0)
        m -= 1

        #Update the Vertices adjacency list, not necessary
        #Vertices = contraction_nodes(Vertices, u, v)

        #Update Edges
        Edges, m = contractionEdges(Edges, u, v, m)

    if m < minCut:
        minCut = m

    print "Iteration", j, "minCut =", minCut, "m =", m

print "...iterations complete."

print "MinCut =", minCut
#print "Contracted array:", Vertices
#print "Edges: ", Edges