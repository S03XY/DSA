# find position of first occurrence of a number

array = [9,7,2,16,4]


def linearSearch(array:list, value:int):
    for i,v in enumerate(array):
       if v == value:
           return i+1





if __name__ == "__main__":
    k=16
    output = linearSearch(array,k)
    print(f"position is {output}")



