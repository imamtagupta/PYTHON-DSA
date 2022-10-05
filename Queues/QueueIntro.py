from queue import Queue

q1 = Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)



def displayQueue(q):
    while not q.empty():
        print(q.get())


# displayQueue(q1)
def reverseQueue(q):
    if q.empty():
        return
    print(q.get)
    reverseQueue(q)


reverseQueue(q1)
