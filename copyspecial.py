#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Mavrick Watts - assistance by Nikol and Amanda Yonce"

import re
import os
import sys
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files.
    returns a list of the absolute paths of the special files in 
    the given directory, but not deeper (no recursive search)
    """
    special_dir_files = []
    for file in os.listdir(dirname):
        special_file = re.findall(r'__(\w+)__', file)
        if special_file:
            special_dir_files.append(os.path.abspath(file))
    return special_dir_files

def copy_to(path_list, dest_dir):
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list: 
        shutil.copy(path, dest_dir)
    return    
    """given a list of file paths, copies those files 
    into the given directory"""



def zip_to(path_list, dest_zip):
    """given a list of file paths, 
    zip those files up into the given zip path"""
    for path in path_list:
        print(f'zip -j {dest_zip} {path}')
        subprocess.run(['zip', '-j', dest_zip, path])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='find dir for special files')
    ns = parser.parse_args(args)


    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    if len(sys.argv) < 1:
        parser.print_usage()
    path_list = get_special_paths(ns.from_dir)
    if ns.todir: 
        copy_to(path_list, ns.todir)
        # print(ns.todir)
    elif ns.tozip:
        zip_to(path_list, ns.tozip)
    else:
        print(*path_list, sep='\n')

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
