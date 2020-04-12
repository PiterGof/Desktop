import pickle
def file(name):
    with open(name, 'rb') as f:
        graph = pickle.load(f)
    return graph

def check(v, w, graph):
    if graph[int(v) - 1][int(w) - 1] == 1 or graph[int(w) - 1][int(v) - 1] == 1:
        return True
    return False

def commmon_vertex(v, graph):
    q = {}
    p = []
    for i in range(len(graph[int(v) - 1])):
        if graph[int(v) - 1][i] == 1:
            q[i + 1] = 1
    for i in q:
        p.append(i)
    return p

def weight_vertex(v, graph):
    return sum(graph[int(v) - 1])

def weight_edge(v, w, graph):
    if graph[int(v) - 1][int(w) - 1] == 1:
        sum_v = sum(graph[int(v) - 1])
        sum_w = sum(graph[int(w) - 1])
        return (sum_v + sum_w) / 2
    return False

def edges(v, w, graph):
    array= []
    if graph[int(v) - 1][int(w) - 1] == 1:
        return v+w
    return False

