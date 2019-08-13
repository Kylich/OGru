def chooseLD():
    import random
    
    dice = random.randint(0, 9)
    Q = 0
    LuckR = (8, 9)
    LuckRR = (0,)
    LuckDel = False
    
    if dice == 0:
            y = 1
            LDluck = []
            LDluck.append(dice)
            while True:
                    dice = random.randint(0, 9)
                    LDluck.append(dice)
                    if dice in LuckRR:
                            y += 1
                    else:
                            if dice in LuckR:
                                    y += 1
                            break
    
            if y > 1:
                    resultLD = '>>> Успехи ' + str(y) + '!!! (' + str(LDluck) + ')'
            else:
                    resultLD = '>>> Успех! (' + str(LDluck) + ')'
            
    elif dice == 1:
            resultLD = '>>> Драматический провал! (' + str(dice) + ')'
    else:
            resultLD = '>>> Провал (' + str(dice) + ')'

    return resultLD