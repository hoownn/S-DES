from fk1swfk2 import *
from permutation import *

def encrypt_0(bin_data_1, key_1):
    """
    encrypt_0用于检测输入的是8位二进制数还是字符串，
    如果是字符串则进行拆分后分别加密后返回结果并整合，
    如果是8位二进制数字则直接进行加密后返回加密结果
    """
    bin_data_0 = bin_data_1
    try:
        # 检验输入的是否为字符串，若为字符串则分解字符串后传入加密再将结果组合
        if not all(c in '01' for c in bin_data_1):
            # 将字符串转换为ASCII码的二进制表示形式
            results = []
            for i in bin_data_1:
                # 将字符转换为字节，然后再将字节转换为二进制字符串
                bin_char = format(ord(i), '08b')
                t = encrypt(bin_char, key_1)
                encrypted_char = chr(int(t, 2))
                results.append(encrypted_char)
            print(results)
            return "输入明文为：" + bin_data_0 + "\n输入密钥为：" + key_1 + "\n加密结果为：" + ''.join(results)
        else:
            if len(bin_data_1) != 8:
                return "输入的数据长度错误,必须是8位二进制数"
            result = encrypt(bin_data_1, key_1)
            return "输入明文为：" + bin_data_0 + "\n输入密钥为：" + key_1 + "\n加密结果为：" + str(result)
    except ValueError:
        return "输入数据的格式或长度有误"

def encrypt(bin_data ,key0):
    # 输入8位二进制数据
    # bin_data = input("请输入8位明文: ")
    # key0 = input("请输入10位二进制原始密钥: ")
    print("输入明文为：", bin_data)
    print("输入密钥为：", key0)

    if len(bin_data) != 8:
        # print("输入的数据长度错误,必须是8位二进制数")
        return "输入的数据长度错误,必须是8位二进制数"

    print("输入数据为：", bin_data)

    # 初始置换盒
    initial_permutation_result = ip_box(bin_data)
    print("初始置换盒结果: ", initial_permutation_result)

    # 两把密钥
    k1, k2 = get_keys(key0)
    print("k1:", k1, "|k2:", k2)

    # fk1
    r_fk1 = fk(initial_permutation_result, k1)
    print('fk1的结果: ', r_fk1)

    # fk2
    r_fk2 = fk(initial_permutation_result[4:8] + r_fk1, k2)  ##密码生成
    print('fk2的结果: ', r_fk2)

    # 最终置换盒
    final_permutation_result = fp_box(r_fk2 + r_fk1)
    print("最终置换盒结果: ", final_permutation_result)

    return str(final_permutation_result)

def decrypt_0(bin_data_1, key_1):
    """
    decrypt_0用于检测输入的是8位二进制数还是字符串，
    如果是字符串则进行拆分后分别解密后返回结果并组合，
    如果是8位二进制数字则直接进行解密后返回加密结合
    """
    bin_data_0 = bin_data_1
    try:
        # 检验输入的是否为字符串，若为字符串则分解字符串后传入加密再将结果组合
        if not all(c in '01' for c in bin_data_1):
            # 将字符串转换为ASCII码的二进制表示形式
            results = []
            for i in bin_data_1:
                # 将字符转换为字节，然后再将字节转换为二进制字符串
                bin_char = format(ord(i), '08b')
                t = decrypt(bin_char, key_1)
                decrypted_char = chr(int(t, 2))
                results.append(decrypted_char)
            print(results)
            return "输入明文为：" + bin_data_0 + "\n输入密钥为：" + key_1 + "\n加密结果为：" + ''.join(results)
        else:
            if len(bin_data_1) != 8:
                return "输入的数据长度错误,必须是8位二进制数"
            result = decrypt(bin_data_1, key_1)
            return "输入明文为：" + bin_data_0 + "\n输入密钥为：" + key_1 + "\n加密结果为：" + str(result)
    except ValueError:
        return "输入数据的格式或长度有误"
def decrypt(bin_data, key0):
    # 输入8位二进制数据
    # bin_data = input("请输入8位密文: ")
    # key0 = input("请输入10位二进制原始密钥: ")
    print("输入密文为：", bin_data)
    print("输入密钥为：", key0)

    # 初始置换盒
    initial_permutation_result = ip_box(bin_data)
    print("初始置换盒结果: ", initial_permutation_result)
    # 两把密钥
    k1,k2 = get_keys(key0)
    print("k1:", k1, "|k2:", k2)
    # fk2
    r_fk2 = fk(initial_permutation_result, k2)    # 密码生成
    print('fk2的结果: ', r_fk2)
    # fk1
    r_fk1 = fk(initial_permutation_result[4:8]+r_fk2, k1)
    print('fk1的结果: ', r_fk1)
    # 最终置换盒
    final_permutation_result = fp_box(r_fk1+r_fk2)
    print("最终置换盒结果: ", final_permutation_result)

    return str(final_permutation_result)

# if __name__ == "__main__":
#     bin_data = input("请输入明文: ")
#     key0 = input("请输入10位二进制原始密钥: ")
#     encrypt_0(bin_data, key0)
    # decrypt()
    # 00001001