import graphviz as gv
import RabinKarpHash as hash
import perfection.czech
import MinimalPerfectHashing as mph


def construct_de_bruijn_graph(kmer, k):
    edges = []
    nodes = set()
    node_hash_values = {}
    min_value_list = []
    string_hash_map = {}
    hash_set = set()
    rabinKarp_to_mph = {}
    str_to_mph = {}
    for i in range(len(kmer)-k+1):
        edges.append([kmer[i:i + k - 1], kmer[i + 1:i + k]])
        nodes.add(kmer[i:i + k - 1])
        nodes.add(kmer[i + 1:i + k])
        node_hash_values.update({kmer[i:i + k - 1]:hash.rabin_karp_hash(kmer[i:i + k - 1])})
        node_hash_values.update({kmer[i + 1:i + k]:hash.rabin_karp_hash(kmer[i + 1:i + k])})

  #  visualize_de_bruijn_graph(nodes, edges)

    hash_set = set(node_hash_values.values())
    if (len(hash_set) == len(node_hash_values)):
        #print(hash_set)
        #print("Distinct hashed values by rabin karp")
        rabinKarp_to_mph = mph.mph([str(i) for i in node_hash_values.values()])
    else:
        print("Duplicate hashed values by rabin karp")

    #print(node_hash_values)

    for Xkmer,rkpVal in node_hash_values.iteritems():
        #print Xkmer, rkpVal
        #print("str to mph")
        #print(str_to_mph)
        str_to_mph.update({Xkmer:rabinKarp_to_mph.get(str(rkpVal))})

    #print("str to mph")
    #print(str_to_mph)

    # if len(set(node_hash_values.values())) == len(node_hash_values.values()):
    #     print("true")
    return nodes, edges, str_to_mph


def visualize_de_bruijn_graph(nodes, edges):
    t = gv.Digraph()
    for edge in edges:
        t.edge(edge[0], edge[1])
    t.render('GraphImage')





