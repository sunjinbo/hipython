# 定义节点类
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# 定义二叉树
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            cursor = self.root
            while True:
                if cursor.key < node.key:
                    if cursor.left is None:
                        cursor.left = node
                        break
                    else:
                        cursor = cursor.left
                elif cursor.key > node.key:
                    if cursor.right is None:
                        cursor.right = node
                        break
                    else:
                        cursor = cursor.right
                else:
                    break

    def traverse(self, node: Node, key):
        if node is None:
            return False
        else:
            if node.key < key:
                return self.traverse(node.left, key)
            elif node.key > key:
                return self.traverse(node.right, key)
            else:
                return True

    def find(self, key):
        if self.root is None:
            return False
        else:
            return self.traverse(self.root, key)


# 测试代码
tree = BinaryTree()
tree.add(2)
tree.add(6)
tree.add(9)
tree.add(3)
tree.add(7)
tree.add(11)
print(tree.find(6))
print(tree.find(4))
print(tree.find(7))
