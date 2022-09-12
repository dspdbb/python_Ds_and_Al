def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i表示找到的数字下标
        tmp = li[i]
        j = i - gap  # j指有序区的数字下标
        # 每一次循环都判断前一位和相比较于后一位大小是否顺序，如果顺序没问题，不改变插入的排序，如果不相同那么插入位插入
        # 判断插入在有序区的位左还是位右
        # tmp保存每次取出来的值，来对while进行判断
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


import random

a = list(range(20))
random.shuffle(a)
print(a)
shell_sort(a)
print(a)
