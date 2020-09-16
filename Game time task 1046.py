X,Y=map(int,input().split())
if X>Y :
    A=24-X
    Z=A+Y
    print("O JOGO DUROU %d HORA(S)"%Z)
elif Y>X :
    Z=Y-X
    print("O JOGO DUROU %d HORA(S)"%Z)
elif X==Y :
    Z=24
    print("O JOGO DUROU %d HORA(S)"%Z)