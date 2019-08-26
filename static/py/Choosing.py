def main(x, RollX, Luck, LuckRR, LuckR, WillPower,
            DicePullTMP, DicePullQ, LuckCount, RR,
            DramCount, RandList, r):
    
    if DicePullQ > 0 and x >= DicePullTMP:
        if RollX in LuckRR:                         #        1=0   +, Q, RR-
            ShortText = (str(RollX)+' - ')
            DicePullTMP += 1
            LuckCount += 1
        elif RollX in LuckR:                        #        1=8   +, RR-
            ShortText = (str(RollX) + ' - ')
            LuckCount += 1
        elif RollX == 1:                            #        1=1   RR-
            ShortText = (str(RollX) + ' - ')
            DramCount += 1
        else:                                       #        1=3   RR-
            ShortText = (str(RollX) + ' - ')

    else:
        if RollX in LuckRR:                         #        1=0    +, Q
            ShortText = (str(RollX) + ' - ')
            DicePullTMP += 1
            LuckCount += 1
        elif RollX in LuckR:                        #        1=8     +
            ShortText = (str(RollX)+' - ')
            LuckCount += 1
        elif RollX == 1:
            if RR and WillPower > 0:                #(1=1)          
                ShortText = ('(' + str(RollX) + ') ')
            else:                                   #        1=1   -
                ShortText = (str(RollX) + ' - ')
                DramCount += 1
        else: 
            if RR and WillPower > 0:                #(1=3)
                ShortText = ('(' + str(RollX) + ') ')
            else:                                   #        1=3           
                ShortText = (str(RollX) + ' - ')

        if RollX not in Luck and WillPower > 0 and RR:
            RollX = RandList[len(RandList) - r - 1]
            if RollX in LuckRR:                     #        1=0  +, Q
                ShortText += (str(RollX)+' - ')
                DicePullQ += 1
                LuckCount += 1
            elif RollX in LuckR:                    #        1=8  +
                ShortText += (str(RollX) + ' - ')
                LuckCount += 1
            
            elif RollX == 1:                        #        1=1  -
                ShortText += (str(RollX) + ' - ')
                DramCount += 1
            else:                                   #        1=3
                ShortText += (str(RollX) + ' - ')
    return ShortText, LuckCount, DramCount, DicePullQ, DicePullTMP