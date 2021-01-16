# file : middleware/mymiddleware.py
import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response


class MyMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法2 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法2 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法2 process_response 被调用")
        return response


class MyMiddleWare3(MiddlewareMixin):
    ip_history = {}

    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']
        url = request.path_info
        # print(url)  # /test
        if not re.match(r'^/test', url):
            return
        times = self.ip_history.get(ip, 0)
        if times >= 5:
            return HttpResponse('你已经被禁止访问')
        self.ip_history[ip] = times+1
        print(f'第{self.ip_history[ip]}次访问')
