import graphviz as gv
import RabinKarpHash as hash
import perfection.czech


def construct_de_bruijn_graph(str, k):
    edges = []
    nodes = set()
    node_hash_values = {}
    min_value_list = []
    string_hash_map = {}
    for i in range(len(str)-k+1):
        edges.append([str[i:i+k-1], str[i+1:i+k]])
        nodes.add(str[i:i + k - 1])
        nodes.add(str[i+1:i+k])
        node_hash_values.update({str[i:i + k - 1]:hash.rabin_karp_hash(str[i:i + k - 1])})
        node_hash_values.update({str[i+1:i+k]:hash.rabin_karp_hash(str[i+1:i+k])})

    visualize_de_bruijn_graph(nodes, edges)
    perfect_hash = perfection.make_hash(node_hash_values.values())

    for i in node_hash_values.values():
        min_value_list.append(perfect_hash(i))

    for x in range(len(min_value_list)):
        string_hash_map.update({node_hash_values.keys()[x]:min_value_list[x]})

    print(string_hash_map)
    print(min_value_list)
    min_value_list.sort()
    print(node_hash_values.values())
    print(min_value_list)
    print(node_hash_values)
    if len(set(node_hash_values.values())) == len(node_hash_values.values()):
        print("true")
    return nodes, edges, string_hash_map


def visualize_de_bruijn_graph(nodes, edges):
    t = gv.Digraph()
    for edge in edges:
        t.edge(edge[0], edge[1])
    t.render('GraphImage')





