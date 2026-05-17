i = input
mb = 0
fan = 'NO'
userCycleInt = int(i('Количество участников: \t'))
for cycN in range(userCycleInt):
    bb = int(i(f'Баллы участника #{cycN+1}:\t'))
    if bb == 0: fan = 'YES'
    if bb > mb: mb=bb
print(f'Итог:\n\t{mb}\n\t{fan}')