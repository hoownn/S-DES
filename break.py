import sys
from fk1swfk2 import fk, get_keys
from permutation import fp_box, ip_box
import threading
import time

def encrypt(bin_data,key0):
    # 输入8位二进制数据

    if len(bin_data) != 8:
        print("输入的数据长度错误,必须是8位二进制数")
        return
        # 初始置换盒
    initial_permutation_result = ip_box(bin_data)
    # print("初始置换盒结果: ", initial_permutation_result)
    #两把密钥
    k1,k2 = get_keys(key0)
    # print("k1:",k1,"|k2:",k2)
    #fk1
    r_fk1 = fk(initial_permutation_result,k1)
    # print('fk1的结果: ',r_fk1)
    #fk2
    r_fk2 = fk(initial_permutation_result[4:8]+r_fk1,k2)##密码生成
    # print('fk2的结果: ',r_fk2)
    # 最终置换盒
    final_permutation_result = fp_box(r_fk2+r_fk1)
    # print("最终置换盒结果: ", final_permutation_result)
    return final_permutation_result
def t1():
    trykey = 0
    sc = 0
    while 1:
        k = bin(trykey)[2:].zfill(10)
        for i  in range(len(plain_text)) :
            if encrypt(plain_text[i],k) ==  cipher_text[i]:
                sc += 1
            else :
                break
        if sc == len(plain_text):
            print('密码已找到，结果为:',k)
            print('本次破解用时',time.time()-str_ti)
            sys.exit()
            break
        else :
            trykey += 1
        if trykey == 85:
            break
def t2():
    trykey = 85
    sc = 0
    while 1:
        k = bin(trykey)[2:].zfill(10)
        for i  in range(len(plain_text)) :
            if encrypt(plain_text[i],k) ==  cipher_text[i]:
                sc += 1
            else :
                break
        if sc == len(plain_text):
            print('密码已找到，结果为:',k)
            print('本次破解用时',time.time()-str_ti)
            sys.exit()
            break
        else :
            trykey += 1
        if trykey == 170:
            break
def t3():
    trykey = 170
    sc = 0
    while 1:
        k = bin(trykey)[2:].zfill(10)
        for i  in range(len(plain_text)) :
            if encrypt(plain_text[i],k) ==  cipher_text[i]:
                sc += 1
            else :
                break
        if sc == len(plain_text):
            print('密码已找到，结果为:',k)
            print('本次破解用时',time.time()-str_ti)
            sys.exit()
            break
        
        else :
            trykey += 1
        if trykey > 2**8:
            break
if __name__ == '__main__':
    plain_text = ['11001000','10010011','11110000']
    cipher_text = ['00111011','10000110','00011110']
    # plain_text =['10000000']
    # cipher_text =['00000010']
    # 创建新线程
    th1 = threading.Thread(target=t1,name='t1')
    th2 = threading.Thread(target=t2,name='t2')
    th3 = threading.Thread(target=t3,name='t3')
    print('开始')
    str_ti = time.time()
    th1.start()
    th2.start()
    th3.start()
    