#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
import csv, operator
from itertools import groupby
from const import \
    FILE_ENDPOINT_ORIGINAL_CSV, \
    FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS, \
    FILE_ENDPOINT_ALL_CSV, \
    FILE_ENDPOINT_PER_AREA_CSV, \
    FILE_ENDPOINT_PER_BLOCK_LARGE_CSV,\
    FILE_ENDPOINT_PER_POSTAL_CODE_CSV

def create_fixed_files(latest_update_date_dir):
    original_csv = latest_update_date_dir + FILE_ENDPOINT_ORIGINAL_CSV
    fixed_csv = latest_update_date_dir + FILE_ENDPOINT_ALL_CSV
    fixed_json = fixed_csv.replace('.csv', '.json')

    with open(original_csv, "rb") as src, src, open(fixed_csv, 'w') as dest:
        reader = csv.reader(src)
        writer = csv.writer(dest, quotechar='"', quoting=csv.QUOTE_ALL)

        data = sorted(reader, key=operator.itemgetter(2))
        writer.writerow(FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS)

        rows = []
        for line in data:
            rows.append([unicode(col, 'shift-jis').encode('utf-8') for col in line])
        writer.writerows(rows)
        create_json_from_csv(fixed_csv, fixed_json)

        for key, group in groupby(rows, key=lambda x: x[2][:2]):
            # print(key)
            fixed_per_area_csv = latest_update_date_dir + FILE_ENDPOINT_PER_AREA_CSV.replace('%POSTAL_CODE_first2digit%', key.strip())
            fixed_per_area_json = fixed_per_area_csv.replace('.csv', '.json')
            div_writer = csv.writer(open(fixed_per_area_csv, 'w'))
            div_writer.writerow(FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS)
            div_writer.writerows(group)
            create_json_from_csv(fixed_per_area_csv, fixed_per_area_json)

        for key, group in groupby(rows, key=lambda x: x[2][:5]):
            # print(key)
            fixed_per_block_large_csv = latest_update_date_dir + FILE_ENDPOINT_PER_BLOCK_LARGE_CSV.replace('%POSTAL_CODE_first5digit%', key.strip())
            fixed_per_block_large_json = fixed_per_block_large_csv.replace('.csv', '.json')
            div_writer=csv.writer(open(fixed_per_block_large_csv, 'w'))
            div_writer.writerow(FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS)
            div_writer.writerows(group)
            create_json_from_csv(fixed_per_block_large_csv, fixed_per_block_large_json)

        for key, group in groupby(rows, key=lambda x: x[2]):
            # print(key)
            fixed_per_postal_code_csv = latest_update_date_dir + FILE_ENDPOINT_PER_POSTAL_CODE_CSV.replace('%POSTAL_CODE%', key.strip())
            fixed_per_postal_code_json = fixed_per_postal_code_csv.replace('.csv', '.json')
            div_writer=csv.writer(open(fixed_per_postal_code_csv, 'w'))
            div_writer.writerow(FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS)
            div_writer.writerows(group)
            create_json_from_csv(fixed_per_postal_code_csv, fixed_per_postal_code_json)


def create_json_from_csv(from_csv, to_json):
    json_list = []
    with open(from_csv, 'r') as src:
        reader = csv.DictReader(src)
        data = [OrderedDict((field, row[field]) for field in reader.fieldnames) for row in reader]
        for row in data:
            json_list.append(row)
    with open(to_json, 'w') as dest:
        s = json.dumps(json_list, indent=4, sort_keys=False, separators=(",", ": "), ensure_ascii=False)
        dest.write(s)
