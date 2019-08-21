def main(x, RollX, Luck, LuckRR, LuckR, WillPower,
            DicePullTMP, DicePullQ, LuckCount, RR,
            DramCount, Space, RandList, r):
    
    if DicePullQ > 0 and x >= DicePullTMP:
        if RollX in LuckRR:                         #        1=0   +, Q, RR-
            LongText = (' '*Space + str(x+1) + ' = '
                + str(RollX) + '\t\t+, Q, RR-\n')
            ShortText = (str(RollX)+' - ')
            DicePullTMP += 1
            LuckCount += 1
        elif RollX in LuckR:                        #        1=8   +, RR-
            LongText = (' '*Space + str(x+1) + ' = '
                + str(RollX) + '\t\t+, RR-\n')
            ShortText = (str(RollX) + ' - ')
            LuckCount += 1
        elif RollX == 1:                            #        1=1   RR-
            LongText = (' '*Space + str(x+1) + ' = '
                + str(RollX) + '\t\t-, RR-\n')
            ShortText = (str(RollX) + ' - ')
            DramCount += 1
        else:                                       #        1=3   RR-
            LongText = (' '*Space + str(x+1) + ' = '
                + str(RollX) + '\t\tRR-\n')
            ShortText = (str(RollX) + ' - ')

    else:
        if RollX in LuckRR:                         #        1=0    +, Q
            LongText = (' '*Space+ str(x+1) + ' = '
                + str(RollX) + '\t\t+, Q\n')
            ShortText = (str(RollX) + ' - ')
            DicePullTMP += 1
            LuckCount += 1
        elif RollX in LuckR:                        #       1=8     +
            LongText = (' '*Space+ str(x+1) + ' = '
                + str(RollX) + '\t\t+\n')
            ShortText = (str(RollX)+' - ')
            LuckCount += 1
        elif RollX == 1:
            if RR and WillPower > 0:              #(1=1)          
                LongText = ('(' + str(x+1) + ' = '
                    + str(RollX) + ')\n')
                ShortText = ('(' + str(RollX) + ') ')
            else:                                   #        1=1   -
                LongText = (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\t\t-\n')
                ShortText = (str(RollX) + ' - ')
                DramCount += 1
        else: 
            if RR and WillPower > 0:              #(1=3)
                LongText = ('(' + str(x+1) + ' = ' 
                    + str(RollX) + ')\n')
                ShortText = ('(' + str(RollX) + ') ')
            else:                                   #        1=3           
                LongText = (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\n')
                ShortText = (str(RollX) + ' - ')

        if RollX not in Luck and WillPower > 0 and RR:
            RollX = RandList[len(RandList) - r - 1]
            if RollX in LuckRR:                     #        1=0  +, Q
                LongText += (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\t\t+, Q\n')
                ShortText += (str(RollX)+' - ')
                DicePullQ += 1
                LuckCount += 1
            elif RollX in LuckR:                    #        1=8  +
                LongText += (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\t\t+\n')
                ShortText += (str(RollX) + ' - ')
                LuckCount += 1
            
            elif RollX == 1:                                                            #        1=1  -
                LongText += (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\t\t-\n')
                ShortText += (str(RollX) + ' - ')
                DramCount += 1
            else:                                                                       #        1=3
                LongText += (' '*Space + str(x+1) + ' = ' 
                    + str(RollX) + '\n')
                ShortText += (str(RollX) + ' - ')
    return ShortText, LongText, LuckCount, DramCount, DicePullQ, DicePullTMP