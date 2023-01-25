year=eval(input("enter the year:"))
if(year<=0 or year==float):
    print("invalid")
if(year%100==0):
    print("itis not leap year")
elif(year%400==0):
    print("it is a leap year")
elif(year%4==0):
    print("it is  a leap year")
else:
    print("it is not a leap year")
    m=year%4
    print("previous leap year is:",year-m)
