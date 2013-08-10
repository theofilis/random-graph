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

def childs(m):
    p = random.randint(0, m);
    return p

def genareteCaterpillarTree(n, m):
    T = nx.path_graph(n)

    label = n
    for i in range(n):
        k = childs(m)
        for j in range(k):
            label = label + 1
            T.add_edge(i, j)

    return T

