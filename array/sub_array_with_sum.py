array = [1,2,3,4,5,6,7,8,9,10]
s=15

# points to note
# - sub array is continuous
# - return [-1] if it doesn't exist
# return an array of which start index and end index from left to right



def sub_array_of_a_sum (array:list,sum_value:int):
    sum =0
    n= len(array)
    left_most_index = -1
    right_most_index = -1
    for i in range(n):
        sum += array[i]
        print(f"sum at i {i}")
        for j in range(i+1,n):
            sum +=array[j]
            print(f"j sum is {sum}")
            if (sum  == sum_value):
                print(f"found a sum inside j {j} and i {i}")
                if left_most_index == -1:
                     left_most_index = i+1
                right_most_index = j     
                sum = 0
                break

        if (sum  == sum_value):
                print(f"found a sum outside")
                right_most_index = n
          
        sum = 0

    print(f"left most index is {left_most_index} and right most index is {right_most_index}")        



            
        








    


sub_array_of_a_sum(array,s)