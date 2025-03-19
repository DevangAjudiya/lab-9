def pelindrom(a):
    ls=list(a)
    for i in ls:
        if i==" ":
            ls.remove(" ")
    l=len(ls)
    for i in range(0,l//2):
        if(ls[i]==ls[l-i-1]):
            pass
        else:
            return False
    return True
s=input("enter the string =")
print("pelinndrom = ",pelindrom(s))
           
