#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from const import \
    DIR_CURRENT


def update_current(latest_update_date_dir):
    if os.path.exists(DIR_CURRENT):
        os.remove(DIR_CURRENT)
    symlink_path = os.path.basename(os.path.normpath(latest_update_date_dir))
    os.symlink(symlink_path, DIR_CURRENT)
    os.symlink('docs/' + symlink_path, DIR_CURRENT + '_test')
    # if os.path.exists(DIR_CURRENT):
    #     shutil.rmtree(DIR_CURRENT)
    # shutil.copytree(latest_update_date_dir, DIR_CURRENT)
