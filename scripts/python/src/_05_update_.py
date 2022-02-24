#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from const import \
    DIR_CURRENT


def update_current(latest_update_date_dir):
    if os.path.exists(DIR_CURRENT):
        os.remove(DIR_CURRENT)
    os.symlink(latest_update_date_dir, DIR_CURRENT)
    # if os.path.exists(DIR_CURRENT):
    #     shutil.rmtree(DIR_CURRENT)
    # shutil.copytree(latest_update_date_dir, DIR_CURRENT)
