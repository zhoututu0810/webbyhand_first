# Python3.6增加了一个新的可以产生用于密钥管理的安全随机数的模块：secrets。
# 因为random都是伪随机
import secrets
import string

# secrets模块完成两种操作：
# 1）生成安全随机数
# 2）生成一个预期长度的随机字符串--可用作令牌和安全URL

# 功能与random.choice(seq)相同，从指定的非空序列中随机选择一个元素并返回
secrets.choice(string.digits)

print()
# 返回一个带有k个随机位的整数, 返回的结果是一个整数。随机位数越多越安全，但是性能越低
ret = secrets.randbits(3)
print(ret)

print()
# secrets.token_bytes([nbytes=None])
ret = secrets.token_bytes(nbytes=2)
print(ret)  # b'\x8e\xb2'
# 请求drf的知识判断下，这个是哪种编码

print()
# 返回一个包含nbytes字节的16进制格式的随机文本字符串，每个字节被转成成2个16进制数字，
# 所以长度是 字节参数的 2倍
# 这可以用来生成一个随机密码。
salt = secrets.token_hex(30) # 字符508c
print(salt)

print()
# 返回一个包含nbytes个字节的随机安全URL文本字符串，这可以在提供重置密码的应用中用来生成一个临时的随机令牌
# 问题：什么是安全url
url_safe = secrets.token_urlsafe(30)
print(url_safe)


# 下面精髓的实战
# 实例1： 生成一个由8位数字和字母组成的随机密码
import secrets
import string

alphanum = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphanum) for i in range(8))

# 实例2： 生成一个由10位数字和字母组成的随机密码，要求至少有一个小写字符，至少一个大写字符 和 至少3个数字
import secrets
import string

alphanum = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphanum) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and len(c.isdigit() for c in password) >= 3):
        break

# 实例3： 生成一个用于找回密码应用场景的、包含一个安全令牌的、很难猜到的临时URL
import secrets
url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()

