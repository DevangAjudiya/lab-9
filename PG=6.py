def lt(e):
    ls=[]
    for i in range(1,e+1):
        row=[]
        a=1
        for j in range(3):
            a=a*i
            row.append(a)
        ls.append(row)
    for i in range(len(ls)):
        ls[i]=tuple(ls[i])
    return ls
a=int(input("enter the last bound"))
print( lt(a))
