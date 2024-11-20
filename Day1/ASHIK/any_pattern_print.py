number=int(input("ENTER THE VALUE: "))
symbol=input('ENTER THE CHARACTER: ')
for i in range (1,number+1):
    for j in range(i):
        print(symbol,end=' ')
    print()    
