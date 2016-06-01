import random


class Node():
    key = 0
    value = None
    left, right = None, None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class BinarySearchTree():
    root_node = None

    def __init__(self):
        pass

    def put(self, key, value):
        self.root_node = self._put(self.root_node, key, value)

    def get(self, key):
        temp = self.root_node
        while temp:
            if temp.key > key:
                temp = temp.left
            elif temp.key < key:
                temp = temp.right
            else:
                return temp.value
        return None

    def _put(self, root, key, value):
        if not root:
            node = Node(key, value)
            root = node
            return root

        if root.key > key:
            root.left = self._put(root.left, key, value)
        elif root.key < key:
            root.right = self._put(root.right, key, value)
        else:
            root.value = value
        return root


if __name__ == '__main__':
    bs = BinarySearchTree()
    bs.put(50, 0)
    bs.put(25, 0)
    bs.put(75, 0)
    bs.put(65, 0)
    bs.put(36, 0)

    print bs.get(36)
    print bs.get(33)