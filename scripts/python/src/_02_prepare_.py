#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from const import FILE_ENDPOINT_POSTAL_AREA, FILE_ENDPOINT_POSTAL_BLOCK_LARGE, FILE_ENDPOINT_POSTAL_CODE


def prepare_update_latest(latest_update_date_dir):
    try:
        os.makedirs(latest_update_date_dir)
        os.makedirs(latest_update_date_dir + FILE_ENDPOINT_POSTAL_AREA)
        os.makedirs(latest_update_date_dir + FILE_ENDPOINT_POSTAL_BLOCK_LARGE)
        os.makedirs(latest_update_date_dir + FILE_ENDPOINT_POSTAL_CODE)
    except Exception as e:
        print(e)
        # pass
        raise Exception
