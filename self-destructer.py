from os import remove, path, rmdir, system, getcwd
from sys import argv
from colorama import init
import shutil
init()
system('Title Инструмент деинсталляции')
system(f'mode con: cols=88 lines=16')
file_path = getcwd()
print('\n\t\033[1;31mВнимание! Данная утилита полностью и безвозвратно стирает все файлы\n\tпрограммы вместе с директорией', file_path,'и (на данный момент)\n\tфайлами сохранения.\n\t\t###\n\tДля подтверждения удаления программы, введите "ПОДТВЕРЖДАЮ".')
a = input('\033[0m\t>')
if a != 'ПОДТВЕРЖДАЮ':
    exit()          
else:
    print('\033[1;31m\tПрограмма готова к деинсталляции, нажмите Enter, чтобы запустить процесс.')
    input()
    shutil.rmtree(file_path, ignore_errors=True)
    try:
        rmdir(file_path)
    except PermissionError:
        print('\033[22m\t! ДИРЕКТОРИЯ БЫЛА ОЧИЩЕНА, НО НЕ УДАЛЕНА !\n\tПричина: Ошибка доступа (Директория занята другим процессом(Открыта\n\t в другой программе.))\033[1m')
        input()
    finally:
        print('\tПрограмма успешно деинсталлирована, установить её заново можно с\n\t нашего репозитория на GitHub')
        input()

