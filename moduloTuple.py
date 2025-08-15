# Input two tuples and write a python program to find Modulo of tuple elements and store in a third tuple.

n = int(input("Enter the divisor : "))
tuple1 = tuple(map(int,input("Enter items to add in first tuple : ").split()))
tuple2 = tuple(map(int,input("Enter items to add in second tuple : ").split()))
tuple3 = tuple(x % n for x in tuple1) + tuple(y % n for y in tuple2)
print("The merged tuple is : ", tuple3)