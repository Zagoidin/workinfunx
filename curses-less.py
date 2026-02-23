def prixy(x, y, *cont, end=None, sep=' '):
    cont = map(str,cont)
    cont = sep.join(cont)
    z = f'\033[{y};{x}H'
    if end==None:
        end = f'\033[1B\033[{len(cont)}D'
    print(z+cont, end=end)
def tabbel(x,y,preset='thin',color=None):
    if preset == 'thin':
        chorder = ['┌','┐','└','┘','─','│']
    elif preset == 'bold':
        chorder = ['┏','┓','┗','┛','━','┃']
    elif preset == 'double':
        chorder = ['╔','╗','╚','╝','═','║']
    elif preset == 'triple':
        chorder = ['┌','┐','└','┘','┄','┆']
    elif preset == 'quadriple':
        chorder = ['┌','┐','└','┘','┈','┊']
    else:
        chorder = ['┌','┐','└','┘','─','│']
    n = str('\x1b[1B\x1b['+str(x+2)+'D')
    z = str(chorder[0]+chorder[4]*x+chorder[1]+n+(chorder[5]+' '*x+chorder[5]+n)*y+chorder[2]+chorder[4]*x+chorder[3])
    if color!=None:
        z = str(color+z+'\033[0m')
    return z
    
def scale1sc(max, act,width=20,f='█',p='░'):
    sec=int((act/max)*width)
    hol=int(width-sec)
    ph = str(p*hol)
    fs = str(f*sec)
    if hol<=0:
        ph = ''
    if sec<=0:
        fs = ''
    if len(fs)>width:
        fs = fs[:width]
    z = str(fs+ph)
    return z
##
def cls(): 
    import os
    a = os.name
    if (a == 'posix'):
        cls = 'clear'
    if (a == 'nt'):
        cls = 'cls'
    os.system(cls)
##
def setterminalsize(x, y):
    import os
    a = os.name
    if x < 15:
        x = 15
    if a == 'posix':
        request = f'stty cols {x} rows {y}'
    if a == 'nt':
        request = f'mode con: cols={x} lines={y}'
    prixy(1,1,request)
    os.system(request)
##
def fgcol(*parg):
    if len(parg) >=3:
        z = f'\033[38;2;{parg[0]};{parg[1]};{parg[2]}m'
        return z
    else:
        z = f'\033[38;5;{parg[0]}m'
        return z
##
def bgcol(*parg):
    if len(parg) >=3:
        z = f'\033[48;2;{parg[0]};{parg[1]};{parg[2]}m'
        return z
    else:
        z = f'\033[48;5;{parg[0]}m'
        return z
##
def psnd(nm, format='wav', dir='audio'):
    from playsound import playsound
    playsound(f'{dir}/{nm}.{format}', block=False)
##ЗАПУСК ФУНКЦИИ
# titulation = threading.Thread(target=Titulate)
# titulation.start()
