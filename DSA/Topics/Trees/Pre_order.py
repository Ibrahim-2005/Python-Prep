class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)

#          1
#      2      3
#    4   5      6
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)

a.left=(b)
a.right=(c)
b.left=(d)
b.right=(e)
c.right=(f)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
pre_order(a)