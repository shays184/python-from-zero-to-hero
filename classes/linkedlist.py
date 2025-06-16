
class Node:
    def __init__(self, val):
        self.val: int = val
        self.next = None


class LinkedList:
    def __init__(self, head: Node | None):
        self.head: Node = head

        if self.head is not None:
            print("LinkedList created with head node value:", self.head.val)
            print("Current linked list:", self)
    

    def append(self, new_node: Node): # cost: # O(n) - linear time complexity. n = number of nodes in the linked list 10, 500, 10000
        print("Appending node with value:", new_node.val)
        if self.head is None:
            self.head = new_node 
            print("Node appended successfully.\n", self)
            return
        node = self.head # (n1)

        # to traverse the linked list, we need to find the last node
        while node.next is not None: # while not node.next:
            node = node.next

        node.next = new_node
        print("Node appended successfully.\n", self)

    def __str__(self) -> str:
        """Return a string representation of the linked list.
        The string representation is in the format: "val1 -> val2 -> ... -> valN -> ||"
        where val1, val2, ..., valN are the values of the nodes in the linked list.
        """
        ans = ""
        node = self.head 
        
        # to traverse the linked list, we need to find the last node
        while node.next is not None: # while not node.next:
            ans += str(node.val) + " -> "
            node = node.next

        ans += str(node.val) + " -> ||"
        return ans

    def remove_by_value(self, value: int): # cost: O(n) - linear time complexity. n = number of nodes in the linked list 
        """
        Remove the *first* node with the given value from the linked list."""

        current = self.head
        next_node = current.next

        # If the head node is the one to be removed
        if current.val == value:
            del current
            self.head = next_node
            print(f"Removed head node with value: {value}")
            print("Updated linked list:", self)
            return
        
        # if the value is not in the head node, we need to traverse the linked list
        while next_node is not None:
            if next_node.val == value:
                temp = next_node.next  # Save the next node
                del next_node  # Delete the node with the value
                current.next = temp  # Link the previous node to the next node
                print(f"Removed node with value: {value}")
                print("Updated linked list:", self)
                return
            current = current.next
            next_node = current.next
        print(f"Value {value} not found in the linked list.")



ll = LinkedList(Node(1))
ll.append(Node(2))  # Append n2 to the linked list
ll.append(Node(15))  # Append n3 to the linked list
ll.append(Node(90))
ll.append(Node(100))  # Append n4 to the linked list
ll.remove_by_value(2)
ll.remove_by_value(1)