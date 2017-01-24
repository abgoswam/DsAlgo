3 -> 1 -> 6 -> 7 -> 4
n = 2
remove nth node from the end of the list


 // Sol 1
 // L <- length of list L = 5
 // nth node from end will be the (L-n + 1)th node from the beginning (L-n + 1) = 4th 
 
 // Sol 2
 // prev <- before p1
 // p1 <- poins to start of list
 // p2 <- p1 + (n) nodes ahead // Verify p2 is valid
 // once P2 reaches end, p1 will be the nth node from the end. use 'prev' to remove this node
 
 Class Node:
     def __init__(self, x):
         self.val = x
         self.next = none
         
 def removenth(head, n):
     if (head is None) or (n <= 0):
         return None
         
     prev = None
     p1 = head
     p2 = head
     
     for i in range(n):
         p2 = p2.next
         if (p2 is None) and (i < n-1):
             return None  
             
     while p2 is not None:
         prev = p1
         p1 = p1.next
         p2 = p2.next
         
     if prev is None:
         head = head.next
     else:    
         prev.next = p1.next
         
     return head
     
3 -> 1 -> 6 -> 7 -> 4 -> none
n = 2          

1) n = 8
2) head = None , n <= 0
3) n = 5
4) n = 2

