class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sample = []
        element = head
        while element:
            sample.append(element)
            element = element.next
        
        last = sample.pop()
        max_element = last.val

        while sample:
            current = sample.pop()
            if current.val < max_element:
                continue
            else:
                max_element = current.val
                current.next = last
                last = current
        return last