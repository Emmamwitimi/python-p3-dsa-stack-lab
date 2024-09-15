class Stack:
    def __init__(self, items=None, limit=None):
        # Initialize the stack with a list of items or an empty list
        self.items = items if items is not None else []
        # Set the limit for the stack size, if provided
        self.limit = limit

    def push(self, value):
        # Check if the stack is full before pushing a new element
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(value)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        # Remove the top element from the stack
        if not self.isEmpty():
            return self.items.pop()
        else:
            # Return None instead of raising an error if the stack is empty
            return None

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def full(self):
        # Check if the stack is full
        if self.limit is not None:
            return len(self.items) >= self.limit
        return False

    def search(self, value):
        # Return the distance from the top to the target element
        if value in self.items:
            return len(self.items) - 1 - self.items.index(value)
        return -1
