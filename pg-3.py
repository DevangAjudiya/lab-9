def creat_array(r,c,w,n):
    lis=[]
    for i in range(r):
        ley=[]
        for j in range(c):
            row=[]
            for k in range(w):
                row.append(n)
            ley.append(row)    
        lis.append(ley)    
    return lis

a=creat_array(2,2,2,2)
print(a)
                       
    
    
