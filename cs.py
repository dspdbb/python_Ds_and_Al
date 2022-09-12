#
# from functools import wraps
# f import time
# f
#
# # time装饰器
# def timer(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         begin_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         start_time = time.perf_counter()
#         print('func:%r args:[%r, %r] took: %2.4f sec' % (func.__name__, args, kwargs, start_time - begin_time))
#         return result
#
#     return wrap
#
#
# @timer
# def waste_some_time(num):
#     my_list = []
#     for i in range(num):
#         my_list.append(i)
#     return my_list
#
#
# if __name__ == '__main__':
#     arr = waste_some_time(1000)
#     print(arr)
# import random
#
#
# def sort(li, b, c):
#     if b<c:
#         mid = (b + c) // 2
#         sort(a, b, mid)
#         sort(li, mid + 1, c)
#
#
# import random
#
# a = list(range(10))
# random.shuffle(a)
#
#
# # sort(a,0,len(a)-1)
# # 这是一个递归小案例，这个函数在函数内部自己调用了自listsum(numlist[1:])
# def listsum(numlist):
#     if len(numlist) == 1:  # 当数组的长度为1时，代表是数组是一个数了
#         return numlist[0]
#     else:
#         return numlist[0] + listsum(numlist[1:])  # 第一个数加上后面的数，这里自己调用了自己，是数组不断递归的条件
#
#
# listsum(a)


# 3 + 2 + 1
# def sum_numbers(num):
#     # 1.如果是1，直接返回1 -- 出口
#     if num == 1:
#         return 1
#     # 2.如果不是1，重复执行累加并返回结果
#     return num + sum_numbers(num-1)
#
#
# sum_result = sum_numbers(3)
# # 输出结果为6
# print(sum_result)


def j(a):
    if a > 1:
        return a * j(a - 1)
    return a


print(j(3))

# 运行过程
# 传入a
# 第一轮 3* j（2）
# 第二论 3* 2*j(1)
# 第三轮 不满足条件，直接返回1 然后回溯每次的值，递归就相当于将每次的值暂存，然后在不满足递归条件的时候，
# 结束递归 将每一次递归的值进行计算，或者是传值等
a=[2,3,35,38,39,3444,31111111111,322222]
a.sort()
print(a)