#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import login_check

#url_register = {
#    '/' : views.index,
#    '/login/' : views.login,
#    '/register/' : views.register,
#    '/main/' : views.main,
#    '/user_info/' : views.user_info,
#    '/user_license_info' : views.user_license_info,
#    '/buy/' : views.buy,
#    '/admin/' : views.admin_index,
#    '/admin/info/' : views.admin_info,
#    '/admin/user_info/' : views.admin_user_info,
#    '/admin/license_info/' : views.admin_license_info,
#    '/admin/add_license/' : views.admin_add_license,
#}



def page_view(rpath):
    local_path = os.getcwd() + rpath

    return local_path

def index():
    print('client access main page')
    cwd = os.getcwd()+'\\webpage\\login_form\\index.html'
    print(cwd)
    if os.path.exists(cwd):
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
    else :
        html_doc = 'file not exist'

    return html_doc


def login(req_body):
    print('web browser login-process request')
    print(req_body)
    tub = repr(req_body).split('&')
    id = tub[0].split('=')
    password = tub[1].split('=')
    print(id[1], password[1])
    login_state=login_check.login(id[1], password[1])

    if login_state == True:
        cwd = os.getcwd()+'\\webpage\\login_form\\success.html'
        print(cwd)
        if os.path.exists(cwd):
            html_file = open(cwd,'r',encoding='utf-8')
            html_doc = html_file.read()
        else:
            html_doc = 'file not exist'

        return html_doc

    else:
        cwd = os.getcwd()+'\\webpage\\login_form\\redirect.html'
        print(cwd)
        if os.path.exists(cwd):
            html_file = open(cwd,'r',encoding='utf-8')
            html_doc = html_file.read()
        else:
            html_doc = 'file not exist'

        return html_doc

def register(req_bod=''):
    print('web browser registraion-page request')
    cwd = os.getcwd() + '\\webpage\\sign up\\sign up.html'
    html_file = open(cwd,'r',encoding='utf-8')
    html_doc = html_file.read()

    return html_doc

def registration():
    print('web browser registraion-page request')
    cwd = os.getcwd() + '\\webpage\\sign up\\sign up.html'
    html_file = open(cwd,'r',encoding='utf-8')
    html_doc = html_file.read()

    return html_doc

def register_process(req_body):
    print('web browser registraion-process request')
    tub = repr(req_body).split('&')
    username = tub[0].split('=')
    id = tub[1].split('=')
    password = tub[2].split('=')
    password2 = tub[3].split('=')
    email = tub[4].split('=')
    phone = tub[5].split('=')
    print(username[1],id[1], password[1], password2[1], email[1], phone[1])
    state = login_check.registration(username[1], id[1], password[1], password2[1], email[1], phone[1])
    if state==1:
        print("id is matched")
        cwd = os.getcwd()+'\\webpage\\sign up\\redirect.html'
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
        return html_doc
    elif state==2:
        print("password is not matched")
        cwd = os.getcwd()+'\\webpage\\sign up\\redirect.html'
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
        return html_doc
    elif state==0:
        print("success registration")
        cwd = os.getcwd() + '\\webpage\\login_form\\redirect.html'
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
        return html_doc
    else:
        print("insert error")
    return
