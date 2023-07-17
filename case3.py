# Ortalama qiymeti tapmaq ucun 0 - 100 arasinda qiymet daxil edin.

bal = int(input('Qiymet daxil edin: '))

if ( bal > 90 and bal <= 100):
    print("Siz elaci oldunuz ve stipendiya alacaqsiniz.")
elif ( bal > 70 and bal <=90):
    print('Siz zerbeci oldunuz.')
elif ( bal > 50 and bal <= 70):
    print('Siz adi oldunuz.')
elif( bal <= 50):
    print('Siz kesildiniz.')
else:
    print('Daxil etdiyiniz melumat yanlisdir.')
