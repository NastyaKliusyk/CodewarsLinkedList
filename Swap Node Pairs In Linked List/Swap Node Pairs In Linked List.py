class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    dummy = Node()
    dummy.next = head

    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        first.next = second.next
        second.next = first
        current.next = second

        current = first

    return dummy.next
