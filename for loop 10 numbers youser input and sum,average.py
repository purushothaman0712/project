a=[]
print('enter 10 numbers')
for i in range(5):
    num=int(input('enter numbers'+str(i+1)))
    a.append(num)
sum=0
for i in a:
    sum=sum+i
print('addision:',sum)
print('average:',sum/5)
