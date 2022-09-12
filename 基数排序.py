from cal_time import *
from 桶排序 import *
import copy


@cal_time
def radix_sort(li):
    # 基数排序就是对个位十位等进行一次排序   9 排序一次  99 两次 依次类推
    max_num = max(li)
    # 迭代次数
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 创建n个空桶
        # 对应每个元素分到那个桶里面
        for var in li:
            # 通过整除和取余知道当前数字为多少
            # 例如(987//10^0)%10 最后的值为7,就可以将值放入七号桶
            # 当it迭代进行自加,那么下次就整除十位,以致于继续迭代到百位,依次类推,将数字通过大小排序放到每个桶里面
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 写回li
        it += 1


# import random
#
# li = list(range(10000))
# random.shuffle(li)
# # print(li)
# # radix_sort(li)
# # print(li)
# li1 = copy.deepcopy(li)
# li2 = copy.deepcopy(li)
# bucket_sort(li1)
# radix_sort(li2)
print((987//100)%10)