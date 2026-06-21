from collections import deque

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head == None:
        return None

    curr = head
    count = 1
    queue = deque(maxlen=n + 1)

    queue.append(head)

    while curr.next != None:
        curr = curr.next
        count += 1
        queue.append(curr)

    if count == n:
        return head.next
    elif len(queue) > 1:
        queue[0].next = queue[1].next
        
    return head