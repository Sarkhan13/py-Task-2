yas = int(input('Yasiniz: '))

elillik = input('Elilliyiniz var mi?: ')

if ( yas >= 70):
    print('Size prava dusmur.')
elif ( yas >= 18 and elillik == 'yox'):
    print('Siz prava ala bilersiniz.')
elif ( yas >= 18 and elillik == 'var'):
    print('Size prava dusmur. Cunki elilliyiniz var')
else :
    qaliq = 18 - yas
    print("prava almaq ucun sizin yasiniz catmir " + str(qaliq) + ' ilden sonra gelin')