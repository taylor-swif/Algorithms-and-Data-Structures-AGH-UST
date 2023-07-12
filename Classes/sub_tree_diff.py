class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.w = 0
    
    def add_edge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)

def f(node: Node):
    if len(node.edges) == 0:
        return 0
    
    for i in range(len(node.edges)):
        node.w += f(node.edges[i]) + node.weights[i]
    return node.w



def balance(root: Node):
    f(root)

    min_diff = float('inf')
    min_idx = 69
    def g(node: Node):
        nonlocal min_diff, min_idx
        
        for i in range(len(node.edges)):
            child = node.edges[i]
            upper_tree_val = node.w - child.w - node.weights[i]
            lower_tree_val = child.w
            if abs(upper_tree_val - lower_tree_val) < min_diff:
                min_diff = upper_tree_val - lower_tree_val
                min_idx = node.ids[i]

            g(child)

    g(root)

    return min_diff, min_idx


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()

A.add_edge(B, 6, 1)
A.add_edge(C, 10, 2)
B.add_edge(D, 5, 3)
B.add_edge(E, 4, 4)

print(balance(A))
