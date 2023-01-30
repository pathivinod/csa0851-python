str1=input("enter the name:")
str2=input("enter the 2nd name:")
def isisomorphic(str1,str2):
    if(len(str1)!=len(str2)):
       return False
    else:
        map1={ }
        map2={ }
        for i in range(len(str1)):
            ch1=str1[i]
            ch2=str2[i]
            if(ch1 not in map1):
                map1[ch1]=ch2
            if(ch2 not in map2):
                map2[ch2]=ch1
            if(map1[ch1]!=ch2 or map2[ch2]!=ch1):
                return False
        return True
print(isisomorphic(str1,str2))
