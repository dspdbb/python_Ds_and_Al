class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]  # 创建size长度的列表
        self.size = size
        self.rear = 0  # 队首指针
        self.front = 0  # 队尾指针

    # 进队列
    def push(self, element):
        if not self.is_filled():
            # 判断队首指针的位置
            self.rear = (self.rear + 1) % self.size
            # 将循环列表的rear位置将外部参数element放进来
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front
    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue()
for i in range(4):
    q.push(i)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
