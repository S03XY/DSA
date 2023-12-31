from sys import maxsize

array = [21,642, 642,642, 642, 642, 642, 642]
# 5,4,3

def find_third_larget(arr:list,n:int):
    first = second = third = float("-inf")
    arr = list(set(arr))
    for num in arr:
        if (num > first):
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num        

    print(f"{first} {second} {third} ")
    return second






output = find_third_larget(array,len(array))
print(output)



