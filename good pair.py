n=[1,2,3,1,1,5]
count=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            print([i,j])
            count=count+1
print(count)
