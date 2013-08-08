"""
SYNOPSIS

DESCRIPTION
    
EXAMPLES

AUTHOR

    Theofilis George <theofilis.g@gmail.com>

LICENSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    1
"""

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