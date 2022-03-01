# ######################################
# 实例4： 使用RSA算法生成密钥对儿
# ######################################
# 生成秘钥对：
from Crypto import Random
from Crypto.PublicKey import RSA

# 获取一个伪随机数生成器
random_generator = Random.new().read
# 获取一个rsa算法对应的密钥对生成器实例
rsa = RSA.generate(1024, random_generator)

# 生成私钥并保存
private_pem = rsa.exportKey()
print(type(private_pem))        # <class 'bytes'>
# 注意open的模式是wb，因为exoprtKey返回的是字节串
# 如果模式是wt，即文本模式，那么write的对象必须是字符串，此时就是需要将字节串解码成字符串，但是你根部不知道编码类型啊！
with open('rsa.key', 'wb') as f:
    f.write(private_pem)

# 生成公钥并保存
public_pem = rsa.publickey().exportKey()
with open('rsa.pub', 'wb') as f:
    f.write(public_pem)

# 私钥文件rsa.key的内容为：
private_key = '''
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCo7vV5xSzEdQeFq9n5MIWgIuLTBHuutZlFv+Ed8fIk3yC4So/d
y1f64iuYFcDeNU7eVGqTSkHmAl4AihDXoaH6hxohrcX0bCg0j+VoQMe2zID7MzcE
d50FhJbuG6JsWtYzLUYs7/cQ3urZYwB4PEVa0WxQj2aXUMsxp6vl1CgB4QIDAQAB
AoGAS/I5y4e4S43tVsvej6efu1FTtdhDHlUn1fKgawz1dlwVYqSqruSW5gQ94v6M
mZlPnqZGz3bHz3bq+cUYM0jH/5Tygz4a+dosziRCUbjMsFePbJ4nvGC/1hwQweCm
+7sxog4sw91FrOfAg/iCcoeho0DghDolH9+zzwRYPIWUyUECQQDFGe+qccGwL9cU
v+GmZxtF8GkRL7YrXI7cvnZhnZZ7TANjxlYukLGEpiFGIDd0Aky1QhkK18L8DTO4
+iGXTpgJAkEA22o03/1IqeRBofbkkDmndArHNUnmv5pyVFaLKPoVgA4A1YsvqxUL
DK6RwFGONUMknBWY59EDKCUdIf3CsVIhGQJAJKDMRB19xBMv4iBCe9z/WYDy1YnL
TcWWmvkeIMfbVjBrFNif3WlwQ9lnp5OHGpzuymRtKPGtv49ohECfi3HEmQJAPI+n
AoAdk07+Up8b3TccoinrbCj2uMH/dongpTHJx2uWDVr6kEUhpKF2d1fLYaYjr7VC
XBHTxjvgO6aYG2to2QJBAIzDugOSTeQFpidCoewfa0XX4guF+WRf8wzyBC/XE6TY
3cIY05sjbpfiVwW/Cb8Z2ia8EgBTGN8HSIFOUQ2jRl4=
-----END RSA PRIVATE KEY-----
'''

# 公钥文件rsa.pub的内容为：
public_key = '''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCo7vV5xSzEdQeFq9n5MIWgIuLT
BHuutZlFv+Ed8fIk3yC4So/dy1f64iuYFcDeNU7eVGqTSkHmAl4AihDXoaH6hxoh
rcX0bCg0j+VoQMe2zID7MzcEd50FhJbuG6JsWtYzLUYs7/cQ3urZYwB4PEVa0WxQ
j2aXUMsxp6vl1CgB4QIDAQAB
-----END PUBLIC KEY-----
'''


# ######################################
# 实例5： 公钥加密算法的实现
# 加密是用对方提供的公钥加密
# ######################################
# 前面说过，公钥加密算法是由Crypto.Cipher子包下的PKCS1_v1_5.py或PKCS1_OAEP.py模块以已经存在的密钥对儿为密钥来实现的，
# 现在常用的是PKCS1_v1_5。另外，我们前面提到过，使用对方的公钥加密，使用对方的私钥解密才能保证数据的机密性，
# 因此这里以上面生成的公钥进行加密数据，以上面生成的私钥解密数据：
from Crypto import Random
from Crypto.PublicKey import RSA
# Cipher_PKCS1_v1_5, PKCS1_OAEP 这两个是不同的加密方式
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5, PKCS1_OAEP
import base64

