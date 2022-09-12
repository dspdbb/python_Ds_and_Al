# n的意义是桶， max_num是他们之间最大的值
from cal_time import *

@cal_time
def bucket_sort(li, n=10, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建n个空桶
    for var in li:
        # max_num//n代表一个 桶内放置多少数字
        # var // (max_num // n) var整除后面的值,就可以知道数字需要放置的桶的序号
        # min（）作用防止数字整除超出界限，n-1就一直是99号桶，保证数字不会越界，在整除出大的数字的时候在两个值之前取小，就必定放到最后一个桶里面
        i = min(var // (max_num // n), n - 1)  # i表示var放到几号桶
        buckets[i].append(var)
        # 保持桶内顺序，利用冒泡排序，从列表最后每次一倒退一步的方式进行比较，保持桶内的元素顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sort_li = []
    for buc in buckets:
        # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        # 也就是在原列表中直接将新列表在后面添加进来
        """---------以下两种中方式都可以使用-------------"""
        # sort_li += buc
        sort_li.extend(buc)
    #     因为有返回值在进行排序的时候需要有个变量进行接收
    return sort_li


import random

# a = [random.randint(0, 1000) for i in range(10000)]
# print(a)
# b = bucket_sort(a)
# print('----------------------------------------------------------------------------------------------------------------------------')
# print(b)

# bucket_sort(a)
# print(a)
