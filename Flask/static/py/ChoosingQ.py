def select(X):
    if not X:
        LuckR = (8, 9)
        LuckRR = (0,)
        LuckDel = False
    elif X == 1:
        LuckR = (8,)
        LuckRR = (9, 0)
        LuckDel = False
    elif X == 2:
        LuckR = ()
        LuckRR = (8, 9, 0)
        LuckDel = False
    elif X == -1:
        LuckR = (8, 9, 0)
        LuckRR = ()
        LuckDel = False
    elif X == -2:
        LuckR = (8, 9, 0)
        LuckRR = ()
        LuckDel = True
    return LuckR, LuckRR, LuckDel