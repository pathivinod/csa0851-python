string=int(input("enter the integer:"))
string1=str(string)
string2=string1[: : -1]
if(string2==string1):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
