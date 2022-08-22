import random


def bubble_sort(li):
    for i in range(len(a) - 1): #排序的第几次
        # 标志位，初始赋值错误
        exchange = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                # 每一次发生交换就将标志位置为正确
                exchange = True
        print(li)
        # 如果 标志为没有发生改变 那么就返回空，结束循环
        if not exchange:
            return


# eg:
# 创建一个无序列表
# random.randint(0, 10000) 意思是从零到一万随机取值
# for i in range(10) 意思是 取出十个数字放进列表
# a = [random.randint(0, 10000) for i in range(10)]
# print(a)
# bubble_sort(a)
# print(a)

# eg2:
a = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print(a)
bubble_sort(a)
