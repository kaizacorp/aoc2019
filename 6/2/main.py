import sys
import networkx as nx


def main():
    filename = sys.argv[1]
    orbit_codes = open(filename).read().split('\n')
    orbits = []
    G = nx.DiGraph()

    for code in orbit_codes:
        code = code.split(')')
        orbits.append((code[1], code[0]))

    G.add_edges_from(orbits)

    direct_orbits = 0
    for (planet, orbiters) in G.out_degree:
        if orbiters == 0:
            root = planet
        direct_orbits += orbiters

    indirect_orbits = 0
    for planet in G.nodes():
        while not(planet is root):
            parent = list(G.successors(planet))
            if root in parent:
                planet = root
            else:
                indirect_orbits += 1
                planet = parent[0]

    print("Total orbits :",  direct_orbits + indirect_orbits)
    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    # print(G.edges())
    # print(G.in_degree)
    # print(G.out_degree)


if __name__ == "__main__":
    main()
