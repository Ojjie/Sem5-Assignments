#!/usr/bin/python3

import sys

true = 'true'
false = 'false'
infile = sys.stdin

current_word = sys.argv[1]
current_distance = sys.argv[2]
# input comes from STDIN (standard input)
for line in infile:
    # remove leading and trailing whitespace
        line = line.strip()

        exec('line ='+line)

        if not line['word'].replace(' ', '').isalpha() or line['word'] != current_word:
            continue
        else:
            if not line['countrycode'].isalpha() or not line['countrycode'].isupper() or len(line['countrycode']) != 2:
                continue
            else:
                if line['recognized'] != 'true' and line['recognized'] != false:
                    continue
                else:
                    if not line['key_id'].isnumeric() or len(line['key_id']) != 16:
                        continue
                    else:
                        if len(line['drawing']) < 1:
                            continue
                        else:
                            for i in line['drawing']:
                                if len(i) != 2:
                                    continue

        country = line['countrycode']
        drawing = line['drawing']
        distance = (drawing[0][0][0]**2 + drawing[0][1][0]**2)**0.5
        if distance > float(current_distance):
            print('%s\t%s'%(country, 1))
