#  nodes are considered to be siblings if they have same parent node and are on same level

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.child = []
        
        
        

def find_sibling_of_node(node:Node,data):
    for child in node.child:
        print(f"checking parent node {node.data} and child node {child.data}")
        if (child.data == data):
            # print(f"found node {child.data}")
            for c in node.child:
                  if c.data != data:
                      print(c.data,end=" ")


            return 
        else:
            find_sibling_of_node(child,data)

        


if __name__ == "__main__":

    root = Node(10)
    root.child =[Node(20),Node(30),Node(40)]
    root.child[0].child =[Node(50),Node(60)]
    root.child[1].child = [Node(70),Node(80)]
    root.child[2].child = [Node(90),Node(100),Node(110)]

    parent =  find_sibling_of_node(root,100)
    # print(f"parent node is {parent.data}")