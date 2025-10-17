evencount=0
oddcount=0
for i in range(1,100):
    if(i%2==0):
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print('even numbers:',evencount)
print('odd numbers:',oddcount)
