class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        
        part_size = l // k
        extra = l % k
        
        result = []
        temp = head
        
        for i in range(k):
            if not temp:
                result.append(None) 
            else:
                result.append(temp)
                cr = part_size + 1 if extra > 0 else part_size
                extra -= 1
                
                for j in range(cr - 1):
                    temp = temp.next  
                next_node = temp.next
                temp.next = None  
                temp = next_node  
                
        return result