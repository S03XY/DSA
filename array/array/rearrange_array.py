input_arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]


def rearrange(input_arr):
    n= len(input_arr)
    vec= [-1]*n

    for i in range(0,n):
        if (input_arr[i] != -1):
            vec[input_arr[i]] = input_arr[i]

    return vec


print(*rearrange(input_arr))