# 数据加密, 待加密文本长度必须小于rsa秘钥的长度
message = "This is a plain text."
with open('public.pem', 'rb') as f:
    # read读出来的结果是字符串还是字节串，依赖于open的模式
    # 如果模式是rt，那边必须提供解码类型encodng ,open本质是读入字节串，提供了解码类型，可以解码成字符串哦！
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    # 注意encrypt的加密的参数是字节串，所以需要编码
    cipher_text = base64.b64encode(cipher_obj.encrypt(message.encode('utf-8')))
    print('cipher test: ', cipher_text)

# 数据解密， 用私钥解密
with open('rsa.key', 'r') as f:
    private_key = f.read()
    # 加载的是私钥
    rsa_key_obj = RSA.importKey(private_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    random_generator = Random.new().read
    # 为什么解密要用random_generator参数？？？
    plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator)
    print('plain text: ', plain_text)

# 输出结果：
# ('cipher test: ', 'oq1sOSz4lS9PgrKmiwuAHs7iUhmWMvWdEbXLTOdhGtyIAr6xwmjtnBNpuvMVIM2Mz/O/xVzPu5L8nzUVW2THKpQinNwC7JWF0wnxrTHwKrmfXIIxxibQJS02obxkoEeqrjRo0b8V7yktYIV3ig2SlU3yjcr+lOFmRX+h6dE2TAI=')
# ('plain text: ', 'This is a plain text.')


# ######################################
# 实例6： 数据签名与签名验证的实现
# 私钥签名，公钥验签
# ######################################
# 同样，签名与验证相关算法的功能是由Crypto.Signature子包下的PKCS1_v1_5.py和PKCS1_PASS.py以这个密钥对而为密钥来实现的。
# 数据签名的目的是为了防止别人篡改发送人的原始数据，其原理是：
# 1）先以单向加密方式通过某种哈希算法（如MD5，SHA1等）对要发送的数据生成摘要信息（数据指纹）；
# 2）然后发送方用自己密钥对儿中的私钥对这个摘要信息进行加密；
# 3）数据接收方用发送的公钥对加密后的摘要信息进行解密，得到数据摘要的明文A；
# 4）数据接收方再通过相同的哈希算法计算得到数据摘要信息B；
# 5）数据接收方对比数据摘要A与数据摘要B，如果两者一致说明数据没有被篡改过。
from Crypto.Hash import SHA
# PKCS1_v1_5 和 PKCS1_PSS 不同的签名方式
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS
message = "This is the message to send."
# 数据签名
with open('rsa.key', 'r') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    signer = Signature_PKCS1_v1_5.new(rsa_key_obj)
    digest = SHA.new()  # digest 摘要
    digest.update(message)  # 先把待签名的文件 签名
    signature = base64.b64encode(signer.sign(digest))   # 把前面后的结果，在用base64编码
    print('signature text: ', signature)

# 验证签名
with open('rsa.pub', 'r') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    signer = Signature_PKCS1_v1_5.new(rsa_key_obj)
    digest = SHA.new(message)   # 把比较文本，转化为比较摘要
    # 反向过程，先base反编码
    is_ok = signer.verify(digest, base64.b64decode(signature))
    print('is ok: ', is_ok)

# 输出结果：
# ('signature text: ', 'Bb4gvPU9Ji63kk3SSTiAVLctDbdb91DQuQKecbTcO2Jvpwbr7fr9sKZO+vZ8LIuSOdJkhbGX6swsSNwDI/CoT0xCdjiasfySPgsLyTcSWLyy9P7SrDuveH1ABUR/oYisvT1wFsScu0NMOBR8sLpboPk2DiW6n400jZq7t09xUyc=')
# ('is ok: ', True)

# 上面这几个关于pycrpto的使用实例来自这里