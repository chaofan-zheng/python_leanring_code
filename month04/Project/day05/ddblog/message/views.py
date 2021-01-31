from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from message.models import Message
from tools.login_dec import login_check
from topic.models import Topic


@login_check
def message_view(request, topic_id):
    # 1 限定前端发送的POST请求
    if request.method != 'POST':
        result = {'code':10400,'error':'请发送post请求'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    # 2 从客户端获取评论内容。parent_id[0]
    content = json_obj['content']
    parent_id = json_obj.get('parent_id',0)# 因为前端没有验证这个parent_id 有时候发有时候不发，所以要温柔的拿
    # 3 验证topic_id对应的文章是否存在，获取topic对象
    try:
        topic = Topic.objects.get(id=topic_id)
    except:
        result = {'code': 10311, 'error': 'topic不存在'}
        return JsonResponse(result)
    # 4 从请求对象中获取用户对象
    author = request.myuser
    # 5 数据入库
    Message.objects.create(
        content=content,
        parent_message=parent_id,
        topic_id=topic.id,
        user_profile=author,
    )
    # 6 返回
    return JsonResponse({'code': 200})
