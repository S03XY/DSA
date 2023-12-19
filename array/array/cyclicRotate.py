input_array = [1,2,3,4,5]
# output array =[5,1,2,3,4]


# one way to solve where time complexity O(n) and space complexity is O(n)
def rotate(input_array):
    # last_element = input_array[len(input_array)-1]
    # process_arr =[0 for i in range(0,len(input_array))]
    # process_arr[0] = last_element;
    # for i in range(1,len(input_array)):
    #     process_arr[i]= input_array[i-1]      
    # return process_arr

    n= len(input_array)
    last_ele = input_array[n-1]

    for i in range(n-1,0,-1):
        input_array[i] = input_array[i-1]

    input_array[0] = last_ele
    return input_array    



# correct way to solve where time complexity is O(n) and space complexity is O(n)

def correct_way(input_array):
    n = len(input_array)
    last_ele = input_array[n-1]
    for i in range(n-1,0,-1):
        input_array[i] = input_array[i-1]
    input_array[0] = last_ele
    return input_array






# rotated_array = rotate(input_array)
rotated_array = correct_way(input_array)
print("rotated array",rotated_array)


