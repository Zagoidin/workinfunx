i = input
rei = 30001
userCycleInt = int(i('Длина последовательности:\t'))
for cycN in range(userCycleInt):
    ui = int(i(f'Число #{cycN+1}:\t'))
    if ui%3==0 and ui < rei:
        rei=ui
print(f"Итог:\n\t{rei}")