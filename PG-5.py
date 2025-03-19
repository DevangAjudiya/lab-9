def ispangram(st):
    st=set(st)
    st.remove(" ")
    for i in range(65,91):
        if chr(i) in st:
            pass
        elif chr(i+32) in st:
            pass
        else:
            return False
    return True
a=input("enter the string=")
b= ispangram(a)
print(b)
