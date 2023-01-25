str1=input("enter the first string:")
str2=input("enter the second string:")
s1=list(str1.split(" "))
s2=list(str2.split(" "))
for i in s1:
    if(i in s2):
        s1.remove(i)
        s2.remove(i)
print(*s1)
print(*s2)


