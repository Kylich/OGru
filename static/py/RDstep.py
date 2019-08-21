import os
import sys
import random

WillPower = self.WPchQt.isChecked()
DicePull = self.DicePullQt.value()
NumRoll = self.NumRollQt.value()
Str = self.StrQt.isChecked()
sender = self.sender().text()
if sender == 'RR':
	RR = True
	self.RRstrQt.setEnabled(False)
else:
	RR = self.RRchQt.isChecked()

Q = self.QQt.currentText()
Q = int(Q[0:Q.find(':')])
OM = self.OMQt.value()

LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
Luck = LuckRR + LuckR

if Str:
	if RR:
		LuckGlobal = self.LuckGlobalRR
		y = self.yRR
		z = self.zRR
		r = self.rRR
		RandList = self.RandListRR
		WillPower = True
		WP3 = False


		if y == 0:
			DetalText = ''
			JoinText = ('Dice:'  + str(DicePull) +
						' Roll:' + str(NumRoll) +
						' WP:'   + str(WillPower) +
						' Q:'    + str(Q) +
						' RR:'   + str(RR) +
						' OM:'   + str(OM) +
										'\r\n')
		else:
			JoinText = (self.JoinTextRR +
						'\nDice:' + str(DicePull) +
						' Roll:' + str(NumRoll) +
						' WP:' + str(WillPower) +
						' Q:' + str(Q) +
						' RR:' + str(RR) +
						' OM:' + str(OM) +
										'\r\n')
			DetalText = self.DetalTextRR
	else:
		LuckGlobal = self.LuckGlobal
		y = self.y
		z = self.z
		r = self.r

		if sender == 'WP':
			WillPower = True
			WP3 = True
			self.RRstrQt.setEnabled(False)
		else:
			WillPower = False
			WP3 = False
			self.RRstrQt.setEnabled(True)

		if y == 0:
			RandList = []
			DetalText = ''
			JoinText = ('Dice:' + str(DicePull) +
						' Roll:' + str(NumRoll) +
						' WP:' + str(WillPower) +
						' Q:' + str(Q) +
						' RR:' + str(RR) +
						' OM:' + str(OM) +
										'\r\n')
		else:
			JoinText = (self.JoinText +
						'\nDice:' + str(DicePull) +
						' Roll:' + str(NumRoll) +
						' WP:' + str(WillPower) +
						' Q:' + str(Q) +
						' RR:' + str(RR) +
						' OM:' + str(OM) +
										'\r\n')
			DetalText = self.DetalText
			RandList = self.RandList
else:
	JoinText = ('Dice:' + str(DicePull) +
				' Roll:' + str(NumRoll) +
				' WP:' + str(WillPower) +
				' Q:' + str(Q) +
				' RR:' + str(RR) +
				' OM:' + str(OM) +
									'\r\n')
	WP3 = True if WillPower and not RR else False
	LuckGlobal = y = z = r = 0
	DetalText = ''
	RandList = []

Pp = 2 if RR else 1			
z_all = NumRoll * DicePull * Pp * 5
if z_all < 100: z_all = 100

if not RandList:
	while z <= z_all:
		RandList.append(random.randint(0, 9))
		z += 1


if sender == 'GO' and Str:
	self.LuckGlobalRR = LuckGlobal
	self.yRR = y
	self.zRR = z
	self.rRR = r
	self.RandListRR = RandList
	self.DetalTextRR = DetalText
	self.JoinTextRR = JoinText
