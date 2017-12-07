import GraphConstruction
import In_Out_Matrix
import StaticRabinKarp as rk
import perfection.czech
import MinimalPerfectHashing as mph

def compute_permutation(permuted_set):
    new_permuted_set = set()
    list = ['A', 'C', 'G', 'T']
    for char in list:
        for str in permuted_set:
            new_permuted_set.add(char + str)
    return new_permuted_set


def main():
    k = input("Enter the value of K:")
   # permuted_set = set(['A', 'C', 'G', 'T'])
   # for i in range(k-1):
    #    permuted_set = compute_permutation(permuted_set)
    #print(permuted_set)
    #print(len(permuted_set))
    #hash_set = StaticRabinKarp.static_rabin_karp(permuted_set)
    #print(hash_set)
    #perfect_hash = perfection.make_hash(hash_set.values())

    fileData = open("test.txt", "r").read().replace('\n', '')
    #print(fileData)
    nodes, edges, string_hash_map, node_hash_values = GraphConstruction.construct_de_bruijn_graph(fileData, k)
    # print(nodes)
    # print(string_hash_map)
    print("No. of nodes in de brujin graph", len(nodes))
   # print(edges)
    In_Out_Matrix.construct_in_out_matrix(nodes, edges, string_hash_map)
    print("Enter the nodes you want to add, with the size k")
    s = raw_input("Enter the nodes you want to add, seprated by space, with the size k")
    inserted_nodes = [i for i in s.split()]
    str_to_rk = rk.static_rabin_karp(set(inserted_nodes))
    new_str_to_rk = str_to_rk.copy()
    new_str_to_rk.update(node_hash_values)
    print("computing mph")
    # print(mph.mph(new_str_to_rk))



if __name__ == "__main__":
    main()
