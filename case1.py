1.
print('17 + 8 misalinin duzgun cavabini tapin:')

print('A=23')
print('B=25')
print('C=20')

choose = input('Duzgun varianti secin: ')

if(choose == 'B'):
    print('Cavabiniz duzgundur.')
elif(choose == 'A' or  choose == 'C'):
    print('Cavabiniz yanlisdir')
else:
    print('Melumat yanlisdir')


2.
print('(17 + 8) ceminin kvadratini hesablayin')

kvad = pow(25, 2)
print(kvad)

print('A=144')
print('B=256')
print('C=625')

sual = input('duzgun cavabi yazin:')

if(sual == 'C'):
    print('cavabiniz dogrudur.')
elif(sual == 'A' or sual == 'B'):
    print('cavabiniz yanlisdir.')
else:
    print('daxil etdiyiniz melumat yanlisdir.')