# Write a Python function that prints out the first n rows of Pascal's triangle.
n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    first = 1
    for j in range(1,n-i+1):
        print(" ",end = "")
    for k in range(1,i+1):
        print(first,end=" ")
        first = first * (i-k)//k
    print()