def roll(DicePull, NumRoll, OM, Q, WP, RR, EText):

        import random
        import Choosing
        import ChoosingQ
        
        LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
        Luck = LuckRR + LuckR
        
        JoinText = []

        JTWP = '+' if WP==1 else '-'
        JTRR = '+' if RR==1 else '-'
        EText = '+' if EText else '-'

        if Q==0: JTQ = "(0)"
        elif Q==1: JTQ = "(0/9)"
        elif Q==2: JTQ = "(0/9/8)"
        elif Q==-1: JTQ = "( )"
        elif Q==-2: JTQ = "(-)"
        else: JTQ = "(упс)"
        
        if JTRR=='-' and OM==0:
            JoinText.append ('Кубы:' + str(DicePull) +
                            ' Броски:' + str(NumRoll) +
                            ' Доброс:' + JTQ +
                            ' ПСВ:' + JTWP +
                            ' Отчет:' + EText)
        else:
            JoinText.append ('Кубы:' + str(DicePull) +
                            ' Броски:' + str(NumRoll) +
                            ' Доброс:' + JTQ +
                            ' ПСВ:' + JTWP +
                            ' Переброс:' + JTRR +
                            ' OM:' + str(OM) +
                            ' Отчет:' + EText)
        
        WP3 = True if WP and not RR else False
        LuckGlobal = y = z = r = 0
        RandList = []

        Pp = 2 if RR else 1			
        z_all = NumRoll * DicePull * Pp * 5
        if z_all < 100: z_all = 100

        if not RandList:
                while z <= z_all:
                        RandList.append(random.randint(0, 9))
                        z += 1
        
#
# Rolls start
#
        while y < NumRoll:
                DicePullTMP = DicePull + 3 if WP3 else DicePull
                DPch = DicePullTMP

                y += 1
                Roll = []
                
                if NumRoll > 1:
                    JoinTextTMP = '[%s] ' % y
                else: JoinTextTMP = ''
                
                LuckCount = DramCount = DicePullQ = x = 0
                
                while x < DicePullTMP + DicePullQ:
                        Roll.append(RandList[r])
                        
                        (ShortText, LuckCount,
                                DramCount, DicePullQ, DicePullTMP) = Choosing.main(x, Roll[x], Luck,
                                                                                LuckRR, LuckR, WP, DicePullTMP,
                                                                                DicePullQ, LuckCount, RR, DramCount,
                                                                                RandList, r)
                        JoinTextTMP += ShortText
                        
                        if x == DPch-1:
                                JoinTextTMP = JoinTextTMP[:-2] + ': '
                        
                        r += 1
                        x += 1

                if JoinTextTMP[-2:-1] == '-':
                        JoinTextTMP = JoinTextTMP[:-2]
                if JoinTextTMP[-2:-1] == ':':
                        JoinTextTMP = JoinTextTMP[:-2] + '---> '
                else:
                        JoinTextTMP += '---> '

                if LuckDel and LuckCount > 0:
                        LuckCount -= DramCount
                        if LuckCount < 0: LuckCount = 0
                
                if OM and LuckCount > 0:
                        LuckCount += OM
                        if LuckCount < 0: LuckCount = 0

                if DramCount > LuckCount:
                        LuckCount = -DramCount
                # elif LuckCount == 0 and y != NumRoll:
                #        DicePull -= 1
                elif LuckCount >= 5:
                        if NumRoll > 1:
                                Except = LuckCount - 4
                                LuckCount += Except
                        else:
                                Except = LuckCount - 4
                        
                LuckGlobal += LuckCount
                JoinTextTMP += str(LuckCount)
                JoinText.append(JoinTextTMP)

                if DicePull == 0:
                        break
#
# Rolls end
#
        JoinText.append('Итого: ' + str(LuckGlobal))
        return JoinText
