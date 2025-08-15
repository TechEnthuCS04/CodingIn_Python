# Write a Python program to count Even and Odd numbers in a List.
print("Enter any 5 elements : ")
my_list = []
count_E = 0 
count_O = 0
for i in range(5):
    num = int(input())
    my_list.append(num)
    if num%2 == 0:
        count_E += 1
    else:
        count_O +=1
print("The number of even number is : ",count_E)
print("The number of odd number is : ",count_O)