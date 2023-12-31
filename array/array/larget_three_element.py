array =[1, 8, 7, 56, 90]



def largest_three(arr:list,n:int):
    largest = 0
    for num in arr:
        if  num > largest:
            largest = num
        
    return largest




    



    # arr.sort()
    # return [arr[n-1],arr[n-2],arr[n-3]]





    



output = largest_three(array,len(array))
print("larget three elements are ",output)
