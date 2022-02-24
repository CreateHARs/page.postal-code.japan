#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DIR_SRC_ROOT = os.path.dirname(os.path.abspath(__file__)) # os.curdir
DIR_PUBLIC = os.path.join(DIR_SRC_ROOT, '../../../public')

DIR_CURRENT = DIR_PUBLIC + '/current'
DIR_VERSION = DIR_PUBLIC + '/%yyyy-MM-dd%'

FILE_ENDPOINT_POSTAL_AREA = '/postal-areas'
FILE_ENDPOINT_POSTAL_BLOCK_LARGE = '/postal-blocks'
FILE_ENDPOINT_POSTAL_CODE = '/postal-codes'
# original file
FILE_ENDPOINT_ORIGINAL_CSV = '/KEN_ALL.CSV'
FILE_ENDPOINT_ORIGINAL_CSV_COLUMNS = ( # (仮)
    'code',
    'postal_old',
    'postal_new',  # 2
    'pref_kana',
    'address1_kana',
    'address2_kana',
    'pref',
    'address1',
    'address2',
    'is_multi_code',
    'is_koaza',
    'is_choume',
    'is_multi_place',
    'is_updated',
    'update_reason',
)
# fixed file
FILE_ENDPOINT_ALL_CSV = '/all.csv'
FILE_ENDPOINT_PER_AREA_CSV = FILE_ENDPOINT_POSTAL_AREA + '/%POSTAL_CODE_first2digit%.csv'
FILE_ENDPOINT_PER_BLOCK_LARGE_CSV = FILE_ENDPOINT_POSTAL_BLOCK_LARGE + '/%POSTAL_CODE_first5digit%.csv'
FILE_ENDPOINT_PER_POSTAL_CODE_CSV = FILE_ENDPOINT_POSTAL_CODE + '/%POSTAL_CODE%.csv'


URL_SCRAPING = 'https://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html'
URL_CSV_ZIP = 'https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'

print(__file__)