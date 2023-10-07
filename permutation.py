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
    fp_keys = [4, 1, 3, 5, 7, 2, 8, 6]
    permutated = ''
    for i in fp_keys:
        permutated += x[i - 1]
    return permutated
