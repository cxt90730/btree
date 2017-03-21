# coding=utf-8
import graph

MAX_CHILD_NUM = 4 # Max num of child , if beyond it, that node need to split

t = (MAX_CHILD_NUM >> 1) - 1  # Mid Idx

class BPlusTreeNode(object):
    def __init__(self):
        self.isRoot = False
        self.isLeaf = False
        self.n = 0 # num of key
        self.key = []
        self.child = []
        self.last = None
        self.next = None
        self.p = None # parent

class BPlusTree(object):
    def __init__(self):
        self.root = BPlusTreeNode()
        self.root.isRoot = True
        self.root.isLeaf = True

    def allocateNode(self):
        return BPlusTreeNode()

    def split(self, x, i): # x is current node, i is child index on x
        z = self.allocateNode() # Temp Node

        y = x.child[i]
        z.isLeaf = y.isLeaf
        z.n = t

        for j in range(0, t): # copy keys from y
            z.key.append(y.key[j + t + 1])

        if y.isLeaf is False: # copy childs from y
            for j in range(0, t + 1 ):
                z.child.append(y.child[j + t + 1])
        y.n = t

        for j in range(x.n, i)[::-1]:  # resort child of x node
            if j == x.n:
                x.child.append(x.child[j])
            else:
                x.child[j + 1] = x.child[j]

        if x.child.__len__() == i + 1: # new node
            x.child.append(z)
        else:
            x.child[i + 1] = z

        for j in range(x.n - 1, i - 1)[::-1]:  # resort key of x node
            if j == x.n - 1:
                x.key.append(x.key[j])
            else:
                x.key[j + 1] = x.key[j]

        if x.key.__len__() == i:  # new node
            x.key.append(y.key[t])
        else:
            x.key[i] = y.key[t]
        x.n = x.n + 1

    def insert(self, k):
        r = self.root
        if r.n == (2 * t + 1):
            s = self.allocateNode()
            self.root = s
            s.isLeaf = False
            s.n = 0
            s.child.append(r)
            self.split(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(r, k)

    def insert_non_full(self, x, k):
        i = x.n - 1
        if x.isLeaf is True:            # x is leaf
            while i >= 0 and k < x.key[i]:
                if i == x.n - 1:
                    x.key.append(x.key[i])
                else:
                    x.key[i + 1] = x.key[i]
                i = i - 1
            if i == x.n - 1:
                x.key.append(k)
            else:
                x.key[i + 1] = k
            x.n = x.n + 1
        else:
            while i >= 0 and k < x.key[i]:
                i = i - 1
            i = i + 1
            if x.child[i].n == (2 * t + 1):
                self.split(x, i)
                if k > x.key[i]: # k > key[i] , right child of key[i]
                    i = i + 1
            self.insert_non_full(x.child[i], k)





if __name__ == '__main__':
    tree = BPlusTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.insert(12)
    tree.insert(13)
    tree.insert(14)
    tree.insert(15)
    # tree.insert(16)
    # tree.insert(11)



    g = graph.Graph()
    g.GraphTree(tree)
    g.View()














