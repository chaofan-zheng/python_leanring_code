import json  # 原始数据编程json串
import base64
import time  # 生成token有有效期
import hmac  # 生成消息验证码的算法
import copy  # 对于不想影响到输入的实参，所以要对参数进行拷贝


class Jwt():
    def __init__(self):
        pass

    # 方法的目的在于生成一个token
    # playload: 载荷
    # key:共享密钥key
    # exp：token的有效期，以秒为单位
    @staticmethod
    def encode(payload, key, exp=300):
        # 1 初始化头
        # 1.1 用字典表示header
        header = {'alg': 'HS256', 'typ': 'JWT'}  # 固定化的格式，一个字母都不可以错
        # 1.2 将字典序列化为json串
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)  # 为了去掉空格，因为字典是无序的，sort_keys为了让字典编程有序
        print(header_json)  # {"alg": "HS256", "typ": "JWT"}
        # 1.3 将json串进行base64编码
        # 在这之前要把字符串转化为字符串
        header_bs = Jwt.b64encode(header_json.encode())
        print(header_bs)  # b'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9'

        # 2 载荷(公有声明和私有声明)
        # 2.1 对实参做一个深拷贝，不希望在函数内部修改到实参的值
        payload_data = copy.deepcopy(payload)  # 这一步的payload是私有声明
        # 2.2 设置公有声明
        payload_data['exp'] = time.time() + int(exp)
        # 2.3 对载荷对象字段序列化为json串
        payload_json = json.dumps(payload_data, separators=(',', ':'), sort_keys=True)
        # 2.4 讲json串做base64编码
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)  # b'eyJleHAiOjE2MTE1NjI1NTguOTQ3NTQxLCJ1c2VybmFtZSI6ImFpZDIwMTAifQ=='

        # 3签名(消息验证码的算法)
        # 3.1 生成一个算法对象
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        # 3.2 调用算法对象的digest对象，拿到消息验证码(签名)
        digest = hm.digest()
        # 3.3 将消息验证码进行bs64编码
        hm_bs = Jwt.b64encode(digest)
        print(hm_bs)  # b'SSZ8EQkw7mzSymFFtg6vNJEFgky1opCSK7bvbeVo--k='

        # 合成token
        print(
            header_bs + b'.' + payload_bs + b'.' + hm_bs)  # b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTE1NjI2MDguMjk5MzIsInVzZXJuYW1lIjoiYWlkMjAxMCJ9.90dwUI3e-IsvuptxsGQyfwKGj_HhQTw37VxHetAbKD8='
        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    # 完成base64的去等号操作
    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    # 进行补等号的操作
    # 需要补得数量是 4 -（长度/4的余数）
    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

        # 验证的话 做两个事情，一个是签名是否有效，一个是是否在有效期之内

    @staticmethod
    def decode(token, key):
        # 拆分token为三部分
        header_bs, payload_bs, sign = token.split(b'.')
        # 重新计算消息验证码
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        digest = hm.digest()
        sign2 = Jwt.b64encode(digest)

        # 如果两个消息验证码不相同，说明验证失败
        if sign != sign2:
            raise
            # 如果两个相同，将载荷解码，得到json串，再反序列化，得到私有和公有声明，判断是否在有效期。
        # 问：等号已经去掉了？怎么办
        # 一定要把等号补回来
        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)
        exp = payload['exp']
        now = time.time()
        # now>exp 说明过期了
        if now > exp:
            raise
        return payload


# b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTE1NjMzNjYuNDkzNDExLCJ1c2VybmFtZSI6ImFpZDIwMTAifQ.uvrhHvffrLJl_HZe4gEswM7sKP3wWKB7JEqeFp8kOzE'
# 最终结果就没有等号了


if __name__ == '__main__':
    token = Jwt.encode({'username': 'aid2010'}, '123456', 2)  # 三个参数： 私有声明、共享密钥、有效期
    # time.sleep(3) # 会产生异常
    payload = Jwt.decode(token, '123456')
    print(payload)  # {'exp': 1611564513.321383, 'username': 'aid2010'}
