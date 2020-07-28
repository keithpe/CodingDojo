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
    //****************************************************************************
    secondToLast() {
        console.log('\n**** Second To Last ****')
        let runner = this.head;
        let runner2 = runner;
        while (runner.next) {
            runner2 = runner
            runner = runner.next;
        }
        return runner2;
    }

}

// Create a new list instance, and add some nodes.
my_list = new SLL('Keith').addFront('Eric').addFront('Arlene').addFront('Sydney');

// Show all nodes in the list
my_list.show_all();

let second_to_last = my_list.secondToLast();
console.log('second_to_last:', second_to_last.value);