#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from urllib.parse import urlparse
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json
import os
import views
import admin_views

url_register = {
    '/' : views.index,
    '/login/' : views.login,
    '/register/' : views.register,
    '/register/register_process/' : views.register_process,
#    '/main/' : views.main,
#    '/user_info/' : views.user_info,
#    '/user_license_info' : views.user_license_info,
#    '/buy/' : views.buy,
#    '/admin/' : views.admin_index,
#    '/admin/info/' : views.admin_info,
#    '/admin/user_info/' : views.admin_user_info,
#    '/admin/license_info/' : views.admin_license_info,
#    '/admin/add_license/' : views.admin_add_license,
}

url_admin_register = {
    '/admin/' : admin_views.index,
    '/admin/login/' : admin_views.login,

}


class GetHandler(BaseHTTPRequestHandler) :

    def do_GET(self):
        req_url = urlparse(self.path)
        req_path = req_url[2]
        #req_path = self.path

        if req_path in url_register:


            func = url_register[req_path]
            html_doc = func()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, encoding='utf8'))
            self.path = '/'

        elif req_path in url_admin_register:

            func = url_admin_register[req_path]
            html_doc = func()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, encoding='utf8'))
            self.path = '/'


        elif req_path == '/test/':
            self.send_response(200)
            self.end_headers()
            cwd = os.getcwd()+'\\test.html'
            html_file = open(cwd, 'r', encoding='utf-8')
            html_doc = html_file.read()
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
        elif req_path in url_register:

            content_len = int(self.headers['Content-Length'])
            req_body = self.rfile.read(content_len)
            print(req_body)

            func = url_register[req_path]
            html_doc = func(req_body)

            self.path='/'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, 'utf-8'))
        elif req_path in url_admin_register:

            content_len = int(self.headers['Content-Length'])
            req_body = self.rfile.read(content_len)
            print(req_body)

            func = url_admin_register[req_path]
            html_doc = func(req_body)

            self.path='/'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_doc, 'utf-8'))




if __name__ == '__main__':

    server = HTTPServer(('0.0.0.0', 80), GetHandler)
    print('Starting server. use <Ctrl-C> to stop.')
    server.serve_forever()
