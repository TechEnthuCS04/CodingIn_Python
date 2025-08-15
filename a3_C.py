# Write a Python program to find second largest number in a list
print("Enter any 5 elements : ")
my_list = []
for i in range(5):
    num = int(input())
    my_list.append(num)
    my_list.sort()
print("The second largest element is : ", my_list[3])
