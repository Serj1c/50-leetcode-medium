class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(None)
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        carry, d = divmod(d1 + d2 + carry, 10)
        cur.next = ListNode(d)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next
