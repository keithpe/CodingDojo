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

        # Point the node that WAS at the head (first), and WAS pointing to None
        # to the new_node, and the new node prev pointer will point to None.
        current_head.prev = new_node
        new_node.prev = None
        return self

    def add_to_end(self, value):  # add a new node to the end of the list,
        # First, test if list is empty, and just call add_to_front()
        if self.head == None and self.tail == None:
            self.add_to_front(value)
            return self

        # Otherwise, add new item at end of list
        new_node = DLNode(value)        # Create the new node
        current_tail = self.tail        # Save the current last item (tail)
        self.tail.next = new_node       # Point current last item to new node
        new_node.next = None            # new node is new last/tail item in list
        new_node.prev = current_tail    # Point new node prev to previous last item
        self.tail = new_node            # New node is now last item
        return self

    def delete_from_head(self):  # Delete the first item in the list
        # If the list is empty just exit
        if (self.head == None):
            return self

        # List is not empty delete the first item
        new_head_item = self.head.next          # This will be the new 'first/head' item
        self.head = new_head_item               # point head to new first item
        new_head_item.prev = None               # Set prev pointer of new first item
        return self

    def delete_from_tail(self):
        # If the list is empty, just exit
        if (self.tail == None):
            return self

        # List is not empty delete the last item
        new_tail_item = self.tail.prev          # This will be the new 'last/tail' item
        self.tail = new_tail_item
        new_tail_item.next = None
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    # Print all the values in the list, starting at the END (tail) of the list
    # This will print the list items in the reverse order of the print_values() method.
    # This helped me test that my previous pointers are correct.
    def print_values_from_tail(self):
        runner = self.tail
        while runner != None:
            print(runner.value)
            runner = runner.prev
        return self


mylist = DLList()

# Test add_to_front() and print_values()

print("\n**************** Create new list with some names and print from head to tail **************")
mylist.add_to_front("keith").add_to_front(
    "eric").add_to_front("sydney").print_values()

print("\n*************** Test add_to_end('arlene') ***********************************************\n")

# Now test add_to_end()
mylist.add_to_end("arlene").print_values()

# Test printing nodes from the end of the list (tail), towards the head
print("\n**************** Print from tail backwards ***********************************************\n")
mylist.print_values_from_tail()

# Test deleting from head/begining of list
print("\n**************** Delete first item in list (sydeny) ***********************************************\n")
mylist.delete_from_head().print_values()

# Test deleting from end/tail of list
print("\n**************** Delete last item in list (arlene) ***********************************************\n")
mylist.delete_from_tail().print_values()

# Test printing nodes from the end of the list (tail), towards the head
print("\n**************** Print from tail backwards ***********************************************\n")
mylist.print_values_from_tail()
