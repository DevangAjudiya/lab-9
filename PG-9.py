def count_alfa_num(sr):
    dic={}
    cap=0
    num=0
    for i in sr:
        if 65<=ord(i)<91 or (65+32<=ord(i)<91+32):
            cap=cap+1
        elif(0<=int(i)<=9):
            num=num+1     
        else:
            pass
    dic.update({"alpha":cap , "digit":num})
    return dic
a=input("enter the string = ")
a=a.replace(" ","")
print(count_alfa_num(a))
