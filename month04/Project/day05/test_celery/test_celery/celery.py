from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量，告知celery，为哪一个django项目提供服务的
# 从manage.py中复制
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')

# 创建应用
app = Celery("test_celery")
# 配置应用
app.conf.update(
    BROKER_URL='redis://@127.0.0.1:6379/1'
)

# 设置app自动加载任务  （自动查找和加载任务，因为任务函数不再只写在这个celery.py下，可能会分布在各个app下。）
app.autodiscover_tasks(settings.INSTALLED_APPS)  # 在所有已经注册过了的app下自动查找
# 然后在user应用下增加任务函数
