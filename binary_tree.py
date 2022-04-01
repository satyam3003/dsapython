# ToDo: CRUD way of making a db for a company. O(N) complexity

# class User:
#     def __init__(self, username, name, email):
#         self.username = username
#         self.name = name
#         self.email = email
#
#     def __repr__(self):
#         return "User(username='{}', name='{}', email='{}') \n".format(self.username, self.name, self.email)
#
#
# aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
# biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
#
# name_list = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
#
# class Database:
#     def __init__(self):
#         self.users = []
#
#     def insert(self, user):
#         i = 0
#         while i < len(self.users):
#             if self.users[i].username > user.username:
#                 break
#             i += 1
#         self.users.insert(i, user)
#
#     def find(self, username):
#         for user in self.users:
#             if user.username == username:
#                 return user
#
#     def edit(self, user):
#         target = self.find(user.username)
#         target.name = user.name
#         target.email = user.email
#
#     def list_all(self):
#         return self.users
#
#
# datab = Database()
#
# for add_user in name_list:
#     datab.insert(add_user)
#
#
# print(datab.list_all())


# ToDo: CRUD way is not effecient when it comes to finding something from a db consisting million entries. It mingt take up a long time
''' To overcome this we use binary tree which is of complexity O(logN)
In this topmost element is called as root and other connections are called as branches. lowermost with no nodes are called leaves. '''


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode(self.key = {self.key}, self.left = {self.left}, self.right = {self.right})"


three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
# print(f"{three}\n{four}\n{five}")

three.left = four
three.right = five
# print(three.left.key)
# print(three.right.key)

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parsetree(data):
    if isinstance(data, tuple) and len(data) == 3:  # when there are branches to left and right of a tree
        node = TreeNode(data[1])
        node.left = parsetree(data[0])
        node.right = parsetree(data[2])
    elif data == None:  # when None is a branch given in tree then none becomes node <-leaf
        node = None
    else:
        node = TreeNode(data)  #
    return node


tree = parsetree(tree_tuple)


def showtree2(node):
    if node == None:
        return None
    else:
        if node.left == None and node.right == None:
            return node.key
        else:
            return showtree2(node.left), node.key, showtree2(node.right)


# print(showtree2(tree))

# TODO: Traversing a binary tree
"""To traverse a binary tree we have 2 ways inorder and Preorder"""


def traversig_inorder(node):
    if node == None:
        return []
    else:
        return traversig_inorder(node.left) + [node.key] + traversig_inorder(node.right)


# print(traversig_inorder(tree))


def traversing_preorder(node):
    if node == None:
        return []
    else:
        return [node.key] + traversing_preorder(node.left) + traversing_preorder(node.right)


# print(traversing_preorder(tree))


# TODO: Max height of Binary tree

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


# print(tree_height(tree))


# TODO: Binary Search Tree = the tree in which left side and right side is balenced i.e. differenche in height is not greater than 1 is called balanced tree


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key


def is_balanced(node):
    if node is None:
        return True, 0

    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)

    height = 1 + max(height_l, height_r)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    return balanced, height


print(is_bst(tree))  # because no 3 is repeated its not bst
print(is_balanced(tree))  # but, it is balanced as the different is height is not greater than 1


# Creating a BST

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"BSTNode(key='{self.key}', left={self.left}, right={self.right}) "


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}') \n".format(self.username, self.name, self.email)


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

print(tree)

print(is_bst(tree))
print(is_balanced(tree))


# TODO: display BST

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


print(list_all(tree))  # this gives a list of all nodes in BST tree


# TODO how to make a BST from given a list of nodes


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, hi=mid - 1, parent=root)
    root.right = make_balanced_bst(data, lo=mid+1, hi=hi, parent=root)

    return root
