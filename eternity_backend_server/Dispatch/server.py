import time
from eternity_backend_server.Dispatch import Dispatch

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

# if __name__ == '__main__':
#     dispatchList = Queue()
#     a = Dispatch()
#     dispatchList.enqueue(a)
#     b = Dispatch()
#     dispatchList.enqueue(b)
#     c = Dispatch()
#     dispatchList.enqueue(c)
#     d = Dispatch()
#     dispatchList.enqueue(d)
#     print(dispatchList.items)
#     for i in dispatchList.items:
#         i.Print()
#
#
#     print("================== WORKING =================")
#     while 1:
#         print("=================================")
#         wordid = dispatchList.dequeue()
#         print(wordid)
#         print(dispatchList.items)
#         time.sleep(2)
#         dispatchList.enqueue(wordid)
#         print(dispatchList.items)
#
