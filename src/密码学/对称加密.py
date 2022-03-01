# pycrypto使用实例
# pip install pycrypto

# ######################################
# 实例1： 使用SHA256算法获取一段数据的摘要信息
# ######################################
from Crypto.Hash import SHA256


hash = SHA256.new()
hash.update('Hello, World!')
digest = hash.hexdigest()
print(digest)

# 输出结果：
# dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f


# ######################################
# 实例2： 使用AES算法加密，解密一段数据
# ######################################
from Crypto.Cipher import AES

# 加密与解密所使用的密钥，长度必须是16的倍数
secret_key = "ThisIs SecretKey"
# 要加密的明文数据，长度必须是16的倍数（扯淡吧）
plain_data = "Hello, World123!"
# IV参数，长度必须是16的倍数
iv_param = 'This is an IV456'

# 数据加密
aes1 = AES.new(secret_key, AES.MODE_CBC, iv_param)
cipher_data = aes1.encrypt(plain_data)
print('cipher data：', cipher_data)

# 数据解密
aes2 = AES.new(secret_key, AES.MODE_CBC, 'This is an IV456')
plain_data2 = aes2.decrypt(cipher_data)  # 解密后的明文数据
print('plain text：', plain_data2)

# 输出结果：
# ('cipher data\xef\xbc\x9a', '\xcb\x7fd\x03\x12T,\xbe\x91\xac\x1a\xd5\xaa\xe6P\x9a')
# ('plain text\xef\xbc\x9a', 'Hello, World123!')



# ######################################
# 实例3： 随机数操作
# ######################################
from Crypto.Random import random

print('random.randint: ', random.randint(10, 20))
print('random.randrange: ', random.randrange(10, 20, 2))
print('random.randint: ', random.getrandbits(3))
print('random.choice: ', random.choice([1, 2, 3, 4, 5]))
print('random.sample: ', random.sample([1, 2, 3, 4, 5], 3))
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print('random.shuffle: ', list)

# 输出结果：
# ('random.randint: ', 10L)
# ('random.randrange: ', 10L)
# ('random.randint: ', 5L)
# ('random.choice: ', 5)
# ('random.sample: ', [5, 4, 2])
# ('random.shuffle: ', [5, 2, 1, 3, 4])



