from graphviz import Digraph


class Graph(object):
    def __init__(self):
        self.dot = Digraph("G", comment="btree", )
        self.dot.node_attr['shape'] = "record"

    def GraphNode(self, node, idx):
        # label="<f0> left|<f1> mid\ dle|<f2> right"]
        label = ""
        i = 0
        while i < (2 * node.n):
            tag_c = "<f" + str(i) + ">"
            tag_k = "<f" + str(i + 1) + ">"
            label = label + tag_c + " |" + tag_k + " " + str(node.key[i / 2]) + "|"
            i = i + 2
        label = label + "<f" + str(i) + ">" + " "
        self.dot.node(str(idx), label)

        for i in range(0, node.n + 1):
            if node.isLeaf == False:
                self.GraphNode(node.child[i], idx * 10 + i)

    def EdgeNode(self, node, idx):
        if node.isLeaf is False:
            for i in range(0, node.n + 1):
                tag_c1 = "<f" + str(2 * i) + ">"
                tag_c2 = "<f" + str(node.child[i].n) + ">"
                self.dot.edge(str(idx) + ":" + tag_c1, str(idx * 10 + i) + ":" + tag_c2)
                self.EdgeNode(node.child[i], idx * 10 + i)

    def GraphTree(self, tree):
        self.GraphNode(tree.root, 1)
        self.EdgeNode(tree.root, 1)
        return

    def View(self):
        print (self.dot.source)
        self.dot.view()

    def Render(self):
        self.dot.render('test-output/btree.dot', view=False)
