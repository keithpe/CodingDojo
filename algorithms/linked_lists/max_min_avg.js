//****************************************************************************
// Max/Min/Average
//****************************************************************************
// 
// SList: Max
// American Idol seems to air singers that are the best, and a few that seem 
// like the worst! Create function max(node) to return list’s largest val.
//
// SList: Min
// Create min(node) to return list’s smallest val. 
//
// SList: Average
// Create average(node) to return average val.
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
}

// Create a new list instance, and add some nodes.
my_list = new SLL(1).addFront(2).addFront(3).addFront(4).addFront(5).addFront(6).addFront(7).addFront(-1);

// Show all nodes in the list
my_list.show_all();

// Return the min value in the list
console.log('The min value in the list is ' + my_list.min());

// Return the max value in the list
console.log('The max value in the list is ' + my_list.max());

// Return the avg value in the list
console.log('The avg value in the list is ' + my_list.avg());