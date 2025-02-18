class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        self._size = self._size +1
        node = Node(data)
        # 1. rear에 있는 값이 None인지
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError('dequeue from empty queue')
        self._size = self._size -1
        temp = self.front   # backup
        self.front = self.front.next    #update
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self) -> int:
        return self._size



if __name__ == "__main__":
    q = Queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    print(f'q.size: {q.size()}')
    for i in range(q.size()):
        print(f'q.dequeue: {q.dequeue()}') # return있음
    print(f'q.size: {q.size()}')