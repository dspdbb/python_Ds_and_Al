from cal_time import *
import random


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):  # i表示找到的数字下标
        tmp = li[i]
        j = i - 1  # j指有序区的数字下标
        # 每一次循环都判断前一位和相比较于后一位大小是否顺序，如果顺序没问题，不改变插入的排序，如果不相同那么插入位插入
        # 判断插入在有序区的位左还是位右
        # tmp保存每次取出来的值，来对while进行判断
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        # print(li)


if __name__ == '__main__':

    a = [random.randint(0, 10000) for i in range(10)]
    insert_sort(a)
    print(a)
