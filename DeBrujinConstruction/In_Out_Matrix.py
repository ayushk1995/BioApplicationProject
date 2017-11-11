import BitArray2D
from BitArray2D import godel


def construct_in_out_matrix(nodes, edges, string_hash_map):
    in_matrix = BitArray2D.BitArray2D(rows=len(nodes), columns=5)
    out_matrix = BitArray2D.BitArray2D(rows=len(nodes), columns=5)
    column_char_map = {}
    column_char_map.update({'A':0})
    column_char_map.update({'C': 1})
    column_char_map.update({'G': 2})
    column_char_map.update({'T': 3})
    column_char_map.update({'N': 4})

    print(in_matrix.size())

    for str in nodes:
        for v1,v2 in edges:
            if v2==str:
                in_matrix.__setitem__((string_hash_map.get(str), column_char_map.get(v1[0])), 1)

            if v1==str:
                out_matrix.__setitem__((string_hash_map.get(str), column_char_map.get(v2[len(v2)-1])), 1)

    print("In Matrix")
    print(in_matrix)
    print("************************************")
    print("Out Matrix")
    print(out_matrix)
