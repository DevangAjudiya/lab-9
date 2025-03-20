def ispangram(st):
    st=set(st)
    st2=set()
    for i in range(97,123):
        st2.update(chr(i))
    st= st & st2
    for i in range(65,91):
        if chr(i) in st:
            pass
        else:
            return False
    return True
a=input("enter the string=")
a=a.lower()
b= ispangram(a)
print(b)
