array =[7, 2, 9, 4, 6, 1, 3, 8, 5]

def sort_even_odd(arr:list, n:int):
    i = -1 
    for j in range(n):
        if (arr[j] % 2 == 0):
            i +=1
            arr[i],arr[j] = arr[j],arr[i]


sort_even_odd(array,len(array))
print(f"sorted array {array}")
