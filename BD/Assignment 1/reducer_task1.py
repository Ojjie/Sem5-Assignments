#!/usr/bin/python3

import sys

current_count_rec = 0
current_count_unrec = 0
#word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    recognized = line.split('\t')[0]
    count = line.split('\t')[1]

    #print(type(recognized))

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so we discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer

    #global current_word
    #global current_count

    if recognized == '1':
        current_count_rec += count
    else:
        current_count_unrec += count

print("%s\n%s"%(current_count_rec, current_count_unrec))
