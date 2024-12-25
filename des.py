# 导入DES加密模块
from Crypto.Cipher import DES
# 导入迭代工具模块，用于生成密钥的所有可能组合
import itertools
# 导入时间模块，用于计算程序运行时间
import time

# 待破解的密文（这里示例随意写了一段十六进制表示的密文，实际要替换为真实的）
ciphertext = bytes.fromhex('1234567890abcdef')

# 尝试的日期范围（这里简单用ASCII可打印字符一部分举例，实际可以根据可能的密钥构成调整）
characters = [chr(i) for i in range(32, 127)]

# 定义DES加密模式，这里用常见的ECB模式
mode = DES.MODE_ECB

# 记录开始时间
start_time = time.time()

# 遍历所有可能的8字节密钥组合
for key_tuple in itertools.product(characters, repeat=8):
    # 将密钥元组转换为字符串并编码为UTF-8格式
    key = (''.join(key_tuple)).encode('utf-8')
    # 如果密钥不足8字节，补充\0
    if len(key) < 8:
        key += b'\0' * (8 - len(key))  
    # 创建DES加密对象
    cipher = DES.new(key, mode)
    # 解密密文
    plaintext = cipher.decrypt(ciphertext)
    # 简单判断解密结果是否看起来像是合理的文本（实际情况更复杂判断逻辑可能不同）
    if all(32 <= char <= 126 for char in plaintext):
        # 打印可能的密钥和解密后的明文
        print(f"可能的密钥: {key.decode('utf-8')}")
        print(f"解密后的明文: {plaintext.decode('utf-8', errors='ignore')}")
        # 找到一个可能的密钥后，跳出循环
        break

# 记录结束时间
end_time = time.time()
# 打印程序运行时间
print(f"花费时间: {end_time - start_time} 秒")
