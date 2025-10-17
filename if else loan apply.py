salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 and age<=25):
    loan=int(input("loan amount:"))
    if(loan>=50000):
        print("maxium loan amount 50000")
    else:
        print("you are not eligible for loan")
else:
    print("you are not eligible for loan")
