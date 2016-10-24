import numpy as np

def contraction_nodes(Vertices, u, v):

    # newVertices =  np.delete(Vertices, u-1, axis=0) #need to generalise
    #newVertices = np.delete(Vertices, v - 1, axis=0)  # need to generalise
    newVertices = Vertices

    #append v's neighbours to supernode u's neighbours
    uArray = []
    for x in range(0, len(Vertices[u - 1])):  # need to generalise
        if Vertices[u-1][x] != v:
            uArray.append(Vertices[u - 1][x])  # need to generalise
    for x in range(0, len(Vertices[v - 1])):  # need to generalise
        if Vertices[v-1][x] != u and Vertices[v-1][x] != v:
            uArray.append(Vertices[v - 1][x])  # need to generalise

    newVertices[u - 1] = uArray
    newVertices[v - 1] = []


    #Change node index to supernode index which has been contracted to u
    for node in range(0, len(newVertices)):
        for partnerNode in range(1, len(newVertices[node])):
            for i in range(0, len(newVertices[u-1])):  # need to generalise
                if newVertices[node][partnerNode] == v:  # need to generalise
                    newVertices[node][partnerNode] = u  # need to generalise


    return newVertices

def contractionEdges(Edges, u, v, m):
    j = 0
    while j < m:
        #All edges that had an endpoint at v now point to u:
        for k in range(0, 2):
            if Edges[j][k] == v:
                Edges[j][k] = u
        #Delete ALL self loops
        if (Edges[j][0] == u and Edges[j][1] == v) or (Edges[j][0] == v and Edges[j][1] == u) or (
            Edges[j][0] == Edges[j][1]):
            Edges = np.delete(Edges, j, axis=0)
            m -= 1
            j -= 1
        j += 1
    m = len(Edges)
    # print "Number of edges remaing: ", m

    return Edges, m