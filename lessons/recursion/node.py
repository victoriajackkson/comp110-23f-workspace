"""Node Class."""

from __future__ import annotations
__author__ = "730400711"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return data attribute for first element in linked list."""
        return self.data

    def tail(self) -> Node| None: 
        """Returns linked list of every element minus the head."""
        if self.next is None:
            return None
        else:
            return self.next

    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data

# node_c: Node = Node(2, None) #base case
# node_b: Node = Node(1, node_c)
# node_a: Node = Node(0, node_b) #head of list

# print(node_a.next.next.data)
# print(node_a.next.next.next)