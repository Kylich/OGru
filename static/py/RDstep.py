import os
import sys
import random

WillPower = self.WPchQt.isChecked()
DicePull = self.DicePullQt.value()
NumRoll = self.NumRollQt.value()
sender = self.sender().text()
if sender == 'stepRR':
	RR = True
	self.RRstrQt.setEnabled(False)
else: RR = False

Q = self.QQt.currentText()
Q = int(Q[0:Q.find(':')])
OM = self.OMQt.value()

LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
Luck = LuckRR + LuckR

if RR:
	LuckGlobal = self.LuckGlobalRR
	y = self.yRR
	z = self.zRR
	r = self.rRR
	RandList = self.RandListRR
	WillPower = True
	WP3 = False


	if y == 0:
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
		JoinText = ('Кубы:' + str(DicePull) +
					' Броски:' + str(NumRoll) +
					' ПСВ:' + str(WillPower) +
					' Доброс:' + str(Q) +
					' Переброс:' + str(RR) +
					' Автоуспехи:' + str(OM) +
									'\r\n')
	else:
		JoinText = (self.JoinText +
					'\nКубы:' + str(DicePull) +
					' Броски:' + str(NumRoll) +
					' ПСВ:' + str(WillPower) +
					' Доброс:' + str(Q) +
					' Переброс:' + str(RR) +
					' Автоуспехи:' + str(OM) +
									'\r\n')
		RandList = self.RandList


Pp = 2 if RR else 1			
z_all = NumRoll * DicePull * Pp * 5
if z_all < 100: z_all = 100

if not RandList:
	while z <= z_all:
		RandList.append(random.randint(0, 9))
		z += 1

self.LuckGlobalRR = LuckGlobal
self.yRR = y
self.zRR = z
self.rRR = r
self.RandListRR = RandList
self.JoinTextRR = JoinText


#
# Rolls start
#

DicePullTMP = DicePull + 3 if WP3 else DicePull
DPch = DicePullTMP

y += 1
Roll = []

if NumRoll > 1:
	JoinText += '[' + str(y) + '] '
else: JoinText += ''


LuckCount = DramCount = DicePullQ = x = 0

while x < DicePullTMP + DicePullQ:
	Space = 7 if (x+1) // 10 else 8

	Roll.append(RandList[r])

	(ShortText, LuckCount,
		DramCount, DicePullQ, DicePullTMP) = (Choosing.main(x, Roll[x], Luck,
											LuckRR, LuckR, WillPower, DicePullTMP,
											DicePullQ, LuckCount, RR, DramCount,
											RandList, r))

	JoinText  += ShortText
	
	if x == DPch-1:
		JoinText = JoinText[:-2] + ': '
	
	r += 1
	x += 1

if JoinText[-2:-1] == '-':
	JoinText = JoinText[:-2]
if JoinText[-2:-1] == ':':
	JoinText = JoinText[:-2] + '---> '
else:
	JoinText += '---> '

if OM and LuckCount > 0:
	LuckCount += OM
	if LuckCount < 0: LuckCount = 0

if LuckDel and LuckCount > 0:
	LuckCount -= DramCount
	if LuckCount < 0: LuckCount = 0

if DramCount > LuckCount:
	LuckCount = -DramCount

# elif LuckCount == 0 and y != NumRoll:
# 	self.DicePullQt.setValue(DicePull-1)
# 	DicePull -= 1

elif LuckCount >= 5:
	if NumRoll > 1:
		Except = LuckCount - 4
		LuckCount += Except
	else:
		Except = LuckCount - 4
	
LuckGlobal += LuckCount
JoinText += str(LuckCount) + '\r\n'


#
# Rolls end
#

self.LuckGlobal = LuckGlobal
self.y = y
self.z = z
self.r = r
self.RandList = RandList
self.JoinText = JoinText

JoinText += '> > ' + str(LuckGlobal) + ' < <\r\n\n'
