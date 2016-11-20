class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)
    return root


def search(root, data):
    if root is None:
        return False
    else:
        if data == root.data:
            return True
        elif data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)


def findMin(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, data):
    if root is None:
        return root
    else:
        if data < root.data:
            root.left = delete(root.left, data)
        elif data > root.data:
            root.right = delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print root.data
    inOrder(root.right)


def preOrder(root):
    if not root:
        return
    print root.data
    preOrder(root.left)
    preOrder(root.right)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print 'Inorder traversal of the given tree'
inOrder(root)

print '\nDelete 20'
root = delete(root, 20)
print 'Inorder traversal of the modified tree'
inOrder(root)

print '\nDelete 30'
root = delete(root, 30)
print 'Inorder traversal of the modified tree'
inOrder(root)

print '\nDelete 50'
root = delete(root, 50)
print 'Inorder traversal of the modified tree'
inOrder(root)
