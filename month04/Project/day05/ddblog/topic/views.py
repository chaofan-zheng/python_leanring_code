import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from tools.login_dec import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


class TopicView(View):
    @method_decorator(login_check)
    def post(self, request, author_id):
        # 1 从请求对象中附加数据中获取用户对象
        author = request.myuser
        # 2 从前端获取用户输入的值（内容，不带格式的内容，权限，分类，标题）
        json_str = request.body
        json_obj = json.loads(json_str)
        # {'content': content, 'content_text': content_text, 'limit': limit, 'title': title, 'category': category}
        content = json_obj['content']
        content_text = json_obj['content_text']
        limit = json_obj['limit']
        title = json_obj['title']
        category = json_obj['category']
        introduce = content_text[:30]
        # 3 检查分类的值一定是tec或no-tec
        #   检查权限的值一定public或private
        if category not in ['tec', 'no-tec']:
            result = {'code': '10300', 'error': '类别错误'}
            return JsonResponse(result)
        if limit not in ['public', 'private']:
            result = {'code': '10301', 'error': '权限错误'}
            return JsonResponse(result)
        # 5 数据入库
        try:
            Topic.objects.create(title=title,
                                 category=category,
                                 limit=limit,
                                 introduce=introduce,
                                 content=content,
                                 user_profile_id=author.username,
                                 # user_profile=author,
                                 # 这个两个方法都可以
                                 )
        except Exception as e:
            result = {'code': '10301', 'error': e}
            return JsonResponse(result)
        # 6 返回
        return JsonResponse({'code': 200})

    def get(self, request, author_id):
        # 首先要获取文章的作者的这个对象
        # 防止输入错误的情况
        try:
            author = UserProfile.objects.get(username=author_id)
        except:
            result = {'code': 10305, 'error': '用户名称错误'}
            return JsonResponse(result)
        # 获取访问者的身份(有可能是游客，有可能是某一登录用户，所以不能用login_check，可以重写一个获取访问者)
        visitor_name = get_user_by_request(request)

        # 增加文章详情页的操作
        t_id = request.GET.get('t_id')
        # 文章详情页
        if t_id:
            is_self = False
            # 博主自己访问自己
            if visitor_name == author_id:
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id, user_profile_id=author_id)
                except:
                    result = {'code': 10310, 'error': 'topic id is error'}
                    return JsonResponse(result)
            else:
                try:
                    author_topic = Topic.objects.get(id=t_id, user_profile_id=author_id, limit='public')
                except:
                    result = {'code': 10310, 'error': 'topic id is error'}
                    return JsonResponse(result)
            res = self.make_topic_res(author, author_topic, is_self)
            return JsonResponse(res)

        else:
            # 判断有没有带查询字符串
            # v1/topics/Aiden
            # v1/topics/Aiden?category=tec/no-tec  # 技术或非技术文章列表
            filter_category = False
            category = request.GET.get('category')
            if category in ['tec', 'no-tec']:
                filter_category = True
            # 根据分类和权限，编写四种不同的查询条件
            # 访问自己，无需增加权限过滤
            if visitor_name == author.username:
                # 是否需要分类
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id)

            # 别人访问，增加权限过滤
            else:
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public', category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public')

            # 权限
            # 分以下两种情况
            # 登录用户访问自己的文章，可以看到所有的
            # 其他人访问博主的文章，看到博主所有public的，不能访问private
            # 所以要区分开访问者是不是作者本人

            # 响应json
            # 根据传入的参数：作者，文章列表，构建一个前端要求的json格式返回值
            res = self.make_topics_res(author, author_topics)
            return JsonResponse(res)

    def make_topic_res(self, author, author_topic, is_self):
        # 响应格式
        # {
        #     "code": 200,
        #     "data": {
        #         "nickname": "guoxiaonao",
        #         "title": "我的第一次",
        #         "category": "tec",
        #         "created_time": "2019-06-03",
        #         "content": "<p>我的第一次，哈哈哈哈哈<br></p>",
        #         "introduce": "我的第一次，哈哈哈哈哈",
        #         "author": "guoxiaonao",
        #         "next_id": 2,
        #         "next_title": "我的第二次",
        #         "last_id": null,
        #         "last_title": null,
        #         "messages": [
        #             {
        #                 "id": 1,
        #                 "content": "<p>写得不错啊，大哥<br></p>",
        #                 "publisher": "guoxiaonao",
        #                 "publisher_avatar": "avatar/头像2.png",
        #                 "reply": [
        #                     {
        #                         "publisher": "guoxiaonao",
        #                         "publisher_avatar": "avatar/头像2.png",
        #                         "created_time": "2019-06-03 07:52:16",
        #                         "content": "谢谢您的赏识",
        #                         "msg_id": 2
        #                     }
        #                 ],
        #                 "created_time": "2019-06-03 07:52:02"
        #             }
        #         ],
        #         "messages_count": 2
        #     }
        # }
        if is_self:
            next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                              user_profile_id = author.username).order_by('id').first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                              user_profile_id = author.username).order_by('id').last()
            if next_topic:
                next_id = next_topic.id
                next_title = next_topic.title
            else:
                next_id = None
                next_title=None
            if last_topic:
                last_id = last_topic.id
                last_title = last_topic.title
            else:
                last_id = None
                last_title=None


            # try:
            #     next_id = author_topic.id + 1
            #     next_title = Topic.objects.get(id=next_id, user_profile_id=author.username).title
            # except:
            #     next_id = None
            #     next_title = None
            # try:
            #     last_id = author_topic.id - 1
            #     last_title = Topic.objects.get(id=last_id, user_profile_id=author.username).title
            # except:
            #     last_id = None
            #     last_title = None


        else:
            next_topic = Topic.objects.filter(id__gt=author_topic.id, user_profile_id=author.username,
                                              limit='public').order_by('id').first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, user_profile_id=author.username,
                                              limit='public').order_by('id').last()
            if next_topic:
                next_id = next_topic.id
                next_title = next_topic.title
            else:
                next_id = None
                next_title=None
            if last_topic:
                last_id = last_topic.id
                last_title = last_topic.title
            else:
                last_id = None
                last_title=None



            # try:
            #     next_id = author_topic.id + 1
            #     next_title = Topic.objects.get(id=next_id, user_profile_id=author.username, limit='public').title
            # except:
            #     next_id = None
            #     next_title = None
            # try:
            #     last_id = author_topic.id - 1
            #     last_title = Topic.objects.get(id=last_id, user_profile_id=author.username, limit='public').title
            # except:
            #     last_id = None
            #     last_title = None

        res = {'code': 200, 'data': {}}
        res['data']['nickname'] = author.nickname
        res['data']['title'] = author_topic.title
        res['data']['category'] = author_topic.category
        res['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        res['data']['content'] = author_topic.content
        res['data']['introduce'] = author_topic.introduce
        res['data']['author'] = author.nickname
        res['data']['next_id'] = next_id
        res['data']['next_title'] = next_title
        res['data']['last_id'] = last_id
        res['data']['last_title'] = last_title
        res['data']['messages'] = []
        res['data']['messages_count'] = 0

        return res

    def make_topics_res(self, author, author_topics):
        # {‘
        # code’: 200,
        # ’data’: {‘
        # nickname’: ’abc’,
        # ’topics’: [{‘
        # id’: 1,
        # ’title’: ’a’,
        # ‘category’: ‘tec’,
        # ‘created_time’: ‘2018 - 0
        # 9 - 03
        # 10: 30: 20’,
        # ‘introduce’: ‘aaa’,
        # ‘author’: ’abc’
        # }]
        # }
        # }
        topics = []
        for topic in author_topics:
            dict01 = {
                'id': topic.id,
                'title': topic.title,
                'category': topic.category,
                'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'introduce': topic.introduce,
                'author': author.nickname,
            }
            topics.append(dict01)
        res = {'code': 200, 'data': {}}
        res['data']['nickname'] = author.nickname
        res['data']['topics'] = topics
        return res
