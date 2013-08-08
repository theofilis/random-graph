import networkx as nx
import matplotlib.pyplot as plt
import random

def g(a,b):
    p = random.random();
    if p < a:
        return 0
    elif p < b:
        return 1
    else:
        return 2

def genareteRandomBinaryTree(n, a,b):
    T = nx.Graph()
    T.add_node(0)
    label = 0
    while n > 0:
        y = random.sample(T.nodes(), 1)

        if len(T.neighbors(y[0])) <= 1:
            k = g(a,b)
        elif len(T.neighbors(y[0])) == 2:
            k = round(g(a,b)/2)
        else:
            continue

        for i in range(k):
            label += i + 1
            print ("node ", label)
            T.add_edge(y[0], label)

        n -= k

    return T

T = genareteRandomBinaryTree(30, 0, 0.5)
nx.draw(T)
plt.show()