def isMirror(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True 
print(isMirror(123)) 
