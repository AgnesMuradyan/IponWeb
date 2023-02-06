class NodeError(Exception):
    pass


class Node:
    def __init__(self, val):
        self.__val = val
        self.__color = "red"
        self.__parent = None
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
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color not in ["black", "red"]:
            raise NodeError
        self.__color = color

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        if not isinstance(parent, Node) and parent is not None:
            raise NodeError
        self.__parent = parent

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


class RedBlackTree:
    def __init__(self):
        self.__Nil = Node(None)
        self.__Nil.color = 'black'
        self.__Nil.left = None
        self.__Nil.right = None
        self.__root = self.Nil

    @property
    def Nil(self):
        return self.__Nil

    @Nil.setter
    def Nil(self, nil):
        if not isinstance(nil, Node):
            raise NodeError
        self.__Nil = nil

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        if not isinstance(root, Node) and root is not None:
            raise NodeError
        self.__root = root

    def inorder(self, node):
        if type(node) != Node and node is not None:
            raise NodeError
        if node and node != self.Nil:
            self.inorder(node.left)
            print(f"[{node.val} -> {node.color}]")
            self.inorder(node.right)

    def search(self, val):
        if not isinstance(val, int):
            raise NodeError
        if not self.root:
            raise Node
        curr = self.root
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None or curr == self.Nil:
            raise NodeError
        return curr

    def rotate_left(self, x):
        if not isinstance(x, Node):
            raise NodeError
        y = x.right
        x.right = y.left
        if y.left != self.Nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.Nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        if not isinstance(x, Node):
            raise NodeError
        y = x.left
        x.left = y.right
        if y.right != self.Nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.Nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fix(self, new_node):
        while new_node.parent.color == "red":
            if new_node.parent == new_node.parent.parent.left:
                y = new_node.parent.parent.right
                if y.color == "red":
                    y.color = "black"
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.rotate_right(new_node.parent.parent)
            else:
                y = new_node.parent.parent.left
                if y.color == "red":
                    y.color = "black"
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.rotate_left(new_node.parent.parent)
        self.root.color = "black"

    def insert(self, val):
        if not isinstance(val, int):
            raise NodeError
        new_node = Node(val)
        y = self.Nil
        x = self.root
        while x != self.Nil:
            y = x
            if x.val > new_node.val:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == self.Nil:
            self.root = new_node
        elif y.val > val:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.Nil
        new_node.right = self.Nil
        new_node.color = "red"
        self.insert_fix(new_node)

    def transplant(self, u, v):
        if (not isinstance(u, Node) and u is not None) or (not isinstance(v, Node) and v is not None):
            raise NodeError
        if not u.parent or u.parent == self.Nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fix(self, new_node):
        while new_node != self.root and new_node.color == "black":
            if new_node == new_node.parent.left:
                x = new_node.parent.right
                if x.color == "red":
                    x.color = "black"
                    new_node.parent.color = "red"
                    self.rotate_left(new_node.parent)
                    x = new_node.parent.right
                if x.left.color == "black" and x.right.color == "black":
                    x.color = "red"
                    new_node = new_node.parent
                else:
                    if x.right.color == "black":
                        x.left.color = "black"
                        x.color = "red"
                        self.rotate_left(x)
                        x = new_node.parent.right
                    x.color = new_node.parent.color
                    new_node.parent.color = "black"
                    x.right.color = "black"
                    self.rotate_left(new_node.parent)
                    new_node = self.root
            else:
                x = new_node.parent.left
                if x.color == "red":
                    x.color = "black"
                    new_node.parent.color = "red"
                    self.rotate_right(new_node.parent)
                    x = new_node.parent.left
                if x.right.color == "black" and x.left.color == "black":
                    x.color = "red"
                    new_node = new_node.parent
                else:
                    if x.left.color == "black":
                        x.right.color = "black"
                        x.color = "red"
                        self.rotate_left(x)
                        x = new_node.parent.left
                    x.color = new_node.parent.color
                    new_node.parent.color = "black"
                    x.left.color = "black"
                    self.rotate_right(new_node.parent)
                    new_node = self.root
        new_node.color = "black"

    def delete(self, val):
        if not isinstance(val, int):
            raise NodeError
        old_node = self.search(val)
        y = old_node
        y_color = y.color
        if old_node.left == self.Nil:
            x = old_node.right
            self.transplant(old_node, old_node.right)
        elif old_node.right == self.Nil:
            x = old_node.left
            self.transplant(old_node, old_node.left)
        else:
            y = old_node.right
            while y and y.left != self.Nil:
                y = y.left
            y_color = y.color
            x = y.right
            if y.parent == old_node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = old_node.right
                y.right.parent = y
            self.transplant(old_node, y)
            y.left = old_node.left
            y.left.parent = y
            y.color = old_node.color
        if y_color == "black":
            self.delete_fix(x)




t1 = RedBlackTree()
t1.insert(8)
t1.insert(5)
t1.insert(17)
t1.insert(15)
t1.insert(18)
t1.insert(25)
t1.inorder(t1.root)
t1.insert(40)
print("******************************************")
t1.inorder(t1.root)
t1.insert(80)
print("******************************************")
t1.inorder(t1.root)




t2 = RedBlackTree()
t2.insert(10)
t2.insert(5)
t2.insert(2)
t2.insert(9)
t2.insert(30)
t2.insert(25)
t2.insert(40)
t2.insert(38)

t2.inorder(t2.root)
t2.delete(30)
print("*********************************")
t2.inorder(t2.root)
