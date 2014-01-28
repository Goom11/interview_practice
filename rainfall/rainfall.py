#!/usr/bin/python

def get_neighbors(node, farmland):
    # This could be replaced with a list comprehension, no time atm
    nodes = [node]
    n = len(farmland)
    i, j = node
    if j > 0:
        nodes.append((i, j - 1))
    if j < n - 1:
        nodes.append((i, j + 1))
    if i > 0:
        nodes.append((i - 1, j))
    if i < n - 1:
        nodes.append((i + 1, j))
    if j > 0 and i > 0:
        nodes.append((i - 1, j - 1))
    if j < n - 1 and i > 0:
        nodes.append((i - 1, j + 1))
    if j > 0 and i < n - 1:
        nodes.append((i + 1, j - 1))
    if j < n - 1 and i < n - 1:
        nodes.append((i + 1, j + 1))
    return nodes

def get_min_node(node_to_elevation):
    # neg inf or -1 both work i think cause no negative elevations
    min_node = (-1, -1, float("inf"))
    for node, elevation in node_to_elevation.iteritems():
        i, j, e = min_node
        if elevation < e:
            new_i, new_j = node
            min_node = (new_i, new_j, elevation)
    i, j, e = min_node
    return (i, j)

def find_lowest_neighbor(node, farmland):
    # easy peasy lemon squeesy
    i, j = node
    n = len(farmland)
    nodes = get_neighbors(node, farmland)
    # yay dict comprehensions
    node_to_elevation = {(i, j): farmland[i][j] for i,j in nodes}
    return get_min_node(node_to_elevation)

def traverse(cur_node, basins, farmland):
    next_node = find_lowest_neighbor(cur_node, farmland)
    traversed_nodes = []
    traversed_nodes.append(cur_node)
    # Traverse each node until you are at a sink or at a node that we've already traversed
    while next_node != cur_node and next_node not in basins:
        cur_node = next_node
        traversed_nodes.append(cur_node)
        next_node = find_lowest_neighbor(cur_node, farmland)
    # set sink to point to itself
    if cur_node == next_node:
        basins[cur_node] = cur_node
    # for each node, set its sink to be the sink of the last node we traversed
    for node in traversed_nodes:
        basins[node] = basins[next_node]
    return basins

def get_basins(farmland):
    basins = {}
    n = len(farmland)
    for i in xrange(n):
        for j in xrange(n):
            node = (i, j)
            if node not in basins:
                #only need to traverse the node if it hasn't already been traversed
                basins = traverse(node, basins, farmland)
    return basins

def reverse_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.iteritems():
        output_dict.setdefault(value, []).append(key)
    return output_dict

def basins_to_size(basins):
    # this is for efficiency cause if you reverse it then its faster for sorting
    sinks_to_nodes = reverse_dict(basins)
    return [len(nodes) for sink, nodes in sinks_to_nodes.iteritems()]

def run():
    # get input
    n = int(raw_input())
    farmland = [map(int, raw_input().split()) for _ in xrange(n)]
    # basins is a dict of all N^2 nodes to their sinks
    basins = get_basins(farmland)
    # result is the unsorted list of basin sizes
    result = basins_to_size(basins)
    result.sort(reverse=True)
    for l in result:
        print l,

if __name__ == "__main__":
    # O(N^2)
    run()
