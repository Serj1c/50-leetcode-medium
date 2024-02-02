class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(None)
    dummy.next = head
    cur = head
    prev = dummy

    while cur and cur.next:
        nxt = cur.next
        prev.next = nxt
        cur.next = nxt.next
        nxt.next = cur

        prev = cur
        cur = cur.next

    return dummy.next