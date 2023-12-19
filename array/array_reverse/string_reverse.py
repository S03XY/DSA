S = "i.like.this.program.very.much"


def string_reverse (S):
    string_list = S.split(".")
    n= len(string_list)
    start_i = 0
    last_i= n-1
    
    while (start_i < last_i):
        string_list[start_i],string_list[last_i]=string_list[last_i],string_list[start_i]
        start_i+=1
        last_i-=1

    process_array = ".".join(string_list)    
    return process_array




# reversed_string = string_reverse(S)
# print("reversed string",reversed_string)


def reverse_string(S):
     sub_list = list(S)
     sub_list.reverse()
     return "".join(sub_list)   



def reverse_each_char(S):
    string_list = S.split(".")
    n= len(string_list)
    start_index = 0
    last_index = n-1

    while start_index <= last_index:
        val = string_list[start_index]
        string_list[start_index] = reverse_string(val)    
        start_index+=1

    return ".".join(string_list)





revesed_string = reverse_each_char(S)
print(revesed_string)


