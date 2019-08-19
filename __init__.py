from flask import Flask, render_template, request, json
import sys, os, random

Path = str(os.getcwd())
sys.path.insert(0, Path + '/static/py')

import LD, RD, report
from tutorialpy import tutorialText

app = Flask(__name__)

@app.route('/')
def indexMain():
    return render_template("indexMain.html")
    
@app.route('/openroller')
def indexOR():
    return render_template("indexOR.html")

@app.route('/opencrafter')
def indexOC():
    return render_template("indexOC.html")

@app.route('/stepmod', methods=['GET', 'POST'])
def stepMod():
    stepRoll = """
                <input value="stepRoll" id="stepRoll" type="button"/>
            """
    stepWP = """
                <input value="stepWP" id="stepWP" type="button"/>
            """
    stepRR = """
                <input value="stepRR" id="stepRR" type="button"/>
            """
    RDS = ''
    LDS = ''
    SMS = ''

    return json.dumps({'LDS': LDS, 'RDS': RDS, 'stepRoll': stepRoll, 'stepWP': stepWP, 'stepRR': stepRR, 'SMS': SMS})

@app.route('/fullmod', methods=['GET', 'POST'])
def fullMod():
    fmCheck = int(request.args.get('fmCheck'))
    
    if fmCheck % 2 == 0:
        fmTextPerk = """
                    <td><b>Перк:</b></td>
                    <td><input name="TEXT_ReRoll" id="TEXT_ReRoll" type="checkbox"/></td>
                """
        fmTextPush = """
                    <td><b><FONT color=green>Кнопка для Пушистой!</font></b></td>
                    <td><input name="TEXT_PUSH" id="TEXT_PUSH" type="checkbox"/></td>
                """
        fmTextOM = """
                    <td><h4><b>Автоуспех:</b></h4></td>
                    <td><input type="number" min='-10' max='10' value=0 id="TEXT_OM" name="TEXT_OM"></td>
                """
    else:
        fmTextPerk = ''
        fmTextPush = ''
        fmTextOM   = ''
        
    return json.dumps({'fmTextPerk': fmTextPerk, 'fmTextPush': fmTextPush, 'fmTextOM': fmTextOM})

@app.route('/luckdice', methods=['GET', 'POST'])
def luckDice():
    JoinText = "<h2>" + LD.chooseLD() + "</h2>"
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

    JoinText, DetalText = RD.roll(TEXT_Dices, TEXT_Rolls, TEXT_OM,
                                    TEXT_Q, TEXT_WP, TEXT_RR, TEXT_EText)

    if TEXT_EText and not TEXT_EText.isspace():
        if TEXT_EText.isdigit() == False:
            report.sending(TEXT_EText, JoinText)
            
    if TEXT_PUSH:
        rc = ['s', 'd']
        dicepush = []
        JT=JoinText[:]
        
        for jt in JT:
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
                        dicepush.append(j+rc)
        
        finalpush = []
        for dice in dicepush:
            finalpush.append('<img src="/static/images/dicepush/%s.gif"/>' % dice)
        
    else: finalpush = ''
    
    JoinText = "<h2>" + "<br>".join(JoinText) + "</h2>"
    return json.dumps({'JoinText': JoinText, 'finalpush': finalpush})
        
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
