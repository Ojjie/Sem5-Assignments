#!/usr/bin/python3

import sys

infile = sys.stdin
v = open(sys.argv[1], 'r')

page_rank_dict = {}
page_ranks = v.readlines()
for line in page_ranks:
    page, rank = line.split(', ')
    page_rank_dict[page] = rank

for line in infile:
    from_node, adj_list = line.split('\t')
    adj_list = adj_list.strip('][\n').split(', ')

    importance = int(page_rank_dict[from_node]) / len(adj_list)
    for node in adj_list:
        print("%s,%s,%s"%(node, from_node, importance))
