import os
from django.conf import settings
import sys


def import_module(module_name):
    """
    Import module and return it.
    """
    __import__(module_name)
    return sys.modules[module_name]


def listdir(dir_name, get_dirs=None, get_files=None, hide_ignored=False):
    """
    Return list of all dirs and files inside given dir.

    Also can filter contents to return only dirs or files.

    Args:
    - dir_name: Which directory we need to scan (relative)
    - get_dirs: Return dirs list
    - get_files: Return files list
    - hide_ignored: Exclude files and dirs with initial underscore
    """
    if get_dirs is None and get_files is None:
        get_dirs = True
        get_files = True

    source_dir = os.path.join(settings.BASE_DIR, 'app', dir_name)

    dirs = []

    for dir_or_file_name in os.listdir(source_dir):
        path = os.path.join(source_dir, dir_or_file_name)
        if hide_ignored and dir_or_file_name.startswith('_'):
            continue
        is_dir = os.path.isdir(path)
        if get_dirs and is_dir or get_files and not is_dir:
            dirs.append(dir_or_file_name)

    return dirs
