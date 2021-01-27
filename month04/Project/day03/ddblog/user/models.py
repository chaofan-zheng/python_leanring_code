from django.db import models
import random

# 随机默认的个人签名
def default_sign():
    signs = ['IT精英', '健身达人', '富二代', '创业联盟']
    return random.choice(signs)  # 随机的选项


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=20, primary_key=True)  # 主键，不能有自动增长了
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱')
    password = models.CharField('密码', max_length=32)
    sign = models.CharField('个人签名', max_length=50, default=default_sign)  # 当用户没有设置用户签名的时候，给你一个随机的签名
    # 不能是函数的调用，得是一个函数名，如果是函数的调用的话，所有人的默认签名都是一样了，就不是随机的了
    info = models.CharField('个人简介',max_length=150,default='')
    avatar = models.ImageField(upload_to='avatar', null=True)  # 上传的时候会创建一个新目录，上传的头像会添加到新目录里面
    created_time = models.DateTimeField(auto_now_add=True)  # 第一次的创建时间会记录下来
    updated_time = models.DateTimeField(auto_now=True)  # 每次记录修改时间
    phone = models.CharField('手机号', max_length=11, default='')
