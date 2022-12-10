# Definition for singly-linked list.
class LinkedList(object):
    def __init__(self, nodes):
        self.head = None
        self.list = []

        [self.list.append(node) for node in nodes]


    def __repr__(self):
        node = self.ListNode()
        nodes = []

        while node:
            nodes.append(node.val)
            node = node.next

        nodes.append(None)
        
        return nodes

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.data

class Solution:
    def mergeTwoLists(self, list1: ListNode([1,2,4]), list2: ListNode([1,3,4])) -> ListNode:
        dummy = ListNode()
        tail = dummy
        

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2 
                list2 = list2.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy