def frequency(st):
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
    for i in range(len(ls)):
        c=0
        for j in range(len(ls)):
            if(ls[i]==ls[j]):
                c=c+1
        dic.update({ls[i]:c})
    return dic          
a=input("enter the string = ")
print(frequency(a))
