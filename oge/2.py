i = input
cnt1 = 0
userCycleInt = int(i('Длина последовательности:\t'))
for cycN in range(userCycleInt):
 usi = int(i(f'Число {cycN+1}:\t'))
 if usi%3 == 0:
     cnt1+=1
print(f'Итог:\n\t{cnt1}')   