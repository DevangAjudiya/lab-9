def power(num,pow):
    if pow==0:
        return 1
    return num*power(num,pow-1)
print(power(9,2))