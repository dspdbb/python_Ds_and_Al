from cal_time import *
import random
import sys

sys.setrecursionlimit(10000)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右面找到比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写入左边的空位
        while left < right and li[left] <= tmp:  # 找到比tmp大的值
            left += 1
        li[right] = li[left]  # 把左边的值写道右边的空位上
    li[left] = tmp  # 把tmp归位
    return left  # 返回中间值


# 因为递归的原因，如果在此处添加计算时间函数，那么会多次输出运行时间
# 所以将递归封装一下，利用另外一个函数调用排序
def __quick_sort(li, left, right):
    # 当left小于right
    if left < right:
        # 中间值为通过快排的前置排序得出
        mid = partition(li, left, right)
        # 调用自己,排序出左边的顺序
        __quick_sort(li, left, mid - 1)
        __quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li):
    __quick_sort(li, 0, len(li) - 1)



# 创建一个无序的列表，返回0到10000中的任意整数
# a = [random.randint(0, 10000) for i in range(1000)]
a = list(range(10000, 0, -1))  # 最坏出现的情况  会导致递归爆满，然后无法运行
# b = list(range(10000))
# 而shuffle是将做好的列表打乱顺序
# random.shuffle(a)
# random.shuffle(b)
quick_sort(a)
# bubble_sort(b)
# 运行完毕之后可以看出，快速排序是冒泡排序速度的很多倍
