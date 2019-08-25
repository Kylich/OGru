﻿from flask import Flask, render_template, request, json
import sys, os, random

Path = str(os.getcwd())
sys.path.insert(0, Path + '/static/py')
import LD, RD, report, RDstep
from tutorialpy import tutorialText
app = Flask(__name__)

LuckGlobalRR = 0
yRR = 0
zRR = 0
rRR = 0
RandListRR = []
LuckGlobal  = 0
y = 0
z = 0
r = 0
RandList = []
JoinText_ = []
JoinTextRR = []

LDcount = 0

@app.route('/')
def indexMain():
    return render_template("indexMain.html")
    
@app.route('/openroller/')
def indexOR():
    return render_template("indexOR.html")

@app.route('/opencrafter/')
def indexOC():
    return render_template("indexOC.html")

@app.route('/fullmod', methods=['GET', 'POST'])
def fullMod():
    fmCheck = int(request.args.get('fmCheck'))
    
    if fmCheck % 2 == 0:
        fmTextPerk = """<td><b>Перк:</b></td>
                        <td><input name="TEXT_ReRoll" id="TEXT_ReRoll" type="checkbox"/></td>"""
        fmTextPush = """<td><b><FONT color=green>Кнопка для Пуш!</font></b></td>
                        <td><input name="TEXT_PUSH" id="TEXT_PUSH" type="checkbox"/></td>"""
        fmTextOM = """<td><h4><b>Автоуспех:</b></h4></td>
                      <td><input type="number" min='-10' max='10' value=0 id="TEXT_OM" name="TEXT_OM"></td>"""
    else:
        fmTextPerk = ''
        fmTextPush = ''
        fmTextOM   = ''
        
    return json.dumps({
        'fmTextPerk': fmTextPerk,
        'fmTextPush': fmTextPush,
        'fmTextOM': fmTextOM,
    })

@app.route('/luckdice', methods=['GET', 'POST'])
def luckDice():
    global LDcount
    LDcount += 1
    JoinText = "<h2>["+ str(LDcount) + "] " + LD.chooseLD() + "</h2>"
    return json.dumps({'JoinText': JoinText})
    
@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():
    tutCheck = int(request.args.get('tutCheck'))
    if tutCheck % 2 == 0:
        tutText = tutorialText
    else:
        tutText = ''
    return json.dumps({'tutText': tutText})

@app.route('/rolldice', methods=['GET', 'POST'])
def rollDice():

    global globa
    TEXT_Dices = request.form['TEXT_Dices']
    TEXT_Rolls = request.form['TEXT_Rolls']
    TEXT_Q     = request.form['TEXT_Quality']
    
    try: TEXT_WP = 1 if request.form['TEXT_WillPower'] == 'on' else 0
    except: TEXT_WP = 0
    
    try: TEXT_PUSH = 1 if request.form['TEXT_PUSH'] == 'on' else 0
    except: TEXT_PUSH = 0

    TEXT_Dices = int(TEXT_Dices)
    TEXT_Rolls = int(TEXT_Rolls)
    TEXT_Q     = int(TEXT_Q)

    try:
        TEXT_OM = request.form['TEXT_OM']
        TEXT_OM = int(TEXT_OM)
    except: TEXT_OM = 0
    
    try: TEXT_RR = 1 if request.form['TEXT_ReRoll'] == 'on' else 0
    except: TEXT_RR = 0
    
    try:
        TEXT_EText = request.form['TEXT_EText']
        TEXT_EText = str(TEXT_EText)
    except:
        TEXT_EText = ''

    JoinText = RD.roll(TEXT_Dices, TEXT_Rolls, TEXT_OM,
                        TEXT_Q, TEXT_WP, TEXT_RR, TEXT_EText) #, DetalText

    if TEXT_EText and not TEXT_EText.isspace():
        if TEXT_EText.isdigit() == False:
            report.sending(TEXT_EText, JoinText)
            
    if TEXT_PUSH:
        rc = ['s', 'd']
        dicePush = []
        JT = JoinText[:]

        for jt_ in JT:
            jt = str(jt_)
            if jt[0] not in ('~', 'К'): 
                if jt.find(']') > 0:
                    jt = jt[jt.find(']')+1:]
                    
                while jt.find('(') > 0:
                    jt = jt.split(' ')
                    for j in jt:
                        if j.find('(') >= 0:
                            del jt[jt.index(j)]
                    jt = ' '.join(jt)
        
                jt = jt[:jt.find('>')]
        
                for j in jt:
                    if j.isdigit():
                        rc = random.choice(['s', 'd'])
                        dicePush.append(j+rc)
        
        finalPush = []
        for dice in dicePush:
            finalPush.append('<img src="/static/images/dicepush/%s.gif"/>' % dice)
    else: finalPush = ''

    JoinText = "<h2>" + "<br>".join(JoinText) + "</h2>"
    return json.dumps({
        'JoinText': JoinText,
        'finalPush': finalPush,
    })

