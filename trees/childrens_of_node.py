class Node:
    def __init__ (self,data):
        self.data = data
        self.child =[]


def find_childrens_of_node(node:Node,data):
    for child in node.child:
        print(f"checking parent {node.data} and child {child.data}")
        if (child.data == data):
            print(len(child.child))
            return
        else: 
            find_childrens_of_node(child,data)







if __name__ == "__main__":
    root = Node(20)
    root.child = [Node(2),Node(34),Node(50),Node(60),Node(70)]
    root.child[0].child = [Node(15),Node(20)]
    root.child[1].child = [Node(30)]
    root.child[2].child = [Node(40),Node(100),Node(20)]
    root.child[3].child = [Node(60)]
    root.child[4].child = [Node(70)]
    root.child[0].child[1].child =[Node(25),Node(50)]

    nodeData = 50
    find_childrens_of_node(root,nodeData)
    


    

