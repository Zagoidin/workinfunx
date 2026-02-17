def prixy(x, y, cont): #РАБОТАЕТ, РАБОТАЕТ СУКА!!!!!!!
    xs = str(x)
    ys = str(y)
    z = str('\033['+ys+';'+xs+'H')
    e = str('\033[1B\033['+str(len(cont))+'D')
    print(z+cont, end=e)
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
    return z
def scale1sc(max, act,width=20,f='█',p='░'):
    sec=int((act/max)*width)
    hol=int(width-sec-1)
    z = str(f*sec+p*hol)
    return z
def scale2sc(max, acta, actb,width=20,f='█',p='░'):
    seca=int((acta/max)*width)
    secb=int((actb/max)*width)
    hol=int(width-seca-secb)
    z = str(f*seca+p*hol+'\033[31m'+f*secb+'\033[0m')
def Titulate():
    while True:
        request = str('Title '+title)
        os.system(request)
        if STOPTIT:
            break
        time.sleep(1)
def cls(): #Отлажено на UNIX & WINDOWS (успешно)
    a = os.name
    if (a == 'posix'):
        cls = 'clear'
    if (a == 'nt'):
        cls = 'cls'
    os.system(cls)
def setterminalsize(x, y):
    a = os.name
    if a == 'posix':
        sx=str(x)
        sy=str(y)
        request = str('stty cols '+sx+' rows '+sy)
    if a == 'nt':
        sx=str(x)
        sy=str(y)
        request = str('mode con: cols='+sx+' lines='+sy)
    os.system(request)
## ЗАПУСК ФУНКЦИИ
# titulation = threading.Thread(target=Titulate)
# titulation.start()
