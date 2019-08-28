from flask import Flask, render_template, request, json
import sys, os, random

Path = str(os.getcwd())
sys.path.insert(0, Path + '/static/py')
import LD, RD, report, RDstep

app = Flask(__name__)

LuckGlobalRR = yRR = zRR = rRR = DPtmp = 0
LuckGlobal = y = z = r = LDcount = 0
RandListRR = RandList = JoinText_ = JoinTextRR = []

@app.route('/')
def indexMain():
    return render_template("indexMain.html")

@app.route('/openroller/')
def indexOR():
    return render_template(
        "indexOR.html",
        Dices_ = 5,
        Rolls_ = 1,
        Q_ = 0,
    )

@app.route('/openroller/<int:d>/<int:r>/<int:q>')
def CtoO(d, r, q):

    return render_template(
        "indexOR.html",
        Dices_=d,
        Rolls_=r,
        Q_=q,
    )

@app.route('/opencrafter/')
def indexOC():
    return render_template("indexOC.html")

@app.route('/luckdice', methods=['GET', 'POST'])
def luckDice():
    global LDcount
    LDcount += 1
    JoinText = "<h2>["+ str(LDcount) + "] " + LD.chooseLD() + "</h2>"
    return json.dumps({'JoinText': JoinText})

@app.route('/rolldice', methods=['GET', 'POST'])
def rollDice():
    Dices = request.form.get('TEXT_Dices', type=int)
    Rolls = request.form.get('TEXT_Rolls', type=int)
    OM = request.form.get('TEXT_OM', default=0, type=int)
    Q = request.form.get('TEXT_Quality', type=int)
    EText = request.form.get('TEXT_EText', type=str)
    
    if Dices > 50 or Rolls > 50:
        return json.dumps({
            'JoinText': "Слишком большое число, чит0р",
            'finalPush': '',
        })

    try: WP = 1 if request.form['TEXT_WillPower'] == 'on' else 0
    except: WP = 0
    
    try: PUSH = 1 if request.form['TEXT_PUSH'] == 'on' else 0
    except: PUSH = 0

    try: RR = 1 if request.form['TEXT_ReRoll'] == 'on' else 0
    except: RR = 0

    JoinText = RD.roll(Dices, Rolls, OM,
                        Q, WP, RR, EText)

    if EText and not EText.isspace():
        if EText.isdigit() == False:
            report.sending(EText, JoinText)
            
    if PUSH:
        rc = ['s', 'd']
        dicePush = []
        JT = JoinText[:]

        for jt_ in JT:
            jt = str(jt_)
            if jt[0] not in ('И', 'К'): 
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

@app.route('/stepmod', methods=['GET', 'POST'])
def stepMod():
    global LuckGlobalRR, RandListRR, LuckGlobal
    global yRR, zRR, rRR, y, z, r, RandList
    global JoinText_, JoinTextRR, DPtmp
    LuckGlobalRR = yRR = zRR = rRR = 0
    LuckGlobal = y = z = r = DPtmp = 0
    RandListRR = RandList = JoinText_ = JoinTextRR = []

    stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();"/>'
    stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();"/>'
    stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();" disabled/>'
    stepDl = '<input value="Сброс" type="button" onclick="stepDl();"/>'
    fmTextOM = """<td><h4><b>Автоуспех:</b></h4></td>
                      <td><input type="number" min='-10' max='10' value=0 id="TEXT_OM" name="TEXT_OM"></td>"""
    stepReload = '<br><br><a href="/openroller/">Перезагрузить страницу</a>'
    
    return json.dumps({
        'stepRl': stepRl,
        'stepWP': stepWP,
        'stepRR': stepRR,
        'stepDl': stepDl,
        'fmTextOM': fmTextOM,
        'stepReload': stepReload,
    })

@app.route('/step', methods=['GET', 'POST'])
def step():
    global LuckGlobalRR, RandListRR, LuckGlobal
    global yRR, zRR, rRR, y, z, r, RandList
    global JoinText_, JoinTextRR, DPtmp

    sCheck = request.args.get('sCheck')

    if sCheck == 'Dl':
        stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();"/>'
        stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();"/>'
        stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();" disabled/>'
        LuckGlobalRR = yRR = zRR = rRR = 0
        LuckGlobal = y = z = r = DPtmp = 0
        RandListRR = RandList = JoinText_ = JoinTextRR = []
        return json.dumps({
            'stepRl': stepRl,
            'stepWP': stepWP,
            'stepRR': stepRR,
        })   

    Dices = request.form.get('TEXT_Dices', type=int)
    Rolls = request.form.get('TEXT_Rolls', type=int)
    OM = request.form.get('TEXT_OM', type=int)
    Q = request.form.get('TEXT_Quality', type=int)
    EText = request.form.get('TEXT_EText', type=str)

    WP = 1 if sCheck=="WP" else 0
    RR = 1 if sCheck=="RR" else 0

    if sCheck == 'Rl':
        DPtmp = Dices
    elif sCheck == 'RR':
        Dices = DPtmp

    if sCheck=="Rl":
        stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();"/>'
        stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();"/>'
        stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();"/>'
    else:
        stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();"/>'
        stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();"/>'
        stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();" disabled/>'
    
    (JoinText, LuckGlobalRR, yRR, zRR, rRR, RandListRR,
			JoinTextRR, LuckGlobal, y, z, r,
            RandList, JoinText_) = RDstep.rollStep(Dices,
                        Rolls, OM, Q, WP, RR, EText,
                        sCheck, LuckGlobalRR, yRR, zRR, rRR,
                        RandListRR,	LuckGlobal, y, z, r,
                        RandList, JoinText_, JoinTextRR)

    JoinText = "<h2>" + '<br>'.join(JoinText.split('\n')) + "</h2>"

    if y >= Rolls and sCheck != "Rl":
        stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();" disabled/>'
        stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();" disabled/>'
        stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();" disabled/>'        
        JoinText += "<br>END"
        LuckGlobalRR = yRR = zRR = rRR = 0
        LuckGlobal = y = z = r = DPtmp = 0
        RandListRR = RandList = JoinText_ = JoinTextRR = []
    elif y >= Rolls and sCheck == "Rl":
        stepRl = '<input value="Бросок обычный" type="button" onclick="stepRl();" disabled/>'
        stepWP = '<input value="Бросок с +3 Куба" type="button" onclick="stepWP();" disabled/>'
        stepRR = '<input value="Бросок с Перебросом" type="button" onclick="stepRR();"/>'
    return json.dumps({
        'JoinText': JoinText,
        'stepRl': stepRl,
        'stepWP': stepWP,
        'stepRR': stepRR,
    })   

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)