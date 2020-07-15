//****************************************************************************
// Contains 
//****************************************************************************
//
// Sam thinks Tad might be somewhere in a very long line waiting to attend 
// the Superman movie. Given a ListNode pointer and a val, return whether 
// val is found in any node in the list.
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

    // Check whether any node contains a specific value
    contains(val) {
        console.log('\n**** contains ****')
        let runner = this.head;
        while (runner) {
            if (runner.value == val) {
                return true;
            }
            runner = runner.next;
        }
    }
}

// Create a new list instance, and add some nodes.
my_list = new SLL('Keith').addFront('Eric').addFront('Arlene').addFront('Tad').addFront('Sydney')

// Show all nodes in the list
my_list.show_all();

// Determine whether any node contains 
console.log('Does the list contain Tad?:', my_list.contains('Tad'));