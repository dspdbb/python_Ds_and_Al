# 1.判断两个字符串内的元素组成是否相等

def a(b, c):
    return sorted(list(b)) == sorted(list(c))


def pd(ad, sb):
    # 可以转换为列表进行遍历,也可以直接进行遍历
    a = list(ad)
    b = list(sb)
    di = {}
    di2 = {}
    # 利用get函数，获取输入的内各里面各个元素出现的次数并保存
    # 将输入的元素进行遍历
    for ch in a:
        di[ch] = di.get(ch, 0) + 1
    for ch in b:
        di2[ch] = di2.get(ch, 0) + 1
    return di == di2


x = 'sss'
y = 'sssd'
# p = pd(x, y)
# print(p)


# 2.判断数字是否在二维数组中
def cz(a, ta):
    for i in a:
        if ta in i:
            return True
    return False


b = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
c=cz(b,0)
print(c)