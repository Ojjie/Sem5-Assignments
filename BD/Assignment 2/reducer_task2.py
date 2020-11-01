import sys

infile = sys.stdin
current_node = None
current_sum = None

for line in infile:

    from_node, to_node, value = line.split(',')
    from_node = int(from_node)
    to_node = int(to_node)
    value = float(value)

    if current_node == None:
        current_node = from_node
        current_sum = value
        continue

    elif current_node == from_node:
        current_sum = current_sum + value

    elif current_node != from_node:
        rank = 0.15 + 0.85 * current_sum
        print('%s, %.5f'%(current_node, rank))
        current_node = from_node
        current_sum = value

rank = 0.15 + 0.85 * current_sum
print('%s, %.5f'%(current_node, rank))
