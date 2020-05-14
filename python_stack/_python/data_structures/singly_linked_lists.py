class SLNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, value):
        # If there are no existing nodes in this list, then just use add_to_front()
        if self.head == None:
            self.add_to_front(value)
            return self
        else:
            # Use a runner to move to the tail of the list.
            runner = self.head
            while runner.next != None:
                runner = runner.next
            new_node = SLNode(value)
            runner.next = new_node
            new_node.next = None
            return self

    # Remove the first node and return its value
    def remove_from_front(self):
        if self.head == None:
            print("The list is empty, nothing to remove.")
            return self

        runner = self.head
        self.head = runner.next
        return self

    # Remove the last node and return its value
    def remove_from_back(self):
        # Have two runners, one behind the other. When the first reaches the end (the last item),
        # Have the runner behind it (runner2), point to None, so it becomes the last item in the list
        runner1 = self.head
        runner2 = self.head
        # If there is only one node in this list just point self.head to None.
        if runner1.next == None:
            self.head = None
            return self

        while runner1.next != None:
            runner2 = runner1
            runner1 = runner1.next
        runner2.next = None
        return self

    def remove_val(self, val):
        # Remove the first node with the given value
        # Special case: Check if the first item in the list is a match
        runner1 = runner2 = self.head
        if runner1.value == val:
            self.head = runner1.next
            return self

        while runner1 != None:
            if runner1.value == val:
                runner2.next = runner1.next
                return self
            else:
                runner2 = runner1
                runner1 = runner1.next
        return self

    # TODO: Insert a node with value val as the nth node in the list
    def insert_at(self, val, n):
        # Check for 0th node position, or empty list. In either case just call add_to_front()
        if n == 0 or self.head == None:
            self.add_to_front(val)
            return self

        # Count nodes and insert just before node=n
        new_node = SLNode(val)
        node = 0
        runner1 = runner2 = self.head
        while runner1 != None:
            if node == n:
                # Insert here, just before current
                new_node.next = runner2.next
                runner2.next = new_node
                return self
            runner2 = runner1
            runner1 = runner1.next
            node += 1
        # We're at the last item in the list. The nth Value is larger than the list size.
        # Insert here, at the end of the list. Just call add_to_back()
        self.add_to_back(val)
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self


print("\n******************* Origin List ***************************************\n")
mylist = SList()
mylist.add_to_front("loretta").add_to_front("bobby").add_to_front("josh").add_to_front("arlene").add_to_front("keith").add_to_front(
    "eric").add_to_back("sydney").print_values()

print("\n**** remove from front **********\n")
mylist.remove_from_front().print_values()
print("\n**** remove from back **********\n")
mylist.remove_from_back().print_values()
print("\n*** remove val(keith) First item in the list ***********\n")
mylist.remove_val("keith").print_values()
print("\n*** remove val(josh) ***********\n")
mylist.remove_val("josh").print_values()
print("\n**** remove val(loretta) *** Last item in the list *******\n")
mylist.remove_val("loretta").print_values()
print("\n********** insert_at() ************************************************\n")
mylist.insert_at("Insert at 0", 0).insert_at(
    "Insert at 3", 3).insert_at("Insert at 4", 4).insert_at("Insert at 100 (beyond end of list. Defaults to add_to_back()", 100).print_values()
print("\n***********************************************************************\n")
