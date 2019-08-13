def roll(DicePull, NumRoll, OM, Q, WillPower, RR, EText):

        import os
        import sys
        import random

        import Choosing
        import ChoosingQ
        
        LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
        Luck = LuckRR + LuckR
        
        JoinText = []
        
        JTWP = "да" if WillPower==1 else "нет"
        JTRR = "да" if RR==1 else "нет"
        
        if Q==0: JTQ = "(0)"
        elif Q==1: JTQ = "(0, 9)"
        elif Q==2: JTQ = "(0, 9, 8)"
        elif Q==-1: JTQ = "()"
        elif Q==-2: JTQ = "(- успех)"
        else: JTQ = "(бля)"
        
        EText = 'да' if EText else 'нет'
        
        if JTRR=="нет" and OM==0:
            JoinText.append ('Кубов:' + str(DicePull) +
                            ' Бросков:' + str(NumRoll) +
                            ' Переброс:' + JTQ +
                            ' ПСВ:' + JTWP +
                            ' Отчет:' + EText)
        else:
            JoinText.append ('Кубов:' + str(DicePull) +
                            ' Бросков:' + str(NumRoll) +
                            ' Переброс:' + JTQ +
                            ' ПСВ:' + JTWP +
                            ' Перк:' + JTRR +
                            ' OM:' + str(OM) +
                            ' Отчет:' + EText)
        
        WP3 = True if WillPower and not RR else False
        LuckGlobal = y = z = r = 0
        DetalText = []
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

                DetalText.append('---> Rolls #' + str(y+1) + ' <---')

                DicePullTMP = DicePull + 3 if WP3 else DicePull
                DPch = DicePullTMP

                y += 1
                Roll = []
                
                if NumRoll > 1:
                    JoinTextTMP = '[' + str(y) + '] '
                else: JoinTextTMP = ''
                
                LuckCount = DramCount = DicePullQ = x = 0
                
                while x < DicePullTMP + DicePullQ:
                        Space = 7 if (x+1) // 10 else 8

                        Roll.append(RandList[r])
                        
                        (ShortText, LongText, LuckCount,
                                DramCount, DicePullQ, DicePullTMP) = (Choosing.main(x, Roll[x], Luck,
                                                                                LuckRR, LuckR, WillPower, DicePullTMP,
                                                                                DicePullQ, LuckCount, RR, DramCount,
                                                                                Space, RandList, r))
                         
                        DetalText.append(LongText)
                        JoinTextTMP += ShortText
                        
                        if x == DPch-1:
                                DetalText.append('--------------')
                                JoinTextTMP = JoinTextTMP[:-2] + ': '
                        
                        r += 1
                        x += 1

                if JoinTextTMP[-2:-1] == '-':
                        JoinTextTMP = JoinTextTMP[:-2]
                if JoinTextTMP[-2:-1] == ':':
                        JoinTextTMP = JoinTextTMP[:-2] + '---> '
                else:
                        JoinTextTMP += '---> '
                
                DetalText.append('Lucks = ' + str(LuckCount) +
                                         '     Ones = ' + str(DramCount))

                if LuckDel and LuckCount > 0:
                        DetalText.append(' > > Terrible Q < <    -1 luck')
                        LuckCount -= 1
                        if LuckCount < 0: LuckCount = 0
                
                if OM and LuckCount > 0:
                        DetalText.append('        > > OM < <    ' + str(OM) + ' luck')
                        LuckCount += OM
                        if LuckCount < 0: LuckCount = 0

                if DramCount > LuckCount:
                        LuckCount = -DramCount
                        DetalText.append('      > > Dramat < <')
                #elif LuckCount == 0 and y != NumRoll:
                #        DetalText.append(' > > No Lucks < <    -1 dice')
                #        DicePull -= 1
                elif LuckCount >= 5:
                        if NumRoll > 1:
                                Except = LuckCount - 4
                                DetalText.append('      > > Except < <    ' + str(LuckCount) + ' it ' + str(LuckCount + Except))
                                LuckCount += Except
                        else:
                                Except = LuckCount - 4
                                DetalText.append('      > > Except < <     (if long Rolls: ' + str(LuckCount) + ' it ' + str(LuckCount + Except) + ')')
                        
                LuckGlobal += LuckCount
                JoinTextTMP += str(LuckCount)
                JoinText.append(JoinTextTMP)
                Spam, SpamG = (5, 18) if LuckGlobal//10 else (6, 19)
                
                if y == NumRoll or DicePull == 0:
                        DetalText.append('+'*SpamG)
                DetalText.append('+'*Spam + ' Luck = ' + str(LuckGlobal) + ' ' + '+'*Spam)
                if y == NumRoll or DicePull == 0:
                        DetalText.append('+'*SpamG)
                
                if DicePull == 0:
                        DetalText.append('No Dices')
                        break
#
# Rolls end
#
        JoinText.append('Итого: ' + str(LuckGlobal))

        return JoinText, DetalText
