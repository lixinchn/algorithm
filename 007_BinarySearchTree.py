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

    def delete(self, key):
        self.root_node = self._delete(self.root_node, key)

    def get_min(self, root):
        min_node = root
        while root:
            if root.left:
                min_node = root.left
            root = root.left
        return min_node

    def delete_min(self, root):
        min_node = self.get_min(root)
        self._delete(root, min_node.key)

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

    def _delete(self, root, key):
        if not root:
            return None

        if root.key > key:
            root.left = self._delete(root.left, key)
        elif root.key < key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
                return None
            if not root.right:
                left = root.left
                root = None
                return left
            if not root.left:
                right = root.right
                root = None
                return right

            min_node = self.get_min(root)
            self.delete_min(root)
            min_node.left = root.left
            min_node.right = root.right
            return min_node
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

    bs.delete(50)