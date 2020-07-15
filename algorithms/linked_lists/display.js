//****************************************************************************
// Display 
//****************************************************************************
//
// Create display(node) for debugging that returns a string containing all 
// list values. Build what you wish console.log(myList) did!h
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
        console.log('\n**** Show all Nodes ****')
        let runner = this.head;
        while (runner) {
            console.log(runner.value)
            runner = runner.next;
        }
    }

    display() {
        console.log('\n**** Display Nodes (in a single string) ****')
        let runner = this.head;
        let node_values = '';
        while (runner) {
            node_values += (runner.value + ' ')
            runner = runner.next;
        }
        return node_values;
    }

    // Return the number of nodes in the list
    length() {
        console.log('\n**** Length of List (# of nodes) ****')
        let runner = this.head;
        let counter = 0;
        while (runner) {
            runner = runner.next;
            counter++;
        }
        return counter
    }
}

// Create a new list instance, and add some nodes.
my_list = new SLL('Keith').addFront('Eric').addFront('Arlene').addFront('Sydney');

// Show all nodes in the list
my_list.show_all();

// Display a string containing the values for ALL nodes in the list.
console.log(my_list.display());