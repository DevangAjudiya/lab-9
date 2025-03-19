def sum_avg(la):
    dic={}
    sum=0
    for i in la:
        sum=sum+i
    avg=sum/5
    dic.update({"sum":sum,"avg":avg})
    return dic
ls=[]
print("enter the marks")
for i in range(1,5+1):
    print("enter the marks of",i,"subject")
    a=int(input(""))
    ls.append(a)
print(sum_avg(ls))

