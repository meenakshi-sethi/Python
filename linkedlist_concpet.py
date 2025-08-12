# Linked List

"""
What is a Linked List?
    A linked list is a linear data structure where elements (called nodes) are connected using pointers/references instead of 
    being stored in contiguous memory like arrays (think of theater seats for contiguous array).

Structure of a Linked List Node
    Each Node has:
    1. data - the actual value sorted (integer, string, object, etc.)
    2. next - a reference (or pointer) to the next node in the sequence

Eg - singly linked list:
[10 | next] -> [20 | next] -> [30 | next] -> None

    Each [data | next] is a node.
    the `next` pointer of the last node is None (end of list).

Types of Linked Lists
1. Singly Linked List --> Each node points to the next node only. (Forward travelling only)
    eg: 10 -> 20 -> 30

2. Doubly Linked List --> Each node points to both previous and next node. (forward and backward travelling)
    eg [prev | data | next]
    None <- 10 <-> 20 <-> 30 -> None

3. Circular Linked List --> The last node points back to the head
    eg  10 -> 20 -> 30 -
         |_____________|

Primitive vs Non-Primitive Data structures 

Primitive data structure are built into the language. eg 
int, float, bool, str, list, tuple, dict, set 

Non Primitive data structures:
    - We have to define them ourself (node + structure logic) unless language gives them as part of the library. 
    - Built using primitive data structures. 
    - Eg Linked List, stack, Queue, Tree, Graph

Python doesn't have linked list built in
- Python list (`list`) are dynamic arrays under the hood - they already handle most list-like needs efficiently.
- Linked Lists are more common in languages like C/C++ where we manage memory manually.
- In python, we simulate a linked list by creating:
    - A node class -> stores `data` and `next`
    - LinkedList class -> store `head` and methods like `append()`, `insert()`, `delete()`

"""


# Singly Linked List - Add & Delete Example

# node class: represents a sinlge element in the linked list
class Node:
    def __init__(self, data):
        self.data = data # value stored in node
        self.next = None # pointer/reference to next node

# Linked List class
class SinlglyLinkedList:
    def __init__(self):
        self.head = None # start of the list

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)

        if not self.head: # if list is empty
            self.head = new_node
            return
        
        current = self.head
        while current.next: # move to the last node
            current = current.next
        current.next = new_node # attach new node at the end

    # Delete a node by value



    # display the linked list    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next 
        print("None")  




# ===== Walkthrough======

lnklst = SinlglyLinkedList()

# start: []
lnklst.display() # None

# append
lnklst.append(10)
lnklst.append(20)
lnklst.append(30)
lnklst.append(40)
lnklst.display() # Output: 10 -> 20 -> 30 -> 40 -> None


