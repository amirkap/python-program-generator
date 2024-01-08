class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def mergeTwoLists(list1, list2):
    # Check if either list is empty
    if not list1:
        return list2
    elif not list2:
        return list1
    
    # Initialize dummy node
    dummy = ListNode(0)
    # Initialize current pointer to the dummy node
    current = dummy
    
    # Traverse both lists and compare the values of the nodes
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append any remaining nodes from list1 or list2
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    # Return the head of the merged list
    return dummy.next


# Test cases
def test_mergeTwoLists():
    # Test case 1
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    result = mergeTwoLists(list1, list2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [1, 1, 2, 3, 4, 4]
    
    # Test case 2
    list1 = None
    list2 = None
    
    result = mergeTwoLists(list1, list2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == []
    
    # Test case 3
    list1 = None
    list2 = ListNode(0)
    
    result = mergeTwoLists(list1, list2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [0]
    
    # Test case 4
    list1 = ListNode(1)
    list2 = None
    
    result = mergeTwoLists(list1, list2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [1]
    
    # Test case 5
    list1 = ListNode(1)
    list2 = ListNode(2)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    result = mergeTwoLists(list1, list2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [1, 2, 3, 4]

test_mergeTwoLists()