n=int(input("enter the no.of elements:"))
l1=[ ]
while True:
    num=int(input("enter the element:"))
    if(num==" "):
        break;
    else:
        l1.append(num)
        if len(l1)==n:
            break
print(l1)
def sumsquare(l1):
    odd=[ ]
    even=[ ]
    l2=[ ]
    for i in range(0,len(l1)):
        if(l1[i]%2==0):
            even.append(l1[i])
        else:
            odd.append(l1[i])
    print(even,odd)
    evensquare=sum([x**2 for x in even])
    l2.append(evensquare)
    oddsquare=sum([x**2 for x in odd])
    l2.append(oddsquare)
    return(l2)
print(sumsquare(l1))







































































































































n=int(input("enter the no.of elements:"))
l1=[]
while True:
    num=int(input("enter the element:"))
    if(num==" "):
        break
    else:
        l1.append(num)
        if len(l1)==n:
            break
print(l1)
print(sumsquare(l1))































