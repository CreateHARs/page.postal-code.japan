#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DIR_SRC_ROOT = os.path.dirname(os.path.abspath(__file__)) # os.curdir
DIR_PUBLIC = os.path.join(DIR_SRC_ROOT, '../../../docs')

DIR_CURRENT = DIR_PUBLIC + '/current'
DIR_VERSION = DIR_PUBLIC + '/%yyyy-MM-dd%'

FILE_ENDPOINT_POSTAL_AREA = '/postal-areas'
FILE_ENDPOINT_POSTAL_BLOCK_LARGE = '/postal-blocks'
FILE_ENDPOINT_POSTAL_CODE = '/postal-codes'
# original file
FILE_ENDPOINT_ORIGINAL_CSV = '/KEN_ALL.CSV'
# fixed file
FILE_ENDPOINT_ALL_CSV = '/all.csv'
FILE_ENDPOINT_PER_AREA_CSV = FILE_ENDPOINT_POSTAL_AREA + '/%POSTAL_CODE_first2digit%.csv'
FILE_ENDPOINT_PER_BLOCK_LARGE_CSV = FILE_ENDPOINT_POSTAL_BLOCK_LARGE + '/%POSTAL_CODE_first5digit%.csv'
FILE_ENDPOINT_PER_POSTAL_CODE_CSV = FILE_ENDPOINT_POSTAL_CODE + '/%POSTAL_CODE%.csv'


CSV_COLUMNS_ORIGINAL = ( # (仮)
    'local_government_code',
    'postal_code_5digit',
    'postal_code_7digit',  # 2
    'prefecture_kana',
    'address1_kana',
    'address2_kana',
    'prefecture_kanji',
    'address1_kanji',
    'address2_kanji',
    'is_address2_has_multiple_postal_code',
    'is_address2_has_multiple_sublocality',
    'is_address2_includes_chome',
    'is_postal_code_has_multiple_address2',
    'updated_type',
    'updated_reason_type',
)
CSV_COLUMNS_ORDERED = CSV_COLUMNS_ORIGINAL # (
#     'postal_code_7digit',
#     'postal_code_5digit',
#     'local_government_code',
#     'prefecture_kanji',
#     'prefecture_kana',
#     'address1_kanji',
#     'address1_kana',
#     'address2_kanji',
#     'address2_kana',
#     'is_address2_has_multiple_postal_code',
#     'is_address2_has_multiple_sublocality',
#     'is_address2_includes_chome',
#     'is_postal_code_has_multiple_address2',
#     'updated_type',
#     'updated_reason_type',
# )

URL_SCRAPING = 'https://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html'
URL_CSV_ZIP = 'https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'

print(__file__)