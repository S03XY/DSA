# binary tree


class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


# for recursion there has to be a base condition for recursion to terminate
def check_node_exists(node:BinaryNode,data:int):
    if node.data == data:
        return True   
    
    if node.left == None:
       return False
    
    if node.right == None:
        return False

    response =  check_node_exists(node.left,data)
    if response:
        return True
    response2 = check_node_exists(node.right,data)
    return response2

    

if __name__ == "__main__":

    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)

    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)

    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    root.left.left.left = BinaryNode(7)
    root.left.right.left = BinaryNode(8)
    root.left.right.right = BinaryNode(9)


    ouput= check_node_exists(root,9)
    if ouput:
        print("YES")
    else:
        print("FALSE")

        