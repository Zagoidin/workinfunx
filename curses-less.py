def prixy(x, y, cont): #РАБОТАЕТ, РАБОТАЕТ СУКА!!!!!!!
    xs = str(x)
    ys = str(y)
    z = str('\033['+ys+';'+xs+'H')
    print(z+cont)
def tabbel(x,y,blt='┌',brt='┐',blb='└',brb='┘',bx='─',by='│'): #ТОЖЕ РАБОТАЕТ!!!!
    z = str(blt+bx*x+brt+'\n'+(by+' '*x+by+'\n')*y+blb+bx*x+brb)
    return z
