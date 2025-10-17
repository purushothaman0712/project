a=int(input("a:"))
b=int(input("b:"))
operation=(input("add/sub/div/mul"))
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="div"):
    print(a/b)
elif(operation=="mul"):
    print(a*b)
else:
    print("invailed number")
