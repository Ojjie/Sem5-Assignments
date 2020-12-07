#!/usr/bin/python3

import sys
import datetime

true = 'true'
false = 'false'
infile = sys.stdin
current_word = sys.argv[1]

# input comes from STDIN (standard input)
for line in infile:
    # remove leading and trailing whitespace
        line = line.strip()
    # split the line into words based on the ',' delimiter
        value="0"
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

        recognized = line['recognized']
        timestamp = line['timestamp'][:10].split('-')

        day = datetime.datetime(int(timestamp[0]), int(timestamp[1]), int(timestamp[2])).weekday()
        #print(recognized)

        if recognized == 'true':
            value="1"
            print ('%s\t%s' % (1, value)) #word, 1, 1

        else:
            if day >= 5 and day <= 6 and recognized == 'false':
                value="1"
                print ('%s\t%s' % (0, value)) #word, 1, 0
