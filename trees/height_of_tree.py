# height or depth of a N array tree

class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.child = []

def new_node(key):
    return Node(key)        



def depth_of_tree(node:Node):
    if node is None:
        return 0
    max_depth = 0
    for child in node.child:
        max_depth = max(max_depth, depth_of_tree(child))

    return max_depth +1




if __name__ == "__main__":
    root = Node("A")
    root.child.extend([new_node("B"),new_node("C")])
    root.child[0].child.extend([new_node("D"),new_node("E")])
    root.child[1].child.extend([new_node("F")])
    root.child[1].child[0].child.extend([new_node("G")])

    output = depth_of_tree(root)
    print(f"depth of tree is {output}")



    
