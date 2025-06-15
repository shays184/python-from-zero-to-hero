
class Node:
    def __init__(self, val):
        self.val: int = val
        self.next = None


class LinkedList:
    def __init__(self, head: Node):
        self.head: Node = head
    

    def append(self, new_node: Node): # cost: # O(n) - linear time complexity. n = number of nodes in the linked list 10, 500, 10000
        node = self.head # (n1)

        # to traverse the linked list, we need to find the last node
        while node.next is not None: # while not node.next:
            node = node.next

        node.next = new_node

    def __str__(self) -> str:
        ans = ""
        node = self.head 
        
        # to traverse the linked list, we need to find the last node
        while node.next is not None: # while not node.next:
            ans += str(node.val) + " -> "
            node = node.next

        ans += str(node.val) + " -> ||"
        return ans



ll = LinkedList(Node(1))
ll.append(Node(2))  # Append n2 to the linked list
ll.append(Node(15))  # Append n3 to the linked list
ll.append(Node(90))


print(ll)  # This will print the string representation of the LinkedList object
