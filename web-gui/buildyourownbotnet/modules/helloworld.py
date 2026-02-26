#!/usr/bin/python
# -*- coding: utf-8 -*-
'Create Hello World Folder (Build Your Own Botnet)'

# standard library
import os
import sys

# utilities
import util

# REQUIRED GLOBALS
command = True
packages = ['util']
platforms = ['win32','linux2','darwin']
usage = 'helloworld [path]'
description = """
Create a helloworld folder on the target system
"""

# main
def run(path=None):
    """
    Create a folder named 'helloworld' on the target system.
    
    Args:
        path (str): Directory where helloworld folder will be created.
                   If None, creates in the current working directory.
    
    Returns:
        str: Status message indicating success or failure
    """
    try:
        if path is None:
            path = os.getcwd()
        
        folder_path = os.path.join(path, 'helloworld')
        
        # Check if folder already exists
        if os.path.exists(folder_path):
            msg = "[!] Folder already exists: {}".format(folder_path)
            print(msg)
            return msg
        
        # Create the folder
        os.makedirs(folder_path)
        
        # Create a hello.txt file inside
        hello_file = os.path.join(folder_path, 'hello.txt')
        with open(hello_file, 'w') as f:
            f.write('Hello World!\n')
        
        msg = "[+] Successfully created folder: {}".format(folder_path)
        print(msg)
        return msg
    
    except Exception as e:
        msg = "[-] Error creating folder: {}".format(str(e))
        print(msg)
        return msg

