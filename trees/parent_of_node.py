# assuming the tree is binary 

class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


def find_parent(node:BinaryNode, data:int,isRoot:bool):
    if (isRoot):
        if (node.data == data):
            return -1
        else:
            if node.left == None:
                return None

            if node.right == None:
                return None    
            
            if node.left.data == data:
                return node
            if node.right.data == data:
                return node
            
            left_response = find_parent(node.left,data,True)
            if left_response is not None:
                return left_response
            
            right_reponse = find_parent(node.right,data,True)
            return right_reponse
    else:
        raise  Exception("Invalid root node")
        


if __name__ == '__main__':

    root = BinaryNode(1)

    root.left = BinaryNode(2)
    root.right = BinaryNode(3)

    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)

    output = find_parent(root,5,True)
    if output is not None:
        print(f"found parent is {output.data}")
    else:
        print(f"no parent found")

