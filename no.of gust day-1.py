T=int(input("enter number t:"))
E=[3,4,6,3]
L=[3,5,2,1]
X=[0,0,0,0]
for i in range(0,T):
    X[i]=(X[i-1]+E[i])-L[i]
print(X[i])
print("max gust",max(X))
    
