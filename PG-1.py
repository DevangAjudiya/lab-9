def count_lower_upper(sr):
    dic={}
    cap=0
    sm=0
    for i in sr:
        if 65<=ord(i)<91:
            cap=cap+1
        elif((65+32<=ord(i)<91+32)):
             sm=sm+1
        else:
            pass
    dic.update({"upper":cap , "lower":sm})
    return dic
a=input("enter the string = ")
a=a.replace(" ","")
print(count_lower_upper(a))
    
