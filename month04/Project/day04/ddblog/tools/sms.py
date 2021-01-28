import datetime
import hashlib
import json
import base64

import requests  # 使用该库发送请求


class YunTongXin():
    # 不变的函数写在外面
    base_url = 'https://app.cloopen.com:8883'

    # 通过构造函数传入基本配置参数
    def __init__(self, accountSid, accountToken, appId, templateId):
        self.templateId = templateId
        self.appId = appId
        self.accountToken = accountToken
        self.accountSid = accountSid

    # 1。构造url
    # 用别的函数去计算SigParameter，做到一个函数只做一件事情
    def get_request_url(self, SigParameter):
        self.url = self.base_url + f'/2013-12-26/Accounts/{self.accountSid}/SMS/TemplateSMS?sig={SigParameter}'

        return self.url

    # 调用
    # get_request_url(get_sig(get_time_stamp()))

    # 生成时间戳
    def get_time_stamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime("%Y%m%d%H%M%S")
        return now_str

    # 计算sig
    def get_sig(self, timestamp):
        data = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(data.encode())  # update 参数要求都是字节串
        hash_value = md5.hexdigest()
        return hash_value.upper()

    # 2. 构造请求头
    def get_request_header(self, timestamp):
        data = self.accountSid + ":" + timestamp
        data_bs = base64.b64encode(data.encode())
        data_bs = data_bs.decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': data_bs,
        }

    # 3. 构造请求体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        # 字典传参，必须是一样的
        return data

    # 4。 发送请求
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header, data=json.dumps(body))
        return res.text

    # 5。 封装以上所有步骤
    def run(self, phone, code):
        # 1. 构建url
        timestamp = self.get_time_stamp()
        url = self.get_request_url(self.get_sig(timestamp))
        # 2. 构建header
        header = self.get_request_header(timestamp)
        # 3. 构建body
        body = self.get_request_body(phone, code)
        # 4. 发送请求
        res = self.do_request(url, header, body)
        return res


if __name__ == '__main__':
    account_id = '8aaf0708773733a8017741b5dc9904ae'
    auth_token = 'e7ca8f6377ef406ea0afec3f73e28d36'
    AppId = '8aaf0708773733a8017741b5dd6804b4'
    template_id = '1'

    # 1. 创建云通信对象
    x = YunTongXin(account_id, auth_token, AppId, template_id)
    res = x.run('19847391887', '123456')
    print(res)
    # {"statusCode":"000000","templateSMS":{"smsMessageSid":"31a508ec301d44e6a3e8dc1e7a82d683","dateCreated":"20210127143926"}}
