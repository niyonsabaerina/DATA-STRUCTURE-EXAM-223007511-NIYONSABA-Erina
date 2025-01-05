class Node:
    def __init__(self, order_id, survey_responses):
        self.order_id = order_id  
        self.survey_responses = survey_responses  
        self.next = None  

class SinglyLinkedList:
    def __init__(self, max_orders):
        self.head = None 
        self.max_orders = max_orders  
        self.order_count = 0  

    
    def add_order(self, order_id, survey_responses):
        if self.order_count >= self.max_orders:
            print("Cannot add order: The list is full.")
            return
        
        new_node = Node(order_id, survey_responses)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.order_count += 1
        print(f"Order {order_id} added successfully.")
        
    # Method to display all orders in the list
    def display_orders(self):
        if not self.head:
            print("No orders to display.")
            return
        
        current = self.head
        while current:
            print(f"Order ID: {current.order_id}, Survey Responses: {current.survey_responses}")
            current = current.next
            
    # Method to delete an order by its order_id
    def delete_order(self, order_id):
        if not self.head:
            print("The list is empty.")
            return
        
        # Special case: deleting the first order
        if self.head.order_id == order_id:
            self.head = self.head.next
            self.order_count -= 1
            print(f"Order {order_id} deleted successfully.")
            return
        
        current = self.head
        while current.next:
            if current.next.order_id == order_id:
                current.next = current.next.next
                self.order_count -= 1
                print(f"Order {order_id} deleted successfully.")
                return
            current = current.next
        
        print(f"Order {order_id} not found.")


order_list = SinglyLinkedList(max_orders=3)


order_list.add_order(101, ["Age: 25-34", "Gender: Male", "Rating: 4"])
order_list.add_order(102, ["Age: 18-24", "Gender: Female", "Rating: 5"])
order_list.add_order(103, ["Age: 35-44", "Gender: Male", "Rating: 3"])
order_list.add_order(104, ["Age: 45-54", "Gender: Female", "Rating: 2"])

order_list.display_orders()

order_list.delete_order(102)

order_list.display_orders()

order_list.delete_order(104)
