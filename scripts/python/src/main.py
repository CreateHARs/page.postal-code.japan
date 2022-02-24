#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import _01_check_
import _02_prepare_
import _03_download_
import _04_create_
import _05_update_


def main():
    timestamp('[start]')
    print(os.getcwd())
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())

    timestamp('--- [check_latest_update_date_dir] ---')
    latest_update_date_dir, exists = _01_check_.check_latest_update_date_dir()
    print(latest_update_date_dir, exists)
    if exists:
        return

    timestamp('--- [prepare_update_latest] ---')
    _02_prepare_.prepare_update_latest(latest_update_date_dir)

    timestamp('--- [download_zip_and_unzip] ---')
    _03_download_.download_zip_and_unzip(latest_update_date_dir)

    timestamp('--- [create_fixed_files] ---')
    _04_create_.create_fixed_files(latest_update_date_dir)

    timestamp('--- [update_current] ---')
    _05_update_.update_current(latest_update_date_dir)

    timestamp('[finish]')


def timestamp(message):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '\t' + message)


if __name__ == "__main__":
    main()
