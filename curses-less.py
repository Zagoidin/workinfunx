def prixy(x, y, cont): #РАБОТАЕТ, РАБОТАЕТ СУКА!!!!!!!
    xs = str(x)
    ys = str(y)
    z = str('\033['+ys+';'+xs+'H')
    print(z+cont)
def tabbel(x,y,preset='thin'):
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
    z = str(chorder[0]+chorder[4]*x+chorder[1]+'\n'+(chorder[5]+' '*x+chorder[5]+'\n')*y+chorder[2]+chorder[4]*x+chorder[3])
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
