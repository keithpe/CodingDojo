//****************************************************************************
// Length
//****************************************************************************
//
// July 20, 2013: about 5000 people wait in line
// for a chance to audition
// for American Idol.Create a
//
// function that accepts a pointer to the first list node, and returns number 
// of nodes in that SList.
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

// Return how many nodes in the list
console.log('There are ' + my_list.length() + ' nodes in the list.')