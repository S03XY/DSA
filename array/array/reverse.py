# reverse an input array
my_array = [1,4,2,3,5]


def simpleReverse (array):
    array.reverse()
    print("simple reverse",array," ","\t")
    # pass



# time complexity O(n) space complexity O(1)
def reverse_array_method_one(_array=[]):
    start_index=0
    last_index= len(_array) -1 

    while start_index < last_index:
        _array[start_index],_array[last_index] = _array[last_index],_array[start_index]
        start_index +=1 
        last_index -=1


    print(f"reversed array {_array}")
    return _array
    


# reverse_array_method_one(my_array)
# simpleReverse(my_array)




