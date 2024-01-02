#  nodes are considered to be siblings if they have same parent node and are on same level

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.child = []
        
        
        

def find_sibling_of_node(node:Node,data):
    parentNode = node
    for child in node.child:
        print(f"checking parent node {node.data} and child node {child.data}")
        if (child.data == data):
            print(f"found node {child.data}")
            return node
        else:
            parentNode  = find_sibling_of_node(child,data)
            if parentNode is not None:
                return parentNode

        


if __name__ == "__main__":

    root = Node(10)
    root.child =[Node(20),Node(30),Node(40)]
    root.child[0].child =[Node(50),Node(60)]
    root.child[1].child = [Node(70),Node(80)]
    root.child[2].child = [Node(90),Node(100),Node(110)]


    searchNodeData = 100
    parent =  find_sibling_of_node(root,searchNodeData)
    if parent is not None:
        for node in parent.child:
            if (node.data != searchNodeData):
                print(node.data,end=" ")