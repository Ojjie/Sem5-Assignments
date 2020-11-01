#!/usr/bin/python3

import sys

infile = sys.stdin
current_from_node = None
current_to_node = None
adj_list = []

v = open(sys.argv[1], 'w')

for line in infile:
    from_node, to_node = line.split(',')
    to_node = int(to_node[:-1])

    if current_to_node == to_node:
        continue

    elif current_from_node == from_node:
        adj_list = adj_list + [to_node]
        continue

    else:
        if current_to_node != None:
            print('%s\t%s'%(current_from_node, adj_list))
            v.write('%s, 1\n'%current_from_node)
        current_from_node = from_node
        current_to_node = to_node
        adj_list = [to_node]
