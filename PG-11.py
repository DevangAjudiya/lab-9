#Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it.
def creat_list(ls1,ls2):
    ls1=set(ls1)
    ls2=set(ls2)
    return list(set(ls1) & set(ls2))
ls1=[]
ls2=[]
print("enter first list")
for i in range(5):
    a=int(input())
    ls1.append(a)
print("enter second list")
for i in range(5):
    a=int(input())
    ls2.append(a)
print(creat_list(ls1,ls2))
                
