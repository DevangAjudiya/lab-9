def convert(st):
    a=""
    ls=[]
    dic={}
    for i in st:
        if i == " ":
            ls.append(a)
            a=""
        else:
            a=a+i
    ls.append(a)
    ls=set(ls)
    ls=list(ls)
    ls.sort()
    return ls

a=input("enter the string = ")
print(convert(a))
