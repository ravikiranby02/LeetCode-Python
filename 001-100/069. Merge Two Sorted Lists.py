class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = []
        current = list1

        while current:
            value1.append(current.val)
            current = current.next

        value2 = []
        current = list2

        while current:
            value2.append(current.val)
            current = current.next


        for j in value2:
            value1.append(j)

        value1.sort()
        dummy = ListNode(0)
        current = dummy

        for v in value1:
            current.next = ListNode(v)
            current = current.next

        return dummy.next