###

@app.route('/stepmod', methods=['GET', 'POST'])
def stepMod():
    stepRl = '<input value="stepRl" type="button" onclick="stepRl();"/>'
    stepWP = '<input value="stepWP" type="button" onclick="stepWP();"/>'
    stepRR = '<input value="stepRR" type="button" onclick="stepRR();"/>'
    return json.dumps({
        'stepRl': stepRl,
        'stepWP': stepWP,
        'stepRR': stepRR,
    })

@app.route('/step', methods=['GET', 'POST'])
def step():
    global LuckGlobalRR
    global yRR
    global zRR
    global rRR
    global RandListRR
    global LuckGlobal
    global y
    global z
    global r
    global RandList
    global JoinText_
    global JoinTextRR

    sCheck = request.args.get('sCheck')
    if sCheck=='Rl': globa='Rl'
    TEXT_Dices = request.form['TEXT_Dices']
    TEXT_Dices = int(TEXT_Dices)

    TEXT_Rolls = request.form['TEXT_Rolls']
    TEXT_Rolls = int(TEXT_Rolls)
    TEXT_Q     = request.form['TEXT_Quality']
    TEXT_Q     = int(TEXT_Q)



    try: TEXT_WP = 1 if request.form['TEXT_WillPower'] == 'on' else 0
    except: TEXT_WP = 0

    try:
        TEXT_OM = request.form['TEXT_OM']
        TEXT_OM = int(TEXT_OM)
    except: TEXT_OM = 0
    
    try: TEXT_RR = 1 if request.form['TEXT_ReRoll'] == 'on' else 0
    except: TEXT_RR = 0
    
    try:
        TEXT_EText = request.form['TEXT_EText']
        TEXT_EText = str(TEXT_EText)
    except:
        TEXT_EText = ''

    (JoinText, LuckGlobalRR, yRR, zRR, rRR, RandListRR,
			JoinTextRR, LuckGlobal, y, z, r,
            RandList, JoinText_) = RDstep.rollStep(TEXT_Dices, TEXT_Rolls, TEXT_OM,
                        TEXT_Q, TEXT_WP, TEXT_RR, TEXT_EText,
                        sCheck, LuckGlobalRR, yRR, zRR, rRR,
                        RandListRR,	LuckGlobal, y, z, r,
                        RandList, JoinText_, JoinTextRR)

    JoinText = JoinText.split('\n')
    JoinText = "<h2>" + '<br>'.join(JoinText) + "</h2>"

    if y == TEXT_Rolls:
        JoinText += "<br>END"
        LuckGlobalRR = 0
        yRR = 0
        zRR = 0
        rRR = 0
        RandListRR = []
        LuckGlobal  = 0
        y = 0
        z = 0
        r = 0
        RandList = []
        JoinText_ = []
        JoinTextRR = []

    return json.dumps({
        'JoinText': JoinText,
        'finalPush': '',
    })   


###

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)