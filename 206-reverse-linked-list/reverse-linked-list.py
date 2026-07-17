class Solution(object):
    def reverseList(self, head):

        prev = None          # Previous node (starts before the list)
        curr = head          # Start from the first node

        while curr:          # Process until we reach the end

            next_node = curr.next   # Save the next node

            curr.next = prev        # Reverse the pointer

            prev = curr             # Move prev forward

            curr = next_node        # Move curr forward

        return prev                 # New head of the reversed list