#!/usr/bin/python3

import sys

current_count = 0
current_country = ""
#word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    country = line.split('\t')[0]
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

    if country == current_country:
        current_count += count
    else:
        if current_country:
            print('%s,%s'%(current_country,current_count))
        current_country = country
        current_count = count


print('%s,%s'%(current_country,current_count))
