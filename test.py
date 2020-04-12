class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree(object):
    def __init__(self):
        self.len = 0
    # Вставка
    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)

        return root


    # Поиск
    def get(self,root,val):
       if root:
           res = self._get(val,root)
           if res:
                  return 'Element is in list'
           else:
                  return 'Element is not in list'
       else:
           return 'Tree is empty'

    # Поиск
    def _get(self,val,root):
       if not root:
           return False
       elif root.val == val:
           return root
       elif val < root.val:
           return self._get(val,root.l_child)
       else:
           return self._get(val, root.r_child)


    def size(self, root):
        if root:
            self.size(root.l_child)
            self.size(root.r_child)
            self.len += 1
        return self.len

    def delete(self,val,root):
        if self.len > 1:
            nodeToRemove = self._get(val,root)
            if nodeToRemove:
                #self.remove(nodeToRemove)
                self.len -= 1
                print('Hello')
            else:
                raise KeyError('Error, key not in tree')
        elif self.len == 1 and root.val == val:
            root = None
            self.len -= 1
        else:
            raise KeyError('Error, key not in tree')









    def in_order_place(self, root):
        if not root:
            return False
        else:
            self.in_order_place(root.l_child)
            print(root.val)
            self.in_order_place(root.r_child)

    def pre_order_place(self, root):
        if root:
            print(root.val)
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order_place(self, root):
        if not root:
            return False
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val)






r = Node(3) #  Создание дерева с корнем 3
node = BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]

for nd in nodeList:
    node.insert(r, Node(nd))


# print("------In order ---------")
# print(node.in_order_place(r))
# print("------Pre order ---------")
# print(node.pre_order_place(r))
# print("------Post order ---------")
# print(node.post_order_place(r))

print(node.size(r))
#print(node.delete(1, r))
print(node.get(r, 10))
print()
