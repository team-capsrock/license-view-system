#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os

def page_view(rpath):
    local_path = os.getcwd() + rpath

    return local_path

def main_page():
    print('client access main page')
    cwd = os.getcwd()+'\\webpage\\login_form\\index.html'
    print(cwd)
    if os.path.exists(cwd):
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
    else :
        html_doc = 'file not exist'

    return html_doc


__author__ = 'notebook'

