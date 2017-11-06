import gvmagic
from graphviz import Digraph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot


def construct_de_bruijn_graph(str, k):
    edges = []
    nodes = set()
    for i in range(len(str)-k+1):
        edges.append([str[i:i+k-1], str[i+1:i+k]])
        nodes.add(str[i:i+k-1])
        nodes.add(str[i+1:i+k])
    visualize_de_bruijn_graph(nodes, edges)
    return nodes, edges


def visualize_de_bruijn_graph(nodes, edges):
    G = nx.DiGraph()
    for edge in edges:
        G.add_edges_from(edge)
    nx.write_dot(G, 'graph.dot')
#    pos = nx.spring_layout(G)
#    nx.draw_networkx_nodes(G, pos, label=node,  node_size=1000)
#    nx.draw_networkx_edges(G, pos,arrows=True)
#    nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')
#
#     plt.show()








#        dot = Digraph(comment='De Bruijn Grpaph')
 #       for node in nodes:
  #          dot.node(node)
   #     for edge in edges:
    #        dot.edges(edge)
     #   print(dot.source)


# dot_str = 'digraph "DeBruijn graph" {\n'
#    for node in nodes:
#        dot_str += '   %s  [label="%s"];\n' % (node, node)
#    for src, dst in edges:
#        dot_str += '%s -> %s ;\n' % (src, dst)
#    return dot_str + '}\n'  '''
