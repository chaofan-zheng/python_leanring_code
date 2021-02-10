import random

from django.db import models


# Create your models here.


def default_sign():
    signs = ['富二代', '高富帅', 'python顶级玩家', '办公室摸鱼大师', '琦玉老师']
    return random.choice(signs)


class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=20, primary_key=True)
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱')
    password = models.CharField('密码', max_length=32)
    sign = models.CharField('个人签名', max_length=50,
                            default=default_sign)
    info = models.CharField('个人简介', max_length=150,
                            default='')
    avatar = models.ImageField(upload_to='avatar',
                               null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    phone = models.CharField('手机号', max_length=11, default='')

