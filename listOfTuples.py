#  Write a Python program to create a list of tuples from given list having number and its cube in each tuple. (e.g. (2,8),(3,27),....)
n = int(input("How many tuples ? "))
my_list = []
for i in range(n):
    a = int(input(f"Enter number {i+1} : "))
    b = a**3
    my_list.append((a,b))
print("The list of tuples is : ", my_list)