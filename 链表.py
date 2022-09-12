class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(a.next.next.item)


# 头插入法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


# 尾插法
def create_linklist_tail(li):
    # 根据第一个元素创建头节点
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        # 将尾巴下一个链接到现在的tail
        tail.next = node
        # 让新的tail等于新的位结点
        tail = node
    return head


def print_linklist(pl):
    while pl:
        print(pl.item, end=",")
        pl = pl.next


a = create_linklist_head([1, 2, 3])
b = create_linklist_tail([2, 3, 4])
print_linklist(a)
print('\t')
print_linklist(b)
