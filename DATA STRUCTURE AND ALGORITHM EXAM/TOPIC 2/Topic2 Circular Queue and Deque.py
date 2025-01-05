class CircularQueue:
    def __init__(self, size):
        self.size = size 
        self.queue = [None] * size 
        self.front = -1  
        self.rear = -1  
    
    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot add item.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Added to queue: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot remove item.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Removed from queue: {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty! No front item.")
            return None
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size


survey_queue = CircularQueue(3)

survey_queue.enqueue("Survey Response 1: Age: 25-34, Gender: Male, Rating: 4")
survey_queue.enqueue("Survey Response 2: Age: 18-24, Gender: Female, Rating: 5")
survey_queue.enqueue("Survey Response 3: Age: 35-44, Gender: Male, Rating: 3")
survey_queue.enqueue("Survey Response 4: Age: 45-54, Gender: Female, Rating: 2")

survey_queue.display()

survey_queue.dequeue()
survey_queue.enqueue("Survey Response 5: Age: 30-40, Gender: Male, Rating: 4")
survey_queue.display()

class Deque:
    def __init__(self, size):
        self.size = size  
        self.deque = [None] * size  
        self.front = -1 
        self.rear = -1   
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def append(self, item):
        if self.is_full():
            print("Deque is full! Cannot add item.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = item
        print(f"Added to back: {item}")
    
    def appendleft(self, item):
        if self.is_full():
            print("Deque is full! Cannot add item.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = item
        print(f"Added to front: {item}")
    
    def pop(self):
        if self.is_empty():
            print("Deque is empty! Cannot pop item.")
            return None
        item = self.deque[self.rear]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        print(f"Removed from back: {item}")
        return item
    
    def popleft(self):
        if self.is_empty():
            print("Deque is empty! Cannot pop item.")
            return None
        item = self.deque[self.front]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Removed from front: {item}")
        return item
    
    def peek_front(self):
        if self.is_empty():
            print("Deque is empty! No front item.")
            return None
        return self.deque[self.front]
    
    def peek_back(self):
        if self.is_empty():
            print("Deque is empty! No back item.")
            return None
        return self.deque[self.rear]
    
    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        i = self.front
        while True:
            print(self.deque[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

survey_deque = Deque(3)

survey_deque.append("Survey Response 1: Age: 25-34, Gender: Male, Rating: 4")
survey_deque.append("Survey Response 2: Age: 18-24, Gender: Female, Rating: 5")
survey_deque.appendleft("Survey Response 3: Age: 35-44, Gender: Male, Rating: 3")
survey_deque.display()

survey_deque.pop()
survey_deque.append("Survey Response 4: Age: 45-54, Gender: Female, Rating: 2")
survey_deque.display()

survey_deque.popleft()
survey_deque.display()
