p = print
i = input
fVB     = False
Vmax    = 0
VBAn = 'NO'
userCycleInt = int(i('Число проехавших автомобилей ::\n\t'))
for cycN in range(userCycleInt):
 V = int(i(f'Скорость машины {cycN+1}:\t'))
 if ( V < 30 and not fVB):
    fVB = True
    VBAn = 'YES'
    # p(f'\tfVB changed on lap {cycN+1}') #отладочное
 if ( V > Vmax ): 
    Vmax = V
    # p(f'\tVmax changed into {Vmax} on lap {cycN+1}') #отладочное
p(f'Итоги:\n\t{Vmax}\n\t{VBAn}')
