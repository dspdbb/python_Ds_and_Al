def count_sort(li, max_count=100):
    # 此处的'_'类似常见的i的作用，用于循环迭代中的计数，range(variable)范围的最后和开始值之间的差值（即range范围内包含的值的数量）是多少，这个for循环就循环多少次；
    # [0 for _ in range(max_count + 1)]的意思是创建 以0为元素的列表，换种说法就是将0拷贝了for循环次放入列表
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        # 在列表count下标为val的地方计数加一
        # 存储li中val出现的次数
        count[val] = count[val] + 1
        print(count[val],val)
        # print(val)
    li.clear()
    # 这个函数的基本应用就是用来遍历一个集合对象，它在遍历的同时还可以得到当前元素的索引位置。
    # 在获取到元素出现的次数和值之后进行循环
    print('-------------------------')
    for ind, val in enumerate(count):
        # 将val个下标ind存到li中并且计算个数存入
        for i in range(val):
            print(ind,val )
            li.append(ind)

            print(li)


import random

li = [random.randint(0, 100) for _ in range(100)]
print(li)
count_sort(li)
print(li)
