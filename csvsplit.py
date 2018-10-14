#!/usr/bin/env python3
import re
import sys
import argparse

parser = argparse.ArgumentParser(description='Break a single-row csv into multiple rows based on a repeating pattern')
parser.add_argument("in_csv", help="The single-row csv file")
parser.add_argument("--pattern", default='^[0-9]{13}$', help="The pattern that appears in each row")
args = parser.parse_args()

# Get data from file
with open(args.in_csv, 'r') as f:

    # this tool will become confused if there are commas in the fields
    # TODO: make it smarter by parsing the csv properly in the first place
    data = f.read().split(',')

# Find sentinels
pattern = re.compile(args.pattern)
sentinels = []
for idx, field in enumerate(data):
    if pattern.search(field.strip()):
        sentinels.append(idx)

# Assume that the depth of the first sentinel represents the offset for the first row
#offset = sentinels[0]

# Actually, just start with the sentinel, this will prevent the error codes from wrapping
offset = 0

# Collect rows
rows = []
for this_one, next_one in zip(sentinels, sentinels[1:]):
    start = this_one - offset
    end = next_one - offset
    rows.append(data[start:end])

# including the last one
rows.append(data[end:])

# Print them to stdout
for row in rows:
    try:
        if row[13] == '0':
            for i in range(5):
                row.insert(8,'')
        print(','.join(row))
    except IndexError:
        print("ERROR on row:")
        print(','.join(row))

# Warn if called with no redirection
if sys.stdout.isatty():
    print("\nTo make a csv file from this output, try:\n" + ' '.join(sys.argv) + " > out.csv")
