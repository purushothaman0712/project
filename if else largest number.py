a=int(input("num1:"))
b=int(input("num2:"))
c=int(input("num3:"))
if(a>b and a>c):
    largest=a
elif(b>a and b>c):
    largest=b
else:
    largest=c
    print("largest number:",largest)

