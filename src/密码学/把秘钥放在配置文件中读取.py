from Crypto import Random
from Crypto.PublicKey import RSA
# Cipher_PKCS1_v1_5, PKCS1_OAEP 这两个是不同的加密方式
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5, PKCS1_OAEP
import base64

# 私钥文件rsa.key的内容为：
# 切记：b'''后面不能加空格，否则会报错， 并且在结尾的也不能换行
# 三引号要切记，不能随便换行，特别是三引号地方的的换行，很容易为了美观而自己不经意加了一个换行
# python变量(内存中)字节串默认是unicode的，unicode可以当做是无编码类型
# open写入到文件中的也是unicode, 因为最终会都取会回来到内存中，内存中的字节串就是unicode
# private_key = b'''-----BEGIN RSA PRIVATE KEY-----
# MIICXAIBAAKBgQCo7vV5xSzEdQeFq9n5MIWgIuLTBHuutZlFv+Ed8fIk3yC4So/d
# y1f64iuYFcDeNU7eVGqTSkHmAl4AihDXoaH6hxohrcX0bCg0j+VoQMe2zID7MzcE
# d50FhJbuG6JsWtYzLUYs7/cQ3urZYwB4PEVa0WxQj2aXUMsxp6vl1CgB4QIDAQAB
# AoGAS/I5y4e4S43tVsvej6efu1FTtdhDHlUn1fKgawz1dlwVYqSqruSW5gQ94v6M
# mZlPnqZGz3bHz3bq+cUYM0jH/5Tygz4a+dosziRCUbjMsFePbJ4nvGC/1hwQweCm
# +7sxog4sw91FrOfAg/iCcoeho0DghDolH9+zzwRYPIWUyUECQQDFGe+qccGwL9cU
# v+GmZxtF8GkRL7YrXI7cvnZhnZZ7TANjxlYukLGEpiFGIDd0Aky1QhkK18L8DTO4
# +iGXTpgJAkEA22o03/1IqeRBofbkkDmndArHNUnmv5pyVFaLKPoVgA4A1YsvqxUL
# DK6RwFGONUMknBWY59EDKCUdIf3CsVIhGQJAJKDMRB19xBMv4iBCe9z/WYDy1YnL
# TcWWmvkeIMfbVjBrFNif3WlwQ9lnp5OHGpzuymRtKPGtv49ohECfi3HEmQJAPI+n
# AoAdk07+Up8b3TccoinrbCj2uMH/dongpTHJx2uWDVr6kEUhpKF2d1fLYaYjr7VC
# XBHTxjvgO6aYG2to2QJBAIzDugOSTeQFpidCoewfa0XX4guF+WRf8wzyBC/XE6TY
# 3cIY05sjbpfiVwW/Cb8Z2ia8EgBTGN8HSIFOUQ2jRl4=
# -----END RSA PRIVATE KEY-----'''
#
# # 公钥文件rsa.pub的内容为：
# # 切记：b'''后面不能加空格，否则会报错
# public_key = b'''-----BEGIN PUBLIC KEY-----
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWncGo+rA9Co9YOWp9mjSz3pTY
# iPSU512bzXv/YJpjTqvTLMWG8//5Chqxl0A1w7tW6EOcUKycTn+bZikSw4zCJ5Dq
# QzjybjwZgLX88RkxKrCElp7y1Z66ffP540UNQg9O/SlUZw717qSufDDy1IXc/qZr
# RQ8Lo2clqT5XJsAbnQIDAQAB
# -----END PUBLIC KEY-----'''


# 数据加密, 待加密文本长度必须小于rsa秘钥的长度
message = "This is a plain text."
with open('public.pem', 'rb') as f:
    # read读出来的结果是字符串还是字节串，依赖于open的模式
    # 如果模式是rt，那边必须提供解码类型encodng ,open本质是读入字节串，提供了解码类型，可以解码成字符串哦！
    public_key = f.read()
rsa_key_obj = RSA.importKey(public_key)
cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
# 因为
cipher_text = base64.b64encode(cipher_obj.encrypt(message.encode('utf-8')))
print('cipher test: ', cipher_text)

# 加密后不一样，，肯定不一样啊，如果一样，不就有对照密码本了嘛
# cipher test:  b'wT//RHeRCgUio+9TW5VKfEfWWr6prX13wU6WWJ36Cr0W/bRZ6RqEss3s0NwKu/gGDUDXl9ixsheI4SraLxmQ8zXJARDRuzBYSL1YJQxMZYOVO8yVWenvWLYL9itIraUS9uHAO6w/PfQazUxRfEyh3N5LGaBZ5Etd0NLjIGquE/Y='
# cipher test:  b'bnxU/ck/i4YH1+oDo6vqALyvrLRxMs0YzkwiqPLi+0DjXchECqIGBC9kiMLybZ/iYWiwQfrUJVQ5xwTvv6ZdDt2HviYg5+75nQRnFDxOkNDxppz+Lss274PUbCe8p4Xh/hZrmqWVkPopSdbV02pHdHx0VC9lbdX9aBdZBQDst8o='
