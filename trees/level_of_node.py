# assuming binary tree


class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left= None
        self.right = None




def find_node_level(node:BinaryNode,data:int):
    print(f"checking node {node.data} ")

    if (node.data == data):
        return 1

    if (node.left == None):
        return 0
    if (node.right == None):
        return 0
    

    res1 = find_node_level(node.left,data)
    print("res1",{res1})

    if (res1 != 0):
        print(f"found it {res1}")
        return res1 + 1


    res2 = find_node_level(node.right,data)

    if (res2 == 1):
       return  res2 + 1









if  __name__ == "__main__":
    root = BinaryNode(3)
    root.left = BinaryNode(2)
    root.right = BinaryNode(5)

    root.left.left = BinaryNode(1)
    root.left.right = BinaryNode(4)

    data = 2
    output = find_node_level(root,data)
    print(f"level of given node is {output}")