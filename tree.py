# question http://www.ardendertat.com/2011/12/05/programming-interview-questions-20-tree-level-order-print/

# import collections
#
# class Node:
#     def __init__(self, val=None):
#         self.left, self.right, self.val = None, None, val
#
#
# def levelOrderPrint(tree):
#     if not tree:
#         return
#     nodes=collections.deque([tree])
#     currentCount, nextCount = 1, 0
#     while len(nodes)!=0:
#         currentNode=nodes.popleft()
#         currentCount-=1
#         print currentNode.val,
#         if currentNode.left:
#             nodes.append(currentNode.left)
#             nextCount+=1
#         if currentNode.right:
#             nodes.append(currentNode.right)
#             nextCount+=1
#         if currentCount==0:
#             #finished printing current level
#             currentCount, nextCount = nextCount, currentCount
#             print '\n',
#
# # Driver Program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
#
# print "Level Order Traversal of binary tree is -"
# levelOrderPrint(root)


# --------------------------------------------------------
# considering to use collection.deque which has better
# memory and time than list when working with no fixed
# length
# use an extra for loop inside while and without keeping
# two explicit counters

import collections

class Tree():
    def __init__(self, val=None):
        self._l = None
        self._r = None
        self._val = val

def printlevel(root):
    if not root:
        return
    stack0 = collections.deque([root])
    while stack0:
        stack1 = collections.deque([])
        for r in stack0:
            print r._val,
            if r._l:
                stack1.append(r._l)
            if r._r:
                stack1.append(r._r)
        print
        stack0 = stack1


root = Tree(1)
root._l = Tree(2)
root._r = Tree(3)
root._l._l = Tree(4)
root._l._r = Tree(5)
root._r._l = Tree(6)
root._r._r = Tree(7)
root._l._l._l = Tree(8)
root._r._l._l = Tree(12)

printlevel(root)