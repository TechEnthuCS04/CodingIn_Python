# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_upper_lower(str):
    count_U = 0
    count_L = 0
    for i in str:
        if i == " ":
            continue
        elif ord(i)>=65 and ord(i)<=90:
            count_U +=1
        elif ord(i)>=97 and ord(i)<=122:
            count_L += 1
    print("No. of Upper case elements : ",count_U)
    print("No. of Lower case elements : ",count_L)
str = input("Enter a string : ")
count_upper_lower(str)