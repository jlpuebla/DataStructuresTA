
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

def inorder(node, values):
    if node is None:
        return
    
    # left, root, right
    inorder(node.left, values)
    values.append(node.val)
    inorder(node.right, values)

values = []
inorder(root, values)
print("In Order = ", values)


def left_children_sequence(node, sequence):
    if node is None:
        return
    
    if node.left:
        sequence.append(1)
    else:
        sequence.append(0)
    
    # left, root, right
    left_children_sequence(node.left, sequence)
    left_children_sequence(node.right, sequence)

sequence = []
left_children_sequence(root, sequence)
print('sequence = ', sequence)

    

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

breadth_first(root, queue, result)
print('Breadth first = ', result)

