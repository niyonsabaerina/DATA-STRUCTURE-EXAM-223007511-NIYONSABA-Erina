class Deque:
    def __init__(self, max_size):
        self.max_size = max_size  
        self.deque = []  

    def append(self, item):
        """Add an item to the back of the deque"""
        if len(self.deque) < self.max_size:
            self.deque.append(item)
            print(f"Added to back: {item}")
        else:
            print("Deque is full! Cannot add item.")
    
    def appendleft(self, item):
        """Add an item to the front of the deque"""
        if len(self.deque) < self.max_size:
            self.deque.insert(0, item)
            print(f"Added to front: {item}")
        else:
            print("Deque is full! Cannot add item.")
    
    def pop(self):
        """Remove and return an item from the back of the deque"""
        if self.deque:
            item = self.deque.pop()
            print(f"Removed from back: {item}")
            return item
        else:
            print("Deque is empty! Cannot pop item.")
    
    def popleft(self):
        """Remove and return an item from the front of the deque"""
        if self.deque:
            item = self.deque.pop(0)
            print(f"Removed from front: {item}")
            return item
        else:
            print("Deque is empty! Cannot pop item.")
    
    def peek_front(self):
        """View the front item without removing it"""
        if self.deque:
            return self.deque[0]
        else:
            print("Deque is empty! No front item.")
            return None
    
    def peek_back(self):
        """View the back item without removing it"""
        if self.deque:
            return self.deque[-1]
        else:
            print("Deque is empty! No back item.")
            return None
    
    def display(self):
        """Display the entire deque"""
        if self.deque:
            print("Deque contents:")
            for item in self.deque:
                print(item)
        else:
            print("Deque is empty.")


survey_deque = Deque(max_size=5)

survey_deque.append("Survey Response 1: Age: 25-34, Gender: Male, Rating: 4")
survey_deque.append("Survey Response 2: Age: 18-24, Gender: Female, Rating: 5")
survey_deque.appendleft("Survey Response 3: Age: 35-44, Gender: Male, Rating: 3")
survey_deque.append("Survey Response 4: Age: 45-54, Gender: Female, Rating: 2")

survey_deque.display()

print(f"Front item: {survey_deque.peek_front()}")
print(f"Back item: {survey_deque.peek_back()}")

survey_deque.pop()
survey_deque.popleft()


survey_deque.display()
