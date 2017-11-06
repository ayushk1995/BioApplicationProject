import graphviz as gv


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
    t = gv.Digraph()
    for edge in edges:
        t.edge(edge[0], edge[1])
    t.render('GraphImage')


