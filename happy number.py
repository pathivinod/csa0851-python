def happy(n):
    temp=n
    sum=0
    while(temp>0):
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum
num=int(input("enter the number:"))
result=num
while result!=1 and result!=4:
    result=(happy(result))
if(result==1):
    print("it is a happy number")
elif(result==4):
    print("it is not a happy number")
