#!/usr/bin/python3

import sys

infile = sys.stdin

for line in infile:
    if line[0] == "#":                          #to ignore comments
        continue
    try:
        from_node, to_node = line.split('\t')       #formatting inputs and handling exceptions
    except:
        continue

    to_node = int(to_node[:-2])
    print('%s,%s'%(from_node, to_node))
