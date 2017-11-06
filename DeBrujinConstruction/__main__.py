import GraphConstruction


def main():
    nodes, edges = GraphConstruction.construct_de_bruijn_graph("ACGCGTCG", 5)
    print(nodes)
    print(edges)


if __name__ == "__main__":
    main()
