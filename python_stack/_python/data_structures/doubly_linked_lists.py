class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        current_head = self.head    # Save current head and tail values
        current_tail = self.tail
        new_node = DLNode(value)    # Create new node.

        # If we're adding to an empty list:
        if self.head == None and self.tail == None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            return self

        # otherwise we're adding the new node to the head of the list
        self.head = new_node
        new_node.next = current_head
        new_node.prev = None
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self


mylist = DLList()

# Test add_to_front() and print_values()
mylist.add_to_front("keith").add_to_front(
    "eric").add_to_front("sydney").print_values()

# Now test add_to_back()
# mylist.add_to_back("arlene").print_values()
