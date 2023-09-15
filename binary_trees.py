
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

def inorder(node):
    if node is None:
        return
    
    # left, root, right
    inorder(node.left)
    print(node.val)
    inorder(node.right)

print('In order:')
inorder(root)


def left_children_sequence(node, sequence):
    if node.left:
        #continue here
        return
    

# Breadth-first traversal
# use a queue to determin order in which to travel the nodes: root, left child, right child
def breadth_first(node, q, result):
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)

    result.append(node.val)
    #print(node.val)
    if q:
        breadth_first(q.pop(0), q, result)


queue = []  # using list as a queue
result = []

print('Breadth first:')
breadth_first(root, queue, result)
print('result= ', result)

