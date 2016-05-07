class Node:

    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def preorder(self):
        if self:
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
        print(str(self.value));

    def postorder(self):
        print('value', str(self.value));
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()

    def inorder(self):

        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.value));
            if self.right_child:
                self.right_child.inorder()


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print('#preorder')
        self.root.preorder()

    def postorder(self):
        print('#postorder')
        self.root.postorder()

    def inorder(self):
        print('#inorder')
        self.root.inorder()


def main():
    user_input = [53, 25, 6, 9, 28, 58, 7, 78, 15, 109, 66]
    my_tree = Tree();
    count = 0
    while count < len(user_input):
        my_tree.insert(user_input[count])
        count += 1

    my_tree.preorder()
    my_tree.postorder()
    my_tree.inorder()
    print(my_tree.find(109))

main()
