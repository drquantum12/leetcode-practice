class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur_node=head
        prev_node=None
        next_node=None
        while cur_node:
            next_node=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
        return prev_node

# or
# class Solution:
#     def reverseList(self, head: ListNode | None) -> ListNode | None:
#         prev_node, cur_node=None, head
#         while cur_node:            
#             cur_node.next, prev_node, cur_node = prev_node, cur_node, cur_node.next
#         return prev_node