from collections import deque

q = deque([1,2,3],7)
q.append(4)  # 队尾进队
print(q.popleft())  # 队首出队

# 用于双向队列
# q.appendleft()  # 队首进队
# q.pop()  # 队尾出队
