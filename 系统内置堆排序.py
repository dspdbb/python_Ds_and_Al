import random
import heapq  # 优先队列

li = list(range(10))
random.shuffle(li)
print(li)

heapq.heapify(li)  # 建堆
for i in range(len(li)):
    print(heapq.heappop(li), end=' ')
