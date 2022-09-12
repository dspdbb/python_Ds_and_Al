MAZE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1)
]


def mig(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curnode = stack[-1] #当前节点
        # 终点既起点
        if curnode[0] == x2 and curnode[1] == y2:
            for p in stack:
                print(p)
            return True
        # 通过四个方向来进行下一步的走向
        for dir in dirs:
            # nextnode下一个节点
            nextnode = dir(curnode[0], curnode[1])
            # 如果下一步的地点值为0，那么就将当前x1，y1的值入栈
            if MAZE[nextnode[0]][nextnode[1]] == 0:
                stack.append(nextnode)
                # 记录当前地点已经走过
                MAZE[nextnode[0]][nextnode[1]] = 1
                break
        else:
            #  记录当前地点已经走过
            MAZE[nextnode[0]][nextnode[1]] = 1
            # 取出栈顶，丢弃
            stack.pop()
    # 如果while循环完没有，那么说明没有路
    else:
        print('没有路')
        return False

mig(1,1,2,6)