#
# Rolls start
#
while y < NumRoll or Str:
	if y: # != 0:
		DetalText += ('\n' * 2)

	DetalText += ('---> Бросок №' + str(y+1) + ' <---\n')

	DicePullTMP = DicePull + 3 if WP3 else DicePull
	DPch = DicePullTMP

	y += 1
	Roll = []
	
	#JoinText += '[' + str(y) + '] '
	
	if NumRoll > 1:
		JoinText += '[' + str(y) + '] '
	else: JoinText += ''


	LuckCount = DramCount = DicePullQ = x = 0
	
	while x < DicePullTMP + DicePullQ:
		Space = 7 if (x+1) // 10 else 8 #>= 1 else 8

		Roll.append(RandList[r])

		(ShortText, LongText, LuckCount,
			DramCount, DicePullQ, DicePullTMP) = (Choosing.main(x, Roll[x], Luck,
												LuckRR, LuckR, WillPower, DicePullTMP,
												DicePullQ, LuckCount, RR, DramCount,
												Space, RandList, r))

		DetalText += LongText
		JoinText  += ShortText
		
		if x == DPch-1:
			DetalText += ('--------------\n')
			JoinText = JoinText[:-2] + ': '
		
		r += 1
		x += 1

	if JoinText[-2:-1] == '-':
		JoinText = JoinText[:-2]
	if JoinText[-2:-1] == ':':
		JoinText = JoinText[:-2] + '---> '
	else:
		JoinText += '---> '
	
	DetalText += ('Успехов = ' + str(LuckCount) +
					'\tЕдиниц = ' + str(DramCount) + ' \n')

	if LuckDel and LuckCount > 0:
		DetalText += (' > > Ужасное качество < <\t-1 успех\n')
		LuckCount -= 1
		if LuckCount < 0: LuckCount = 0
	
	if OM and LuckCount > 0:
		DetalText += ('        > > OM < <\t' + str(OM) + ' успех\n')
		LuckCount += OM
		if LuckCount < 0: LuckCount = 0

	if DramCount > LuckCount:
		LuckCount = -DramCount
		DetalText += ('      > > Драмат < <\n')

	# elif LuckCount == 0 and y != NumRoll:
	# 	DetalText += (' > > Успехов не набрано < <\t-1 куб\n')
	# 	if Str: self.DicePullQt.setValue(DicePull-1)
	# 	DicePull -= 1

	elif LuckCount >= 5:
		if NumRoll > 1:
			Except = LuckCount - 4
			DetalText += ('      > > Except < <\t' + str(LuckCount) + ' это ' + str(LuckCount + Except) + '\n')
			LuckCount += Except
		else:
			Except = LuckCount - 4
			DetalText += ('      > > Except < <\t(если бросок длительный: ' + str(LuckCount) + ' это ' + str(LuckCount + Except) + ')\n')
		
	LuckGlobal += LuckCount
	JoinText += str(LuckCount) + '\r\n'

	Spam, SpamG = (5, 18) if LuckGlobal//10 else (6, 19) # >= 1 else (6, 19)
	
	if y == NumRoll or DicePull == 0:
		DetalText += ('+'*SpamG + '\n')
	DetalText += ('+'*Spam + ' Успех = ' + str(LuckGlobal) + ' ' + '+'*Spam + '\n')
	if y == NumRoll or DicePull == 0:
		DetalText += ('+'*SpamG + '\n')

	if DicePull == 0:
		DetalText += ('Кубов не осталось\n')
		break
	elif Str: break

#
# Rolls end
#



if not Str or (y >= NumRoll or DicePull == 0):
	DetalText += ('\n' * 3)
	JoinText += 'Итого: ' + str(LuckGlobal) + '\r\n\n'
	
	if Hash:
		DetalText = JoinText + DetalText
	else:
		DetalText = 'Мошенник!!!'
	
	self.DetTextQt.setText(DetalText)

	self.LuckGlobal = 0
	self.y = 0
	self.z = 0
	self.r = 0
	self.RandList = []
	self.DetalText= ''
	self.JoinText = ''

	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(JoinText)
	win32clipboard.CloseClipboard()

else:
	self.LuckGlobal = LuckGlobal
	self.y = y
	self.z = z
	self.r = r
	self.RandList = RandList
	self.DetalText= DetalText
	self.JoinText = JoinText
	
	DetalText += ('\n' * 3)
	JoinText += '> > ' + str(LuckGlobal) + ' < <\r\n\n'
	if Hash:
		DetalText = JoinText + DetalText
	else:
		DetalText = 'Мошенник!!!'
	
	self.DetTextQt.setText(DetalText)
self.RunQt.setEnabled(True)
