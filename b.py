a=int(input('숫자를 입력해 주세요'))

for i in range(0,a+1):
    for j in range(i):
        print('*', end='')
    print()    
