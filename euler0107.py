# Minimal network
# Problem 107
#
# The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
#
#            B        20       E
#             +---------------+
#            / \             / \
#           /   \           /   \
#          /     \         /     \
#      16 /    17 \       / 18    \ 11
#        /         \     /         \
#       /           \   /           \
#      /             \ /             \
#   A +---------------+---------------+ G
#      \     21      / \      23     /
#       \           / D \           /
#        \         /     \         /
#      12 \    28 /       \ 19    / 27
#          \     /         \     /
#           \   /           \   /
#            \ /             \ /
#             +---------------+
#            C        31       F
#
# The same network can be represented by the matrix below.
#
#       A   B   C   D   E   F   G
#   A   -   16  12  21  -   -   -
#   B   16  -   -   17  20  -   -
#   C   12  -   -   28  -   31  -
#   D   21  17  28  -   18  19  23
#   E   -   20  -   18  -   -   11
#   F   -   -   31  19  -   -   27
#   G   -   -   -   23  11  27  -
#
# However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 - 93 = 150 from the original network.
#
#            B                 E
#             +               +
#            / \             / \
#           /   \           /   \
#          /     \         /     \
#      16 /    17 \       / 18    \ 11
#        /         \     /         \
#       /           \   /           \
#      /             \ /             \
#   A +               +               + G
#      \               \
#       \             D \
#        \               \
#      12 \               \ 19
#          \               \
#           \               \
#            \               \
#             +               +
#            C                 F
#
# Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

import csv;
import Queue;
import sys;
import time;

start_time = time.time();

class EdgeTo(object):
    to_node = None;
    weight = None;
    def __init__(self, to_node, weight):
        self.to_node = to_node;
        self.weight = weight;
    def __str__(self):
        return '-w=%d-{n=%d}' % (self.weight, self.to_node);
    def __repr__(self):
        return str(self);

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

def print_graph(graph):
    node_count = len(graph);
    for node in range(node_count):
        edges_string = "";
        for edge_to in graph[node]:
            edges_string += str(edge_to) + ', '
        edges_string = edges_string[:-2];
        print "%d: %s" % (node, edges_string);

def get_total_weight(graph):
    total_weight_times_2 = 0;
    for edge_to_list in graph:
        for edge_to in edge_to_list:
            total_weight_times_2 += edge_to.weight;
    return total_weight_times_2 / 2;

def is_graph_connected(graph):
    connected = False;
    node_count = len(graph);
    queue = Queue.Queue();
    unvisited = [True] * node_count;
    queue.put(0);
    unvisited[0] = False;
    while not queue.empty():
        node = queue.get();
        for edge_to in graph[node]:
            if unvisited[edge_to.to_node]:
                queue.put(edge_to.to_node);
                unvisited[edge_to.to_node] = False;
    connected = (0 == unvisited.count(True));
    return connected;

def find_edge_index(edge_to_list, to_node):
    edge_index = -1;
    edge_count = len(edge_to_list);
    for index in range(edge_count):
        if edge_to_list[index].to_node == to_node:
            edge_index = index;
            break;
    return edge_index;

def remove_edge(graph, node, to_node):
    edge_removed = False;
    node_edge_to_list = graph[node];
    node_edge_index = find_edge_index(node_edge_to_list, to_node);
    to_node_edge_to_list = graph[to_node];
    to_node_edge_index = find_edge_index(to_node_edge_to_list, node);
    if node_edge_index >= 0 and to_node_edge_index >= 0:
        del node_edge_to_list[node_edge_index];
        del to_node_edge_to_list[to_node_edge_index];
        edge_removed = True;
    return edge_removed;

def remove_minimum_weight_edge(graph):
    minimum_weight = sys.maxint;
    minimum_weight_node = -1;
    minimum_weight_to_node = -1;
    node_count = len(graph);
    for node in range(node_count):
        edge_to_list = graph[node];
        edge_count = len(edge_to_list);
        for index in range(edge_count):
            if edge_to_list[index].weight < minimum_weight:
                minimum_weight = edge_to_list[index].weight;
                minimum_weight_node = node;
                minimum_weight_to_node = edge_to_list[index].to_node;
    remove_edge(graph, minimum_weight_node, minimum_weight_to_node);
    return (minimum_weight_node, minimum_weight_to_node, minimum_weight);

# Joins the set containing node_a with the set containing node_b. Returns whether the sets were successfully joined. If the 
# nodes are already in the same set, returns False (considered a failure).
def join_sets_containing(sets, node_a, node_b):
    success = False;
    set_count = len(sets);
    set_a_index = -1;
    set_b_index = -1;
    for set_index in range(set_count):
        current_set = sets[set_index];
        if node_a in current_set:
            set_a_index = set_index;
        elif node_b in current_set:
            set_b_index = set_index;
        if set_a_index >= 0 and set_b_index >= 0:
            success = True;
            break;
    if success:
        if set_a_index == set_b_index:
            success = False;
        else:
            sets[set_a_index] = sets[set_a_index].union(sets[set_b_index]);
            del sets[set_b_index];
    return success;

FILENAME = 'p107_network_toy.txt';
FILENAME = 'p107_network.txt';

graph = [];
with open(FILENAME) as network_file:
    network_reader = csv.reader(network_file);
    for line in network_reader:
        graph.append([]);
        to_node = 0;
        for element in line:
            if element.isdigit():
                graph[-1].append(EdgeTo(to_node, int(element)));
            to_node += 1; 
graph_weight = get_total_weight(graph);

# Kruskal's Algorithm.
node_count = len(graph);
minimum_spanning_tree = [];
for node in range(node_count):
    minimum_spanning_tree.append([]);
sets = [];
for node in range(node_count):
    node_set = set();
    node_set.add(node);
    sets.append(node_set);
minimum_spanning_tree_final_edge_count = node_count - 1;
minimum_spanning_tree_edge_count = 0;
while minimum_spanning_tree_edge_count < minimum_spanning_tree_final_edge_count:
    (minimum_weight_node, minimum_weight_to_node, minimum_weight) = remove_minimum_weight_edge(graph);
    if join_sets_containing(sets, minimum_weight_node, minimum_weight_to_node):
        minimum_spanning_tree[minimum_weight_node].append(EdgeTo(minimum_weight_to_node, minimum_weight));
        minimum_spanning_tree[minimum_weight_to_node].append(EdgeTo(minimum_weight_node, minimum_weight));
        minimum_spanning_tree_edge_count += 1;
minimum_spanning_tree_weight = get_total_weight(minimum_spanning_tree);
savings = graph_weight - minimum_spanning_tree_weight;
print;
print 'savings = original weight - minumum weight = %d - %d = %d.' % (graph_weight, minimum_spanning_tree_weight, savings);
print;

print_execution_time();
