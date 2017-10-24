import gvmagic
from graphviz import Digraph


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
        dot = Digraph(comment='De Bruijn Grpaph')
        for node in nodes:
            dot.node(node)
        for edge in edges:
            dot.edges(edge)
        dot.source

# dot_str = 'digraph "DeBruijn graph" {\n'
#    for node in nodes:
#        dot_str += '   %s  [label="%s"];\n' % (node, node)
#    for src, dst in edges:
#        dot_str += '%s -> %s ;\n' % (src, dst)
#    return dot_str + '}\n'  '''
