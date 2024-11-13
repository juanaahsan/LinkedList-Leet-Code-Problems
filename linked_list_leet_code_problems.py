# Merge Two linked Lists
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Manually create list1 = [1, 2, 4]
# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)

# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    values = []
    while node:
        values.append(node.val)
        node = node.next
    # print(" -> ".join(map(str, values)))

solution = Solution()
# merged_list = solution.mergeTwoLists(list1, list2)


# print("Merged List:")
# print_linked_list(merged_list)


# remove duplicates


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)



class Solution(object):
    def deleteDuplicates(self, head):
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next


        return head
        


## palindrome


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev  
        while right:  
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
