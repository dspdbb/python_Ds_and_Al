def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        # 利用内置函数找到最小数字
        min_value = min(li)
        # 利用append函数向新空数组顺序填入
        li_new.append(min_value)
        # 旧数组删除每次遍历出的最小值 ，***此方法不严谨会产生空位
        li.remove(min_value)
    return li_new

#
# a = [5, 6, 8, 7, 9, 4, 2, 1, 3]
# print(select_sort_simple(a))


def select_sort(li):
    for i in range(len(li) - 1):  # 第几趟
        # 创建一个变量存取无序区 i 中最小值的位置
        min_loc = i
        # 循环指针向前推进
        for j in range(i+1, len(li)):
            # 判断后一个跟前一个相比较大小，
            if li[j] < li[min_loc]:
                # 如果j小于无序区的i那么就像j作为最新的小位做交换
                min_loc = j
        # 当for循环完毕之后，找到最小的min_loc与第i趟的值做交换，达到排序的作用
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


a = [3,2,1,5,6,9,8,7,4]
select_sort(a)
print(a)
