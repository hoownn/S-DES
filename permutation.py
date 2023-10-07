import fk1swfk2
def ip_box(x):
    """
    IP初始置换盒对8位数据进行置换
    Args:
        x: 8位数据,以字符串形式表示,例如'01010101'
    Returns:
        置换后的8位数据,以字符串形式表示,例如'11001100'
    """
    ip_keys = [2, 6, 3, 1, 4, 8, 5, 7]
    permutated = ''
    for i in ip_keys:
        permutated += x[i - 1]
    return permutated

def fp_box(x):
    """
    FP最终置换盒对8位数据进行逆置换
    Args:
        x: 8位数据,以字符串形式表示,例如'11001100'
    Returns:
        逆置换后的8位数据,以字符串形式表示,例如'01010101'
    """
    print("fp-1:", x)
    fp_keys = [4, 1, 3, 5, 7, 2, 8, 6]
    permutated = ''
    for i in fp_keys:
        permutated += x[i - 1]
    return permutated

# def main():
#     # 输入8位二进制数据
#     bin_data = input("请输入8位二进制数据: ")
#     key0 = input("请输入8位二进制原始密钥: ")
#     if len(bin_data) != 8:
#         print("输入的数据长度错误,必须是8位二进制数")
#         return
#         # 初始置换盒
#     initial_permutation_result = ip_box(bin_data)
#     print("初始置换盒结果: ", initial_permutation_result)
#     #fk1
#     r_fk1 = fk1swfk2.fk('initial_permutation_result','key0')
#     print('fk1的结果: ',r_fk1)
#     #fk2
#     r_fk2 = fk1swfk2.fk(('initial_permutation_result','key0'))##密码生成
#     print(print('fk2的结果: ',r_fk2))
#     # 最终置换盒
#     final_permutation_result = fp_box(initial_permutation_result)
#     print("最终置换盒结果: ", final_permutation_result)
#
# if __name__ == "__main__":
#     main()
