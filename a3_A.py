# Write a program in Python to interchange the first and last elements in a list.
print("Enter any 5 elements : ")
my_list = []
for i in range(5):
    my_list.append(input())
temp = my_list[0]    
my_list[0] = my_list[len(my_list) - 1]
my_list[4] = temp
print("The swapped list is : ", my_list)
