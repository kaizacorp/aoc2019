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

    # print("Total orbits :",  direct_orbits + indirect_orbits)

    # find common parent between 'YOU' and 'SAN

    parent_YOU = list(G.successors('YOU'))[0]
    parent_SAN = list(G.successors('SAN'))[0]
    # print(parent_YOU, parent_SAN)

    ancestors = []

    while parent_YOU != root:
        ancestors.append(parent_YOU)
        parent_YOU = list(G.successors(parent_YOU))[0]

    # print(ancestors)

    while parent_SAN not in ancestors:
        parent_SAN = list(G.successors(parent_SAN))[0]

    common_ancestor = parent_SAN
    # print(common_ancestor)

    start_YOU = list(G.successors('YOU'))[0]
    start_SAN = list(G.successors('SAN'))[0]
    start = []
    start.append(start_YOU)
    start.append(start_SAN)

    min_transfers = 0
    for parent in start:
        while parent != common_ancestor:
            min_transfers += 1
            parent = list(G.successors(parent))[0]

    print(min_transfers)


if __name__ == "__main__":
    main()
