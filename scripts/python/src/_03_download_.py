#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import zipfile
from const import URL_CSV_ZIP


def download_zip_and_unzip(latest_update_date_dir):
    zip_file_name = latest_update_date_dir + '/' + URL_CSV_ZIP.split('/')[-1]

    with requests.get(URL_CSV_ZIP) as download_file:
        data = download_file.content
        with open(zip_file_name, mode='wb') as save_file:
            save_file.write(data)
        with zipfile.ZipFile(zip_file_name) as obj_zip:
            obj_zip.extractall(latest_update_date_dir)
