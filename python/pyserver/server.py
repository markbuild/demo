from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import sys
import re

serverPort = 8022 # 默认端口

class handler(BaseHTTPRequestHandler):
    def do_GET(self): # GET 请求
        content = self.handle_http()
        self.wfile.write(content)

    def do_POST(self): # POST 请求
        content = self.handle_http()
        self.wfile.write(content)

    def handle_http(self):
        status = 200
        content_type = "text/plain"
        response_content = ""

        if self.path == '/': # 重定向到/web/index.html
            self.send_response(301)
            self.send_header('Location','/web/index.html')
            self.end_headers()
            return bytes(response_content, "UTF-8")
        elif re.findall(r'^\/web\/', self.path): # 前端页面
            filepath = Path('.' + self.path)
            if filepath.is_file():
                content_type = "text/html"
                response_content = open('.' + self.path)
                response_content = response_content.read()
            else:
                content_type = "text/plain"
                response_content = "404 Not Found"

        elif re.findall(r'^\/api\/', self.path): # API 接口
            filepath = Path('.' + self.path + '.py')
            if filepath.is_file():
                content_type = "text/html"
                controller = self.path.split('/')[2]
                module = __import__('api.' + controller)
                response_content = eval('module.' + controller + '.index()')
            else:
                content_type = "text/plain"
                response_content = "404 Not Found"

        else:
            content_type = "text/plain"
            response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF-8")

with HTTPServer(('', serverPort), handler) as server:
    print('[37;45m 启动HTTP 服务[0m 访问URL: localhost:' + str(serverPort))
    server.serve_forever()
