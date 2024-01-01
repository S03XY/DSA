# binary tree
class BinaryNode:
    def __init__(self,data) -> None:
        self.data= data
        self.left = None
        self.right =None



def find_all_leaf_nodes(node:BinaryNode):    
    if (node.left is None and node.right is None):
        print(node.data,end=' ') 

    if (node.left is not None):
        find_all_leaf_nodes(node.left)
    if (node.right is not None):
        find_all_leaf_nodes(node.right)        


if __name__ == "__main__":
    root = BinaryNode(1)
    root.left = BinaryNode(2)

    root.left.left = BinaryNode(4)


    root.right = BinaryNode(3)
    root.right.left = BinaryNode(5)
    root.right.left.left = BinaryNode(6)
    root.right.left.right = BinaryNode(7)


    root.right.right = BinaryNode(8)
    root.right.right.left = BinaryNode(9)
    root.right.right.right = BinaryNode(10)

    
    find_all_leaf_nodes(root)
    





        