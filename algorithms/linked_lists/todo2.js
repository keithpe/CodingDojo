//****************************************************************************
// Todo2
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

    // Display all nodes in the list
    show_all() {
        console.log('\n**** Display Nodes ****')
        let runner = this.head;
        while (runner) {
            console.log(runner.value)
            runner = runner.next;
        }
    }

    //****************************************************************************
    // SList: Second to Last Value
    // Create a standalone function that, given a pointer to the first node in 
    // a singly linked list, will return the second-to-last value in that list. 
    // What will you return if the list is not long enough?
    // If the list is NOT long enough, we'll return NULL
    //****************************************************************************
    secondToLast() {
        console.log('\n**** Second To Last ****')
        let count = 0;
        let runner = this.head;
        let runner2 = runner;
        while (runner.next) {
            count++;
            runner2 = runner
            runner = runner.next;
        }
        if (count > 1) {
            return runner2;
        } else {
            return null;
        }
    }


    //****************************************************************************
    // SList: Delete Given Node
    // Create ListNode method removeSelf() to disconnect(remove) itself from 
    // linked lists that include it.
    // Note: the node might be the first in a list(it won’ t be the last), 
    // and you do NOT have a pointer to the previous node.
    // Also, don’ t lose any subsequent nodes pointed to by.next.
    //****************************************************************************

    removeSelf(value) {
        console.log('\n**** removeSelf(value) ****')
        let runner = this.head;
        let runner2 = runner;
        while (runner.next) {
            if (runner.value === value) {
                runner2.next = runner.next;
                return runner.value
            }
            runner2 = runner
            runner = runner.next;
        }
        return null

    }
}

// Create a new list instance, and add some nodes.
my_list = new SLL('Keith').addFront('Eric').addFront('Arlene').addFront('Sydney');
my_short_list = new SLL('Only One Node');

// Show all nodes in the list
my_list.show_all();


// Remove a node from the list
let removedNode = my_list.removeSelf('Eric')
if (removedNode) {
    console.log('Removed Node is:', removedNode);
} else {
    console.log('Node NOT found, not removed')
}

// Show all nodes in the list
my_list.show_all();

let second_to_last = my_list.secondToLast();
if (second_to_last) {
    console.log('second_to_last:', second_to_last.value);
} else {
    console.log('There was only one node in the list. There was NO second node')
}

// Test how secondToLast() works on a list with NO second node
second_to_last = my_short_list.secondToLast();
if (second_to_last) {
    console.log('second_to_last:', second_to_last.value);
} else {
    console.log('There was only one node in the list. There was NO second node')
}