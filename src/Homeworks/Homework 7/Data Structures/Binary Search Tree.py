class NodeError(Exception):
    pass


class Node:
    def __init__(self, val):
        if not isinstance(val, int):
            raise NodeError
        self.__val = val
        self.__left = None
        self.__right = None

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        if not isinstance(val, int):
            raise NodeError
        self.__val = val

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if not isinstance(left, Node) and left is not None:
            raise NodeError
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if not isinstance(right, Node) and right is not None:
            raise NodeError
        self.__right = right


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        if not isinstance(root, Node) and root is not None:
            raise NodeError
        self.__root = root

    def search(self, val):
        if not self.__root:
            raise NodeError
        curr = self.__root
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            raise NodeError('No such node in the tree')
        return curr

    def insert(self, val):
        if not isinstance(val, int):
            raise NodeError
        if not self.__root:
            self.__root = Node(val)
            return None
        curr_p = None
        curr = self.__root
        while curr:
            if val < curr.val:
                curr_p = curr
                curr = curr.left
            elif val > curr.val:
                curr_p = curr
                curr = curr.right
            else:
                raise NodeError
        if val < curr_p.val:
            curr_p.left = Node(val)
        elif val > curr_p.val:
            curr_p.right = Node(val)

    def get_min(self, curr=None):
        if not curr:
            curr = self.root
        while curr.left:
            curr = curr.left
        return curr

    def get_max(self, curr=None):
        if not curr:
            curr = self.root
        while curr.right:
            curr = curr.right
        return curr

    def delete(self, val):
        if not isinstance(val, int):
            raise NodeError
        if not self.__root:
            raise NodeError
        curr_p = None
        curr = self.__root
        while curr and curr.val != val:
            if val < curr.val:
                curr_p = curr
                curr = curr.left
            else:
                curr_p = curr
                curr = curr.right
        if curr is None:
            raise NodeError('No such node in the tree')
        #   case 1, node is a leaf
        if not curr.right and not curr.left:
            if curr == curr_p.left:
                curr_p.left = None
            else:
                curr_p.right = None
        # case 2, node with one child
        elif not curr.right and curr.left:
            if curr == curr_p.left:
                curr_p.left = curr.left
            else:
                curr_p.right = curr.left
        elif not curr.left and curr.right:
            if curr == curr_p.left:
                curr_p.left = curr.right
            else:
                curr_p.right = curr.right
        # case 3, node with two children
        else:
            curr1 = curr.right
            while curr1.left:
                curr1 = curr1.left
            value1 = curr1.val
            self.delete(value1)
            curr.val = value1
        return curr

    def inorder(self, node):
        if not isinstance(node, Node) and node:
            raise NodeError
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)



#
# bst = BinarySearchTree()
# bst.insert(15)
# bst.insert(5)
# bst.insert(10)
# bst.insert(12)
# bst.insert(20)
# bst.insert(13)
# bst.insert(4)
# bst.inorder(bst.root)
# print("\nAfter")
# bst.delete(15)
# bst.inorder(bst.root)


t2 = BinarySearchTree()
t2.insert(10)
t2.insert(5)
t2.insert(2)
t2.insert(9)
t2.insert(30)
t2.insert(25)
t2.insert(40)
t2.insert(38)

t2.inorder(t2.root)
t2.delete(10)
print()
t2.inorder(t2.root)
print()
print(t2.get_max().val)
print(t2.get_min().val)
print(t2.search(25).val)

