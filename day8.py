from collections import namedtuple
import sys

sys.setrecursionlimit(5000)

with open("day8.txt") as f:
    data = list(map(int, f.read().strip().split(' ')))

Node = namedtuple("Node", "child_nodes metadata_entries")

def create_node(i):
    num_child_nodes = data[i]
    num_metadata_entries = data[i+1]
    i += 2
    child_nodes = []
    metadata_entries = []

    for _ in range(num_child_nodes):
        node, i = create_node(i)
        child_nodes.append(node)
    
    for _ in range(num_metadata_entries):
        metadata_entries.append(data[i])
        i += 1
    
    return Node(child_nodes, metadata_entries), i

root, _ = create_node(0)

def node_sum(node):
    return sum(node.metadata_entries) + sum(map(node_sum, node.child_nodes))

print(node_sum(root))

def node_value(node):
    if len(node.child_nodes) == 0:
        return sum(node.metadata_entries)
    ans = 0
    for i in node.metadata_entries:
        if i-1 < len(node.child_nodes):
            ans += node_value(node.child_nodes[i-1])
    return ans

print(node_value(root))

