import random


# 归并
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp = []  # 空数组存储排序后的数组
    while i <= mid and j <= high:  # 只要两边都有数
        # 判断初始i与j那个大，
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    # 将切片后的数组还原
    li[low:high + 1] = tmp


# 分解
def merge_sort(li, low, high):
    if low < high:  # 至少有两个元素递归
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        # 这才是最后的排序
        merge(li, low, mid, high)


def merge_sort_test(li, low, high):
    if low < high:  # 至少有两个元素递归
        mid = (low + high) // 2
        merge_sort_test(li, low, mid)
        merge_sort_test(li, mid + 1, high)
        # 这才是最后的排序
        print(li[low:high + 1])
        merge(li, low, mid, high)


a = list(range(6))
random.shuffle(a)
print(a)
merge_sort_test(a, 0, len(a) - 1)
print(a)
