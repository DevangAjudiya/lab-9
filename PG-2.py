def sume(b):
    sum=0
    a=0
    for i in range(1,b+1):
        sum=sum*10+b
        a=a+sum
    return a
        
a=int(input("enter the name = "))
b=sume(a)
print(b)
