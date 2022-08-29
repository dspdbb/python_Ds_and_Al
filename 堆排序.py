import random


# 调整函数
def sift(li, low, high):
    '''

    :param li:  列表
    :param low:  堆的根节点位置
    :param high:  堆的最后一个元素的位置
    :return:
    '''
    i = low  # 最早指向根节点
    j = 2 * i + 1  # 左子节点
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置没有越界，那么就一直循环
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右节点存在并且比左节点大
            j = j + 1  # j指向右节点
        if li[j] > tmp:  # 如果子节点比根节点大
            li[i] = li[j]  # 那么将子节点上移
            i = j  # i往下推
            j = i * 2 + 1  # 重新找到j
        else:  # tmp更大，就把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一子节点上
            break
    else:
        li[i] = tmp  # 因为到最后j越界了不满足循环条件，有空位，所以将tmp补足


# 堆排序
def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):  # 从最小子节点一路网上找父节点
        # i表示建立堆的时候调整的时候部分的根节点下标
        sift(li, i, n - 1)
    # 建立堆完成
    for i in range(n - 1, -1, -1):
        # i指向当前堆最后一个元素
        li[0], li[i] = li[i], li[0]  # 因为现在堆顶是最大，所以取出最大放到最后
        sift(li, 0, i - 1)  # i-1是新的的high


a = [i for i in range(10)]
random.shuffle(a)
print(a)
heap_sort(a)
print(a)
