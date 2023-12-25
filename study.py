# c = ['ccc', 'aaaa', 'd', 'bb']
# sorted(c)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# 다중 할당과 여러줄 할당 과의 차이점

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3


rev = n1
slow = n2

# rev = 1, slow = 2, slow.next =3
# => rev = 2, rev.next = 1, slow = 3
rev, rev.next, slow = slow, rev, slow.next

# rev = 1, slow = 2
# rev = slow, slow.next = rev => rev = 2, slow.next = 1
# rev, rev.next = slow, rev
# slow = slow.next

print(rev.val, slow.val)