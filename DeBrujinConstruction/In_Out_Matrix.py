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
    
    char_column_map = dict((v, k) for k, v in column_char_map.iteritems())


    print(in_matrix.size())

    # for str in nodes:
    count = 0;
    for v1, v2 in edges:
        in_matrix.__setitem__((string_hash_map.get(v2), column_char_map.get(v1[0])), 1)
        out_matrix.__setitem__((string_hash_map.get(v1), column_char_map.get(v2[len(v2) - 1])), 1)
        count+=1;
        # print(count)

    print("In Matrix")
    #print(in_matrix)
    print("************************************")
    print("Out Matrix")
    #print(out_matrix)

    #print(string_hash_map.get("TAC"))
    #in_column_header = return_column_headers_In("TAC", in_matrix, out_matrix, string_hash_map, char_column_map)
    #out_column_header = return_column_headers_Out("TAC", in_matrix, out_matrix, string_hash_map, char_column_map)
    #print(In_column_header)
    #print(Out_column_header)


def return_column_headers_In(kmer, in_matrix, out_matrix, str_to_mph, char_column_map):
    kmer_to_column_header = {}
    column_header_set = set()
    mph_val = str_to_mph.get(kmer)
    for j in range(5):
        if (in_matrix[godel(mph_val, j)]==1):
            column_header_set.add(char_column_map.get(j))

    return column_header_set


def return_column_headers_Out(kmer, in_matrix, out_matrix, str_to_mph, char_column_map):
    kmer_to_column_header = {}
    column_header_set = set()
    mph_val = str_to_mph.get(kmer)
    for j in range(5):
        if (out_matrix[godel(mph_val, j)]==1):
            column_header_set.add(char_column_map.get(j))

    return column_header_set




