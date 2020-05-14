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
        if self.tail == None:
            return self

        # List is not empty delete the last item
        new_tail_item = self.tail.prev          # This will be the new 'last/tail' item
        self.tail = new_tail_item
        new_tail_item.next = None
        return self

    def delete_val(self, value):
        # Check for empty list
        if self.head == None:
            return self

        # List is not empty. Traverse list for first occurance of item with value
        runner = self.head
        while runner != None:
            if runner.value == value:
                # If we're trying to delete the last item in the list
                # just set tail and head to None and exit
                if runner.prev == None and runner.next == None:
                    self.head = self.tail = None
                    return self

                # If this is the first item there is no previous item
                if runner.prev == None:
                    # Just point the head to the new first item
                    self.head = runner.next
                else:
                    runner.prev.next = runner.next

                # If this is the last item this is no next item
                if runner.next == None:
                    # Just point the tail to the new item
                    self.tail = runner.prev
                else:
                    runner.next.prev = runner.prev

                return self

            else:   # Keep traversiing
                runner = runner.next

        return self

    def insert_at(self, val, n):
        # Check for 0th node position, or empty list. In either case just call add_to_front()
        if n == 0 or self.head == None:
            self.add_to_front(val)
            return self

        # Count nodes and insert just before node=n
        new_node = DLNode(val)
        node = 0
        runner = self.head
        while runner != None:
            if node == n:
                # Insert here, just before current

                # New node points to the current
                new_node.next = runner

                # New node prev points to what current previous pointed to
                new_node.prev = runner.prev

                # Point item before the current item to the new node, instead of current item
                runner.prev.next = new_node

                # Runner previous now points to the new node
                runner.prev = new_node

                return self

            # Location to insert new node not found. Keep traversing and counting node position.
            runner = runner.next
            node += 1

        # We're at the last item in the list. The nth Value is larger than the list size.
        # Insert here, at the end of the list. Just call add_to_back()
        self.add_to_end(val)

        return self

    def print_values(self):
        # Check for empty list
        if self.head == None and self.tail == None:
            print("*** Empty List: Nothing to print ***")
            return self

        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    # Print all the values in the list, starting at the END (tail) of the list
    # This will print the list items in the reverse order of the print_values() method.
    # This helped me test that my previous pointers are correct.
    def print_values_from_tail(self):
        # Check for empty list
        if self.head == None and self.tail == None:
            print("*** Empty List: Nothing to print ***")
            return self

        runner = self.tail
        while runner != None:
            print(runner.value)
            runner = runner.prev
        return self


mylist = DLList()

print("\n**************** Create new list with some names and print from head to tail **************")
mylist.add_to_front("keith").add_to_front("sydney").print_values()

print("\n**************** insert_at(eric, 1) ***( between sydney and keith *************************")
mylist.insert_at("eric", 1).print_values()

print("\n*************** Test add_to_end('arlene') ***********************************************\n")

# Now test add_to_end()
mylist.add_to_end("arlene").print_values()

# Test printing nodes from the end of the list (tail), towards the head
print("\n**************** Print from tail backwards ***********************************************\n")
mylist.print_values_from_tail()

# Test deleting from head/begining of list
print("\n**************** Delete first item in list (sydeny) **************************************\n")
mylist.delete_from_head().print_values()

# Test deleting from end/tail of list
print("\n**************** Delete last item in list (arlene) ***************************************\n")
mylist.delete_from_tail().print_values()

# Test printing nodes from the end of the list (tail), towards the head
print("\n**************** Print from tail backwards ***********************************************\n")
mylist.print_values_from_tail()

# Add one more name (so we hav three)
print("\n**************** Add new name josh********************************************************\n")
mylist.add_to_front("josh").print_values()

# Add delete by value
print("\n**************** Delete by value - eric **************************************************\n")
mylist.delete_val("eric").print_values()

print("\n**************** Delete by value - josh **************************************************\n")
mylist.delete_val("josh").print_values()

print("\n**************** Delete by value - keith *************************************************\n")
mylist.delete_val("keith").print_values()


print("\n**************** Print again, from tail to head ******************************************\n")
mylist.print_values_from_tail()

print("\n*************************************** Done *********************************************\n")
