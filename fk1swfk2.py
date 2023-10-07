def leftshift1(p10):
    a = [p10[0], p10[5]]
    p1 = []
    p2 = []
    for i in range(4):
        p1.append(p10[i+1])
    p1.append(a[0])
    for i in range(4):
        p2.append(p10[i+6])
    p2.append(a[1])
    return p1 + p2

def leftshift2(p10):
    a = [p10[0], p10[1], p10[5], p10[6]]
    p1 = []
    p2 = []
    for i in range(3):
        p1.append(p10[i+2])
    p1.append(a[0])
    p1.append(a[1])
    for i in range(3):
        p2.append(p10[i+7])
    p2.append(a[2])
    p2.append(a[3])
    return p1 + p2
def get_keys(k0):
    # 第一个交换盒
    # k0 = [1,2,3,4,5,6,7,8,9,0]  # 十位的原始密钥
    p10 = []
    # p10置换
    for j in [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]:
        p10.append(k0[j - 1])
    # Key2
    p10_1 = leftshift1(p10)
    k1 = []
    # p8置换
    for i in [6, 3, 7, 4, 8, 5, 10, 9]:
        k1.append(p10_1[i - 1])

    # key1
    p10_2 = leftshift2(p10_1)
    k2 = []
    # p8置换
    for i in [6, 3, 7, 4, 8, 5, 10, 9]:
        k2.append(p10_2[i - 1])
    return k1, k2
    
def fk(text,key):
    '''
    key -> k1
    '''
    #1.先把text分开
    text = list(text)
    for i in range(len(text)):   # 把text的每个元素改为int
        text[i] = int(text[i])

    key = list(key)
    for i in range(len(key)):   # 把key的每个元素改为int
        key[i] = int(key[i])

    textL = text[0:4]
    textR = text[4:8]

    # 2.包含一个轮函数
    rF = F(textR, key)

    # 3.异或    轮函数的结果和textleft异或
    
    a = ''  # 这里出来就只有七位了     有空把之前那个方法也跑通
    for i in range(len(textL)):
        a += str(textL[i]^rF[i])
    return a

def F (textR, k):
    '''
    轮函数
    四位进,思维出
    '''
    textR = list(textR)
    k = list(k)
    # 1.扩展置换
    rr = extend_subt(textR)

    # 2.用轮密钥
    print(type(rr),type(k))  
    for i in range(len(rr)):   # 把rr的每个元素改为int
        rr[i] = int(rr[i])
    for i in range(len(rr)):   # 把k的每个元素改为int
        k[i] = int(k[i])        
    a = []  ### 这里出来就只有七位了     有空把之前那个方法也跑通
    for i in range(len(rr)):    # 异或
        a.append(rr[i] ^ k[i])

    # 3.S-box   八位变四位
    a = S_boxs(a)

    b = []
    # p4置换
    for i in [2, 4, 3, 1]:
        b.append(int(a[i-1]))
    return b

def extend_subt(textR):
    '''
    E/P扩位及置换，将原text的右边四位扩展为八位
    '''
    rr = []
    for i in [4, 1, 2, 3, 2, 3, 4, 1]:
        rr.append(textR[i-1])
    return rr
    
def str_to_binint(a:str)->int:
    '''
    将str类型的二进制表示转换为可以异或的整数
    '''
    i = len(a)-1
    n = 0
    s = 0
    while i >= 0:
        s += int(a[i])*(2**n)
        i -= 1
        n += 1
    return s


def S_boxs(a)->str:
    '''
    替换盒
    将八位的a分为两两一组，共4组
    把两个拼起来，得到一个数字
    '''

    sbox1 = [[1,0,3,2],
             [3,2,1,0],
             [0,2,1,3],
             [3,1,0,2]]

    sbox2 = [[0,1,2,3],
             [2,3,1,0],
             [3,0,1,2],
             [2,1,0,3]]

    # 将八位的a分为两两一组，共4组
    # 要把两个拼起来，得到一个数字
    n = get_num(a)
    return bin(sbox1[n[0]][n[1]])[2:].zfill(2)+bin(sbox2[n[2]][n[3]])[2:].zfill(2)

def get_num(a):
    '''
    把八位异或结果a的03,12,47,56拼起来
    '''

    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    r = a[0]*2 + a[3], a[1]*2 + a[2], a[4]*2 + a[7], a[5]*2 + a[6]
    return r
