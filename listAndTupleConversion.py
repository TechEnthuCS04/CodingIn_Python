# Write a python program to convert a Tuple to a List and vice – versa.
my_tuple = tuple(input("Enter items to add in tuple seperated by space : ").split())
my_list = input("Enter items to add in list seperated by space : ").split()
lt = list(my_tuple)
tl = tuple(my_list)
print("List to Tuple : ",tl)
print("Tuple to List : ",lt)