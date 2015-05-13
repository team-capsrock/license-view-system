import os
import admin_control


def page_view(rpath):
    local_path = os.getcwd() + rpath

    return local_path

def index():
    print('client access admin page')
    cwd = os.getcwd()+'\\webpage\\admin\\login_form\\index.html'
    print(cwd)
    if os.path.exists(cwd):
        html_file = open(cwd, 'r', encoding='utf-8')
        html_doc = html_file.read()
    else :
        html_doc = 'file not exist'

    return html_doc


def login(req_body):
    print('web browser admin page login-process request')
    print(req_body)
    tub = repr(req_body).split('&')
    id = tub[0].split('=')
    password = tub[1].split('=')
    print(id[1], password[1])
    login_state=admin_control.login(id[1], password[1])

    if login_state == True:
        cwd = os.getcwd()+'\\webpage\\admin\\login_form\\success.html'
        print(cwd)
        if os.path.exists(cwd):
            html_file = open(cwd,'r',encoding='utf-8')
            html_doc = html_file.read()
        else:
            html_doc = 'file not exist'

        return html_doc

    else:
        cwd = os.getcwd()+'\\webpage\\admin\\login_form\\redirect.html'
        print(cwd)
        if os.path.exists(cwd):
            html_file = open(cwd,'r',encoding='utf-8')
            html_doc = html_file.read()
        else:
            html_doc = 'file not exist'

        return html_doc