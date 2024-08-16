# formula
#  c    (f-32)
# --- = ------
#  5       9
cel=int(input("enter a cel: "))
def temp(c):
    return ((9/5)*c)+32

print(temp(cel))

far=int(input("enter far:"))
def tempp(f):
    return ((5/9)*(f-32))

print(tempp(far))