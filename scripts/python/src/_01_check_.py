#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import datetime
from const import DIR_VERSION, URL_SCRAPING


def check_latest_update_date_dir():
    with requests.get(URL_SCRAPING) as response:
        response.encoding = response.apparent_encoding
    html = response.text.encode(response.encoding)

    update_date_str_ja = html \
        .split('<h1>')[1].split('</div')[0] \
        .split('<small>')[1].split('</small')[0] \
        .replace('更新', '') \
        .strip()
    print(update_date_str_ja)

    update_datetime = datetime.datetime.strptime(update_date_str_ja, '%Y年%m月%d日')
    update_date = datetime.date(update_datetime.year, update_datetime.month, update_datetime.day)
    update_date_dirname = DIR_VERSION.replace('%yyyy-MM-dd%', update_date.strftime('%Y-%m-%d'))
    print(update_date_dirname)

    if os.path.exists(update_date_dirname):
        return update_date_dirname, True
    else:
        return update_date_dirname, False

