def greatest(a,b,c):
    if (a>b and a>c):
        return("a is greatest")
    elif (b>a and b>c):
        return("b is greatest")
    else:
        return("c is greatest")

print(greatest(100,200,1200))