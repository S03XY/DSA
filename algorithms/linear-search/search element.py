arr =[1,2,3,4]


def serachElement(value:int):
    global arr
    
    for i,v in enumerate(arr):
        if v == value:
            return i
    return -1


if __name__ == "__main__":
    element = 10
    output = serachElement(element)
    print(f"{output}")