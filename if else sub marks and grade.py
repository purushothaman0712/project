maths=int(input("maths subject mark:"))
physics=int(input("physics subject mark:"))
chemistry=int(input("chemistry subject mark:"))
avg=(maths+physics+chemistry)/3
print(avg)
if(avg>=90):
    print("grade A")
elif(avg>=80 and avg<=90):
    print("grade B")
elif(avg>=70 and avg<=80):
    print("grade C")
elif(avg>=60 and avg<=70):
    print("grade D")
else:
    print("grade F")
       
