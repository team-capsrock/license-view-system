#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json
import os
import login_check
import views

url_register = {
    '/': views.main_page,
}

class GetHandler(BaseHTTPRequestHandler) :

    def do_GET(self):
        req_path = self.path

        if req_path in url_register:
            print('client access main page')

            func = url_register[req_path]
            html_doc = func()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, encoding='utf8'))
        else:
            local_path = views.page_view(req_path)
            print(local_path)

            if os.path.exists(local_path):
                fp = open(local_path, 'r', encoding='utf8')

                html_doc = fp.read()

                self.send_response(200)
                self.send_header('Context-Length', str(len(html_doc)))
                self.end_headers()
                self.wfile.write(bytes(html_doc, encoding='utf8'))
            else:
                self.send_response_only(404)
                self.end_headers()
        return

    def do_POST(self):
        req_path = self.path

        if req_path == '/user-auth/':
            print('client access authentication')

            req_body = self.rfile.read()
            print('stream read clear')
            json_read = json.loads(repr(req_body))
            print(json_read)

            # TODO write code for json string
            info = json.dumps({'TYPE': 0, 'END-DATE': 20151231})
            json_val = json.dumps({'SIGNAL': 'LICENSE', 'LICENSE-INFO': info})

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json_val)
        elif req_path == '/login-process/':
            print('web browser login-process request')
            content_len = int(self.headers['Content-Length'])
            req_body = self.rfile.read(content_len)

            print(req_body)

            tub = repr(req_body).split('&')
            id = tub[0].split('=')
            password = tub[1].split('=')
            print(id[1], password[1])
            login_state=login_check.login(id[1], password[1])
            if(login_state==True):
                cwd = os.getcwd()+'\\webpage\\login form\\success.html'
                html_file = open(cwd, 'r', encoding='utf-8')
                html_doc = html_file.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(html_doc, 'utf-8'))
            else:
                cwd = os.getcwd()+'\\webpage\\login form\\fail.html'
                html_file = open(cwd, 'r', encoding='utf-8')
                html_doc = html_file.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(html_doc, 'utf-8'))
        elif req_path == '/registration/':
            print('web browser registraion-page request')
            cwd = os.getcwd()+'\\webpage\\sign up\\sign up.html'
            html_file = open(cwd, 'r', encoding='utf-8')
            html_doc = html_file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, 'utf-8'))
        elif req_path == '/registration/registration-process/':
            print('web browser registraion-process request')
            content_len = int(self.headers['Content-Length'])
            req_body = self.rfile.read(content_len)
            print(req_body)
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
            elif state==2:
                print("password is not matched")
            elif state==0:
                print("success registration")
                cwd = os.getcwd()+'\\webpage\\login form\\index.html'
                html_file = open(cwd, 'r', encoding='utf-8')
                html_doc = html_file.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(html_doc, 'utf-8'))
            else:
                print("insert error")
        return

if __name__ == '__main__':

    server = HTTPServer(('0.0.0.0', 80), GetHandler)
    print('Starting server. use <Ctrl-C> to stop.')
    server.serve_forever()
