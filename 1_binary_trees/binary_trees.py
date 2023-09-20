
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    # insert item into tree
    def insert(self, root, item):
        if root == None:
            root = Node(item)
        if item < root.data:
            self.insert(root.left, item)
        else:
            self.insert(root.right, item)
        return root
    
    # create a tree from a list
    def list_to_tree(self, list):
        return self.list_to_tree_helper(None, list)

    def __list_to_tree_helper(self, root, list):
        for item in list:
            Node.insert(root, item)

        return root

#
# 09.14.2023 - Binary tree traversal
# 
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



#
# 09.19.2023 - Binary tree operations
# 

nums = [1,2,3,4,5,6,7]
#root1 = list_to_tree(list=nums)


q = []  # using list as a queue
result = []

print('List to tree:')
#breadth_first(root1, q, result)



root2 = Node(1)
root2.left = Node(3)
root2.right = Node(7)
root2.left.left = Node(4)
root2.left.right = Node(2)
root2.right.left = Node(1)
root2.left.left.left = Node(7)

def print_tree_traversal_level(root, level=0, q = []):
    # base case
    if root == None:
        return
    
    print(root.val, level)

    # insert children into queue
    if root.left != None:
        q.append([root.left, level+1])
    if root.right != None:
        q.append([root.right, level+1])

    if len(q) > 0:
        next_node = q.pop(0)
        print_tree_traversal_level(next_node[0], next_node[1], q)
    else:
        return
    
que = []
print_tree_traversal_level(root2, 0, que)
