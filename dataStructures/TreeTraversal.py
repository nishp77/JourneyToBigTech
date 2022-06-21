class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    

# recursive preorder
def Rpreorder(root):
    if root is not None:
        print(root.value)
        Rpreorder(root.left)
        Rpreorder(root.right)

# iterative preorder
def Ipreorder(root):
    list = []
    list.append(root)

    while(len(list) > 0):
        node = list.pop()
        print(node.value)

        if(node.right is not None):
            list.append(node.right)
        
        if(node.left is not None):
            list.append(node.left)


# recursive inorder
def Rinorder(root):
    if root is not None:
        Rinorder(root.left)
        print(root.value)
        Rinorder(root.right)


# iterative inorder
def Iinorder(root):
    # list = []
    # done = False
    # curr = root

    # while done is not True:
    #     if curr is not None:
    #         list.append(curr)
    #         curr = curr.left
    #     else:
    #         if len(list) == 0:
    #             done = True
    #         else:
    #             curr = list.pop()
    #             print(curr.value)
    #             curr = curr.right

    list = []
    list.append(root)

    while(len(list)> 0):
        curr = list.pop()

        if curr.left is not None:
            list.append(curr.left)
            curr = curr.left
        
        print(curr.value)

        if curr.right is not None:
            list.append(curr.right)
            curr = curr.right


# recursive postorder
def Rpostorder(root):
    if root is not None:
        Rpostorder(root.left)
        Rpostorder(root.right)
        print(root.value)


# iterative postorder

def Ipostorder(root):
    list = []
    r = []
    list.append(root)
    while (len(list)>0):
        curr = list.pop()
        r.append(curr.value)

        if curr.left is not None:
            list.append(curr.left)
        if curr.right is not None:
            list.append(curr.right)

    while r:
        print(r.pop())

    s={}
    del s['a']


if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    Rpostorder(root)

