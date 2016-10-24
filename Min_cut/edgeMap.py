

def edgeMap(Vertices):
    Edges = []

    edgeCount = 0
    for node in range(0, len(Vertices)):
        for partnerNode in range(1, len(Vertices[node])):
            if Vertices[node][partnerNode] > node:
                Edges.append([])
                Edges[edgeCount].append(Vertices[node][0])
                Edges[edgeCount].append(Vertices[node][partnerNode])
                edgeCount += 1

    m = len(Edges)
    #print "Number of Edges created (m) =", m
    #print "Edges array: ", Edges

    return Edges, m