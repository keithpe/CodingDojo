//****************************************************************************
// Fronts 
//****************************************************************************
//
// Add Front
// Write a method that accepts a value and create a new node, assign it to 
// the list head, and return a pointer to the new head node.
// 
// Remove Front
// Write a method to remove the head node and return the new list head node. 
// If the list is empty, return null.
// 
// Front
// Write a method to return the value (not the node) at the head of the list. 
// If the list is empty, return null.
//
//****************************************************************************

// Node Class
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// Singly linked list
class SLL {
    constructor(value) {
        this.head = new Node(value);
        return this;
    }

    // Add a new node to the head of the list
    addFront(value) {
        this.new_node = new Node(value);
        this.new_node.next = this.head;
        this.head = this.new_node
        return this;
    }

    // Remove the node at the head 
    removeFront() {
        // Only remove if list NOT empty.
        if (this.head) {
            this.head = this.head.next
        }
        return this;
    }

    // Display the value contained in the head node
    front() {
        if (this.head) {
            console.log('The value of Front is:', this.head.value)
        }
    }

    // Display all nodes in the list
    show_all() {
        console.log('\n**** Display Nodes ****')
        let runner = this.head;
        while (runner) {
            console.log(runner.value)
            runner = runner.next;
        }
    }
}

// Create a new list instance, and add some nodes.
my_list = new SLL('Keith').addFront('Eric').addFront('Arlene').addFront('Sydney').removeFront();

// Show all nodes in the list
my_list.show_all();
my_list.addFront('Sydney').addFront('Bernie');
my_list.show_all();

// Display the value contained in the node at the head.
my_list.front();