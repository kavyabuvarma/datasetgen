#!/usr/bin/env python

import sys
import json
import random
import string

print("dataset generator")

arg_len = len(sys.argv) - 1
try:
    if arg_len != 0:
        file_size_mb = int(sys.argv[1])
    else:
        print("default file size - 1 mb")
        file_size_mb = 1
except ValueError:
    print("Usage : main.py [filesize_mb] ")

print("Generating file of size ", str(file_size_mb), "mb with columns first_name, last_name, address, date_of_birth")

f = open("samplevalues.json", "r")
json_str = f.read()
f.close()

sample_values_json = json.loads(json_str)


def generate_rand_value() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 10)))


post_codes = sample_values_json["Postcodes"]

lines = ["first_name,last_name,address,date_of_birth"]
for i in range(0, 20000):
    lines.append(str(generate_rand_value() + ',' + generate_rand_value() + ',' +
                     generate_rand_value() + ' ' + generate_rand_value() + ' ' + random.choice(post_codes))
                 + ',' + str(random.choice(range(1, 30))).zfill(2) + '-' + str(random.choice(range(1, 12))).zfill(2)
                 + '-' + str(random.choice(range(1950, 2019))))

fw = open("out/data_" + str(file_size_mb) + "mb.csv", "w")
for it in range(0, file_size_mb):
    fw.write('\n'.join(lines))
fw.close()
