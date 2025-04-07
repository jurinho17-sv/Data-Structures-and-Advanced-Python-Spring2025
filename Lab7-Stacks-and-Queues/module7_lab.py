# ========================================================
# CS 034 #39575
# Professor. Jamal Ashraf
# Lab 7 Group 15
# Name: Ju Ho Kim(10671687), Sangmin Kim(10664950)
# Lab 7: Implementing Stacks and Queues
# GitHub URL: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab7-Stacks-and-Queues
# ========================================================



# ----- PART A: Stack Implementation (Ticket Cancellation Management) -----

class Node:
    """
    Node class for the linked list implementation of a Stack.
    Each node contains ticket cancellation details and a reference to the next node.
    """
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The ticket cancellation details
        """
        self.data = data    # Ticket cancellation details
        self.next = None    # Reference to the next node
        
class Stack:
    """
    Stack implementation using a linked list for ticket cancellation management.
    Implements LIFO (Last-In-First-Out) behavior.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.top = None     # Reference to the top node
        self.size = 0       # Track the number of nodes in the stack
    
    def push(self, cancellation_details):
        """
        Add a new ticket cancellation to the top of the stack.
        
        Args:
            cancellation_details: Information about the ticket cancellation
        """
        # Create a new node with the cancellation details
        new_node = Node(cancellation_details)
        
        # Make the new node point to the current top
        new_node.next = self.top
        
        # Update the top to be the new node
        self.top = new_node
        
        # Increment the size
        self.size += 1
    
    def pop(self):
        """
        Remove and return the most recent ticket cancellation from the stack.
        
        Returns:
            The cancellation details from the top of the stack
            
        Raises:
            Exception: If the stack is empty
        """
        # Check if the stack is empty
        if self.is_empty():
            raise Exception("Stack is empty - no cancellations to process")
        
        # Get the data from the top node
        cancellation = self.top.data
        
        # Move the top pointer to the next node
        self.top = self.top.next
        
        # Decrement the size
        self.size -= 1
        
        # Return the data
        return cancellation
    
    def peek(self):
        """
        View the most recent ticket cancellation without removing it.
        
        Returns:
            The cancellation details from the top of the stack
            
        Raises:
            Exception: If the stack is empty
        """
        # Check if the stack is empty
        if self.is_empty():
            raise Exception("Stack is empty - no cancellations to view")
        
        # Return the data from the top node without removing it
        return self.top.data
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise
        """
        return self.top is None
    
    def get_size(self):
        """
        Get the number of ticket cancellations in the stack.
        
        Returns:
            The number of elements in the stack
        """
        return self.size
        


# ----- PART B: Queue Implementation (Customer Service Call Handling) -----

class Queue:
    """
    Queue implementation using an array for customer service call handling.
    Implements FIFO (First-In-First-Out) behavior.
    """
    def __init__(self, capacity=10):
        """
        Initialize an empty queue with the given capacity.
        
        Args:
            capacity: Initial size of the underlying array (default: 10)
        """
        self.array = [None] * capacity  # Create an array of the specified capacity
        self.front = 0                  # Index of the front element
        self.rear = -1                  # Index of the rear element
        self.size = 0                   # Current number of elements in the queue
        self.capacity = capacity        # Maximum capacity of the array
    
    def enqueue(self, call_details):
        """
        Add a new customer service call to the end of the queue.
        
        Args:
            call_details: Information about the customer service call
        """
        # Check if the queue is full and needs to be resized
        if self.size == self.capacity:
            self._resize()
        
        # Update the rear pointer and handle wrap-around
        self.rear = (self.rear + 1) % self.capacity
        
        # Add the call details to the queue
        self.array[self.rear] = call_details
        
        # Increment the size
        self.size += 1
        
    def _resize(self):
        """
        Double the capacity of the queue's underlying array when it becomes full.
        This is a private helper method.
        """
        # Create a new array with double the capacity
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        
        # Copy elements from the old array to the new array, starting from front
        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]
        
        # Update the queue's attributes
        self.array = new_array
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1
    
    def dequeue(self):
        """
        Remove and return the earliest customer service call from the queue.
        
        Returns:
            The call details from the front of the queue
            
        Raises:
            Exception: If the queue is empty
        """
        # Check if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty - no customer calls to process")
        
        # Get the data from the front of the queue
        call = self.array[self.front]
        
        # Set the front element to None (optional cleanup)
        self.array[self.front] = None
        
        # Move the front pointer and handle wrap-around
        self.front = (self.front + 1) % self.capacity
        
        # Decrement the size
        self.size -= 1
        
        # Return the data
        return call
    
    def peek(self):
        """
        View the earliest customer service call without removing it.
        
        Returns:
            The call details from the front of the queue
            
        Raises:
            Exception: If the queue is empty
        """
        # Check if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty - no customer calls to view")
        
        # Return the data from the front of the queue without removing it
        return self.array[self.front]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def get_size(self):
        """
        Get the number of customer service calls in the queue.
        
        Returns:
            The number of elements in the queue
        """
        return self.size



# ----- Example Usage -----

def demonstrate_stack():
    """Demonstrate the functionality of the Stack implementation."""
    print("Creating a new ticket cancellation stack...")
    stack = Stack()
    
    print(f"Is the stack empty? {stack.is_empty()}")
    print(f"Stack size: {stack.get_size()}")
    
    print("\nAdding ticket cancellations to the stack:")
    
    # Adding cancellations to the stack
    cancellations = [
        {"ticket_id": "T1001", "event": "Concert", "customer": "John Doe", "reason": "Schedule conflict"},
        {"ticket_id": "T1002", "event": "Theater", "customer": "Jane Smith", "reason": "Illness"},
        {"ticket_id": "T1003", "event": "Sports", "customer": "Mike Johnson", "reason": "Travel issues"}
    ]
    
    for i, cancellation in enumerate(cancellations, 1):
        print(f"Adding cancellation #{i}: Ticket {cancellation['ticket_id']} for {cancellation['event']}")
        stack.push(cancellation)
        print(f"Stack size is now: {stack.get_size()}")
    
    print("\nChecking the most recent cancellation (peek):")
    recent = stack.peek()
    print(f"Most recent cancellation: Ticket {recent['ticket_id']} for {recent['event']} by {recent['customer']}")
    
    print("\nProcessing cancellations (LIFO order):")
    while not stack.is_empty():
        cancellation = stack.pop()
        print(f"Processing: Ticket {cancellation['ticket_id']} for {cancellation['event']} by {cancellation['customer']}")
        print(f"Reason: {cancellation['reason']}")
        print(f"Remaining cancellations: {stack.get_size()}")
    
    print("\nAttempting to process a cancellation from an empty stack:")
    try:
        stack.pop()
    except Exception as e:
        print(f"Error: {e}")

def demonstrate_queue():
    """Demonstrate the functionality of the Queue implementation."""
    print("Creating a new customer service call queue...")
    queue = Queue()
    
    print(f"Is the queue empty? {queue.is_empty()}")
    print(f"Queue size: {queue.get_size()}")
    
    print("\nAdding customer service calls to the queue:")
    
    # Adding calls to the queue
    calls = [
        {"call_id": "C001", "customer": "Alice Brown", "issue": "Payment problem", "priority": "Medium"},
        {"call_id": "C002", "customer": "Bob Wilson", "issue": "Ticket not received", "priority": "High"},
        {"call_id": "C003", "customer": "Carol Davis", "issue": "Event information", "priority": "Low"},
        {"call_id": "C004", "customer": "David Miller", "issue": "Refund request", "priority": "Medium"}
    ]
    
    for i, call in enumerate(calls, 1):
        print(f"Adding call #{i}: {call['call_id']} from {call['customer']} about {call['issue']}")
        queue.enqueue(call)
        print(f"Queue size is now: {queue.get_size()}")
    
    print("\nChecking the next call to be handled (front):")
    next_call = queue.peek()
    print(f"Next call: {next_call['call_id']} from {next_call['customer']} - {next_call['issue']} (Priority: {next_call['priority']})")
    
    print("\nProcessing customer service calls (FIFO order):")
    while not queue.is_empty():
        call = queue.dequeue()
        print(f"Handling call: {call['call_id']} from {call['customer']}")
        print(f"Issue: {call['issue']} (Priority: {call['priority']})")
        print(f"Remaining calls in queue: {queue.get_size()}")
    
    print("\nAttempting to process a call from an empty queue:")
    try:
        queue.dequeue()
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting queue resizing:")
    print("Adding 15 calls to demonstrate automatic resizing...")
    for i in range(1, 16):
        queue.enqueue({"call_id": f"C{1000+i}", "customer": f"Customer {i}", "issue": "Test call", "priority": "Low"})
    
    print(f"Queue size after adding 15 calls: {queue.get_size()}")
    print(f"Queue capacity after resizing: {queue.capacity}")

# Main execution
if __name__ == "__main__":
    print("===== TICKET CANCELLATION STACK DEMONSTRATION =====")
    demonstrate_stack()
    
    print("\n===== CUSTOMER SERVICE CALL QUEUE DEMONSTRATION =====")
    demonstrate_queue()