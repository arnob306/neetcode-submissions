class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        current1 = list1
        current2 = list2
        while current1 != None and current2 != None:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            elif current1.val >= current2.val:
                current.next = current2
                current2 = current2.next 
            current = current.next 

        if current1:
            current.next = current1
        elif current2:
            current.next = current2

        return dummy.next