import GraphConstruction
import In_Out_Matrix
import StaticRabinKarp
import perfection.czech

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
    nodes, edges, string_hash_map = GraphConstruction.construct_de_bruijn_graph(fileData, k)
    print("No. of nodes in de brujin graph", len(nodes))
   # print(edges)
    In_Out_Matrix.construct_in_out_matrix(nodes, edges, string_hash_map)



if __name__ == "__main__":
    main()
