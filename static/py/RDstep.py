﻿def rollStep(DicePull, NumRoll, OM, Q,
				WillPower, RR, EText, sCheck,
				_LuckGlobalRR, _yRR, _zRR, _rRR, _RandListRR,
				_LuckGlobal,   _y,   _z,   _r,   _RandList,
				_JoinText, _JoinTextRR):

	import os
	import sys
	import random
	import Choosing
	import ChoosingQ

	RR = True if sCheck == 'RR' else False
		
	LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
	Luck = LuckRR + LuckR

	if RR:
		LuckGlobal = _LuckGlobalRR
		y = _yRR
		z = _zRR
		r = _rRR
		RandList = _RandListRR
		WillPower = True
		WP3 = False


		if y == 0:
			JoinText = ('Кубы:'  + str(DicePull) +
						' Броски:' + str(NumRoll) +
						' ПСВ:'   + str(WillPower) +
						' Доброс:'    + str(Q) +
						' Переброс:'   + str(RR) +
						' Автоуспехи:'   + str(OM) +
										'\r\n')
		else:
			JoinText = (_JoinTextRR +
						'\nКубы:' + str(DicePull) +
						' Броски:' + str(NumRoll) +
						' ПСВ:' + str(WillPower) +
						' Доброс:' + str(Q) +
						' Переброс:' + str(RR) +
						' Автоуспехи:' + str(OM) +
										'\r\n')
	else:
		LuckGlobal = _LuckGlobal
		y = _y
		z = _z
		r = _r

		if sCheck == 'WP':
			WillPower = True
			WP3 = True
		else:
			WillPower = False
			WP3 = False

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
			JoinText = (_JoinText +
						'\nКубы:' + str(DicePull) +
						' Броски:' + str(NumRoll) +
						' ПСВ:' + str(WillPower) +
						' Доброс:' + str(Q) +
						' Переброс:' + str(RR) +
						' Автоуспехи:' + str(OM) +
										'\r\n')
			RandList = _RandList


	Pp = 2 if RR else 1			
	z_all = NumRoll * DicePull * Pp * 5
	if z_all < 100: z_all = 100

	if not RandList:
		while z <= z_all:
			RandList.append(random.randint(0, 9))
			z += 1

	_LuckGlobalRR = LuckGlobal
	_yRR = y
	_zRR = z
	_rRR = r
	_RandListRR = RandList
	_JoinTextRR = JoinText


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
	# 	_DicePullQt.setValue(DicePull-1)
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

	_LuckGlobal = LuckGlobal
	_y = y
	_z = z
	_r = r
	_RandList = RandList
	_JoinText = JoinText

	JoinText += '> > ' + str(LuckGlobal) + ' < <\r\n\n'

	return (JoinText, _LuckGlobalRR, _yRR, _zRR, _rRR, _RandListRR,
			_JoinTextRR, _LuckGlobal, _y, _z, _r, _RandList, _JoinText)
