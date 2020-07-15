//****************************************************************************
// Back/Remove/Add
//****************************************************************************
//
// SList: Back
// Create a function that accepts a ListNode pointer and returns the last 
// value in the list.
//
// SList: Remove Back
// Create a standalone function that removes the last ListNode in the list 
// and returns the new list.
//
// SList: Add Back
// Create a function that creates a ListNode with given value and inserts it 
// at end of a linked list.
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

    // Return the number of nodes in the list
    length() {
        let runner = this.head;
        let counter = 0;
        while (runner) {
            runner = runner.next;
            counter++;
        }
        return counter
    }

    min() {
        console.log('\n**** min ****')
        let runner = this.head;
        let min = runner.value;
        while (runner) {
            if (runner.value < min) {
                min = runner.value;
            }
            runner = runner.next;
        }
        return min
    }

    max() {
        console.log('\n**** max ****')
        let runner = this.head;
        let max = runner.value;
        while (runner) {
            if (runner.value > max) {
                max = runner.value;
            }
            runner = runner.next;
        }
        return max
    }

    avg() {
        console.log('\n**** avg ****')
        let runner = this.head;
        let avg = 0;
        let sum = 0;
        let length = this.length()
        while (runner) {
            sum += runner.value;
            runner = runner.next;
        }
        avg = sum / length;
        return avg;
    }

    back() {
        console.log('\n**** Back: return the value of the last node ****')
        let runner = this.head;
        let last_node_value = 0;
        while (runner.next) {
            runner = runner.next;
        }
        last_node_value = runner.value;
        return last_node_value;
    }

    remove_back() {
        console.log('\n**** Remove Back: Remove the last node ****')
        let runner = this.head;

        // Save this 'lagging' pointer we'll need it to be the new last 
        // (and change its next pointer to null)
        let runner2 = runner;
        while (runner.next) {
            runner2 = runner;
            runner = runner.next;
        }
        runner2.next = null;
        return;
    }

    add_back(val) {
        console.log('\n**** Add Back: Add new node to the back/end of the list ****')

        // Create the new node
        this.new_node = new Node(val);

        // We know it's next is null - it will be at the back(last)
        this.new_node.next = null;

        let runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = this.new_node;
        return;
    }

}

// Create a new list instance, and add some nodes.
my_list = new SLL(1).addFront(2).addFront(3).addFront(4).addFront(5).addFront(6).addFront(7).addFront(-1);

// Show all nodes in the list
my_list.show_all();

// Display the last value in the list
console.log('The value of the last node is: ', my_list.back());

// Remove the last node (back)
my_list.remove_back();

// Show all nodes in the list
my_list.show_all();

// Add new node to the back
my_list.add_back(27);

// Show all nodes in the list
my_list.show_all();