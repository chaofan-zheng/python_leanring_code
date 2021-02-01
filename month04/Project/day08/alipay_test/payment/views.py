import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class JumpView(View):
    def get(self, request):
        return render(request, 'ajax_alipay.html')

    def post(self, request):
        # 从前端获取订单编号
        json_str = request.body
        json_obj = json.loads(json_str)
        order_id = json_obj['order_id']
        # 生成并返回一个return_url（pay_url）
        # 参数1：订单编号，参数2：订单金额
        pay_url = self.get_trade_url(order_id, 999)
        return JsonResponse({'pay_url': pay_url})

    def get_trade_url(self, order_id, money):
        # 步骤: 编写一个父类，在够在函数中，初始化一个alipay对象
        # 调用alipay的方法完成功能
        pass
    