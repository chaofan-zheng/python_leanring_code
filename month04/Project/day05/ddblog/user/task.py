from django.conf import settings

from ddblog.celery import app
from tools.sms import YunTongXin


@app.task
def send_sms(phone, code):
    # 向指定的手机号发送短信验证
    # account_id = '8aaf0708773733a8017741b5dc9904ae'
    # auth_token = 'e7ca8f6377ef406ea0afec3f73e28d36'
    # AppId = '8aaf0708773733a8017741b5dd6804b4'
    # template_id = '1'
    # 这些都写到配置文件里面去
    account_id = settings.ACCOUNT_ID
    auth_token = settings.AUTH_TOKEN
    AppId = settings.APPID
    template_id = settings.TEMPLATE_ID
    # 不能用内置的setting？ why
    # 必须全大写！！！！！
    # setting里设置的变量必须全大写

    x = YunTongXin(account_id, auth_token, AppId, template_id)
    res = x.run(phone, code)
    return res
