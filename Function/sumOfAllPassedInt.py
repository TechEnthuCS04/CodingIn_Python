# Write a Python program, where N number of integer arguments are passed to a function make_sum(), 
# which will print the sum of all the passed integers.
def make_sum(current_sum,num):
    current_sum += num
    return current_sum
n = int(input("Enter number of elements : "))
sum = 0
x = 0
for i in range(n):
    num = int(input("Enter the number to add : "))
    x += make_sum(sum,num)
print(f"The sum is : {x} ")
