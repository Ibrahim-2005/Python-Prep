from collections import deque
from In_order import in_order

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)
def build_tree(list):
    if not list or list[0] is None:
        return
    root=Node(list[0])
    queue=deque([root])
    i=1
    while i < len(list):
        current=queue.popleft()
        if i < len(list) and list[i] is not None:
            current.left=Node(list[i])
            queue.append(current.left)
        i+=1

        if i < len(list) and list[i] is not None:
            current.right=Node(list[i])
            queue.append(current.right)
        i+=1
    return root
list=[4,2,7,1,3,6,9]
tree=build_tree(list)
in_order(tree)
