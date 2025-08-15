# Write a Python function to multiply all the numbers in a list.
def multiply(my_list):
    mul = 1
    for i in my_list:
        mul *= i
    print("Multiplying we get : ", mul)
    return
n = int(input("Enter number of items to be multiplied : "))
my_list = []
for i in range(n):
    num = int(input(f"Enter number {i+1} : "))
    my_list.append(num)
multiply(my_list)