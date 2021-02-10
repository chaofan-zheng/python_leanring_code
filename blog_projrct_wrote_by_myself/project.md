# 一、注册

先调研API手册查看数据库结构。规定Model类名为UserProfile

| 字段名       | 类型         | 作用     | 备注1                        | 备注2 |
| ------------ | ------------ | -------- | ---------------------------- | ----- |
| username     | varchar(11)  | 用户名   | 注册时填写的用户名，不可修改 | 主键  |
| nickname     | varchar(30)  | 昵称     | 在博客中显示的名字，可修改   | 无    |
| email        | varchar(50)  | 邮箱     | 预留                         | 无    |
| password     | varchar(32)  | 密码     | 用户密码，已散列存储         | 无    |
| sign         | varchar(50)  | 个人签名 | 无                           | 无    |
| info         | varchar(150) | 个人描述 | 无                           | 无    |
| avatar       | varchar(100) | 头像     | 无                           | 无    |
| created_time | datetime     | 创建时间 | 无                           | 无    |
| updated_time | datetime     | 更新时间 | 无                           | 无    |

然后通过分析前段代码或者API手册得出：

```
URL：http://127.0.0.1:8000/v1/users 
请求：{‘username’: jack, ‘email’: ‘abc@qq.com’, ‘password1’: ‘abcdef’, ‘password2’: ‘abcdef’}
相应：{‘code’: 200 , ‘username’: ‘abc’, ’data’: {‘token’: ‘asdadasd.cvreijvd.dasdadad’} }
```

注册功能需要使用到数据库，使用mysql，这就要startapp，所以采用分布式路由。

```python
create database my_blog default charset utf8;
python3 manage.py startapp user
# 注册user
path('v1/users/', include('user.urls')),
class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=20, primary_key=True)
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱')
    password = models.CharField('密码',max_length=32)
    sign = models.CharField('个人签名', max_length=50,
                            default=default_sign)
    info = models.CharField('个人简介', max_length=150,
                            default='')
    avatar = models.ImageField(upload_to='avatar',
                               null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    phone = models.CharField('手机号', max_length=11, default='')
# 因为我们想用随机签名，这里就要实现随机签名的方法
def default_sign():
    signs = ['富二代', 'python顶级玩家', '办公室摸鱼大师', '琦玉老师']
    return random.choice(signs)

# 生成随机签名有两点需要注意
	1. default = default_sign 不能调用这个函数。不然的话就不是随机的了，所有人的签名都相同。
    2. 函数要写在这个类名之外。
    
然后进行迁移。
python3 manage.py makemigrations
python3 manage.py migrate
```

## 顺便复习下models模型类

```python
class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=20,
                                primary_key=True)
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

字段类型：
	CharField   => varchar 必须要制定max_length参数，因为varchar不能省略
    需要注意的是 varchar指定的是字符个数，而不是字节大小
    DateField => date               YYYY-MM-DD 
    	里面有三个参数：
        auto_now 保存对象时，自动设置字段为当前时间
        auto_now_add 当对象第一次被创建时，自动设置字段为当前时间
        default 设置当前时间 default('2019-6-1')
    DateTimeField => datetime     	YYYY-MM-DD HH:MM:SS 
    ImageField => varchar(100)      保存了文件的路径，使用的是字符串 
    	upload_to被用来指定传到media/avatar 路径下
```

思考：如果想自定义时间怎么办？例如精确到秒数。在后端通过time.time通过时间戳按格式输出来实现，这样就会比较麻烦了。

接下来在注册界面实现的功能就比较多了。

大致思路是在前端获取Ajax请求后验证数据是否合格然后入库。所以要做一个发送短信验证码的工作。通过和后端存在redis的和前端Ajax发过来的，进行一致性的比较。所以要在免费获取验证码这个button下面对后端发送一个专门的url，后端专门进行处理项目中定为/v1/users/sms（这里要注意要放到` path('<str:username>',views.UserView.as_view()),`之上。防止进入到这个url）。因为send_sms是一个比较依赖外部服务器的功能，所以可能会比较耗时，所以说需要使用celery，使用任务队列，来提升感觉。

# 获取短信验证码



