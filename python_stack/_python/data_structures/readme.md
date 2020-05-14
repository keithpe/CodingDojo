## Singly Linked List

- Singly Linked Lists
- Objectives:
- Learn how linked lists work
- Learn more about pointers
- Learn how to traverse through a linked list

### Add methods to:

- Add a Value to the Front
- Traversing Through a List
- Traversing Through a List and Adding a Value to the End

### Additional Challenges

These are challenging! Hop up to a whiteboard, grab a cohort mate if available, and try to work through these together.

- remove_from_front(self) - remove the first node and return its value
- remove_from_back(self) - remove the last node and return its value
- remove_val(self, val) - remove the first node with the given value

Consider the following cases:
the node with the given value is the first node
the node with the given value is in the middle of the list
the node with the given value is the last node

- Insert_at(self, val, n) - insert a node with value val as the nth node in the list

Consider the following cases:
n is 0
n is the length of the list
n is between 0 and the length of the list

### Output from singly_linked_lists.py

```
******************* Origin List ***************************************

eric
keith
arlene
josh
bobby
loretta
sydney

**** remove from front ************************************************

Removing front node:eric
keith
arlene
josh
bobby
loretta
sydney

**** remove from back *************************************************

Removing back node:sydney
keith
arlene
josh
bobby
loretta

*** remove val(keith) First item in the list **************************

Removing first val item in the list:keith
arlene
josh
bobby
loretta

*** remove val(josh) **************************************************

Removing first val item in the list:josh
arlene
bobby
loretta

**** remove val(loretta) *** Last item in the list ********************

Removing first val item in the list:loretta
arlene
bobby

********** insert_at() ************************************************

Insert at 0
arlene
bobby
Insert at 3
Insert at 4
Insert at 100 (beyond end of list. Defaults to add_to_back()

***********************************************************************
```
