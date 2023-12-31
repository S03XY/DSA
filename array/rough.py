
# for calculating factorial
def factorial(n):
    if (n== 0 or n==1):
        return 1
    return  n * factorial(n-1)

# while True:  
#     number =  int(input())
#     print(f"factorial is {factorial(number)}")


# fabonacci sequences
def fabonacci(n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1  
    return fabonacci(n-2) + fabonacci(n-1)



# while True:
#     number = int(input())
#     print(f"fabonacci is {fabonacci(number)}")




