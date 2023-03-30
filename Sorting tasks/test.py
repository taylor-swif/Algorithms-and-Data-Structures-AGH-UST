from queue import PriorityQueue

que = PriorityQueue(3)

que.put((2,'a'))
que.put((1,'b'))
que.put((3,'c'))
print(que.full())
que.maxsize() = 4
que.put((5,'d'))
print("pomidor")
print(que.full())
