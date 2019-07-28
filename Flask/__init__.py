from flask import Flask, render_template, request, json
import sys, os, random #, time

app = Flask(__name__)
f = open('//tmp//restart.txt', 'w')
f.close()
# /home/f/f950220q/open-gamer.ru

@app.route('/')
def indexMain():
    return render_template("indexMain.html")
    
#@app.route('/pom')
#def indexPom():
#    popPhoto=False
#    ending=False
#    
#    return render_template('indexPom.html', popPhoto=popPhoto, ending=ending)
#    
#@app.route('/<choosePhoto>/<string:popPhoto>/')
#def indexPomCh(choosePhoto, popPhoto):
#    
#    if len(popPhoto) <= 9:
#        ending=True
#        popPhoto = popPhoto.split('&')
#        popPhoto.remove(choosePhoto)
#        popPhoto = str(popPhoto)
#        popPhoto=popPhoto[2:5]
#        import report
#        report.sending(popPhoto, popPhoto)
#        return render_template('indexPom.html', popPhoto=popPhoto, ending=ending)
#        
#    ending=False
#    if choosePhoto == '000':
#        spam = list(range(2, 132))
#        popPhoto=['001']
#        for s in spam:
#            if s//10 < 1:
#                f='00'+str(s)
#            elif s//10 in range(1,10):
#                f='0'+str(s)
#            else: f = str(s)
#            popPhoto.append(f)
#    else:
#        popPhoto = popPhoto.split('&')
#        popPhoto.remove(choosePhoto)
#        
#    p1=random.choice(popPhoto)
#    
#    while True:
#        p2=random.choice(popPhoto)
#        if p1==p2:
#            p2=random.choice(popPhoto)
#        else: break
#    
#    popPhoto = '&'.join(popPhoto)
#    
#    return render_template('indexPom.html', p1=p1, p2=p2, popPhoto=popPhoto)

#@app.route('/openpoints')
#def indexOP():
#    return render_template('indexOP.html')

@app.route('/openroller/')
def indexOR():
    return render_template("indexOR.html")

@app.route('/opencrafter/')
def indexOC():
    return render_template("indexOC.html")

@app.route('/FullMod', methods=['GET', 'POST'])
def indexFull():
    fmCheck = int(request.args.get('fmCheck'))
    
    if fmCheck % 2 == 0:
        fmTextPerk = """
                    <td><b>Перк:</b></td>
                    <td><input name="TEXT_ReRoll" id="TEXT_ReRoll" type="checkbox"/></td>
                """
        fmTextPush = """
                    <td><b><FONT color=green>Кнопка только для Пушистой, никому больше не нажимать!</font></b></td>
                    <td><input name="TEXT_PUSH" id="TEXT_PUSH" type="checkbox"/></td>
                """
        fmTextOM = """
                    <td><h4><b>Автоуспех:</b></h4></td>
                    <td><input type="number" min='-10' max='10' value=0 id="TEXT_OM" name="TEXT_OM"></td>
                """
    else:
        fmTextPerk=''
        fmTextPush=''
        fmTextOM=''
        
    return json.dumps({'fmTextPerk': fmTextPerk, 'fmTextPush': fmTextPush, 'fmTextOM': fmTextOM})

@app.route('/LuckDice', methods=['GET', 'POST'])
def LuckDice():
    import LD
    JoinText = "<h2>" + LD.chooseLD() + "</h2>"
    return json.dumps({'JoinText': JoinText})
    
@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():
    
    tutCheck = int(request.args.get('tutCheck'))
    
    if tutCheck % 2 == 0:
        tutText="""
            <h1><b>Информация по использованию:</b></h1>
            <p><b>Кол-во Кубов</b> - то, сколько кубов на броске - атрибуты, навыки, модификаторы, ДМ, и т.д. НО (!) без учета ПСВ</p>
            <p><b>Кол-во Бросков</b> - то, сколько раз бросать для Продолжительного Броска</p>
            <p><b>Переброс</b> - то, какие кубы перебрасываются ("взрываются", профа, качество, и т.д.)</p>
            <p><b>ПСВ</b> - тратишь ли ты ПСВ на все броски (отдельныя трата ПСВ на каждый бросок на Продолжительном Броске в разработке)</p>
            <p><b>Перк</b> - если да, то тратишь ПСВ на переброс всех неудачных кубов на броске; если нет - то +3 куба</p>
            <p><b>Автоуспех</b> - то, сколько добавляется/вычитается успехов на удачном броске (ОМ, контест и т.д.)</p>
            <p><b>Текст отчета</b> - укажите мастера, персонажа, дайспул и/или заявку - ту инфу, по которой будет понятно, какой этот бросок</p>
            <p><b>Куб Удачи</b> - верь, надейся и кидай. У тебя все получится!</p>

            <b>Результаты броска:</b><br>
            <b>[X]</b> - номер броска<br>
            <b>(X)</b> - переброшенный куб за перк<br>
            <b>X</b> - выпавший кубик<br>
            <b>:</b> - переброшенные кубики<br>
            <b>---> X</b> - результат броска (>0 - успехи, <0 - драмат, =0 - провал)<br>
            <b>~~~ X ~~~</b> - итоговый результат<br><br>
            Кубов:5 Бросков:5 ПСВ:да Переброс:(0, 9) Перк:да<br>
            [1] (4) 1 - (1) 4 - (3) 3 - (2) 6 - (6) 1 ---> -2<br>
            [2] 0 - (2) 3 - 9 - (5) 1 - (3) 6 : (4) 5 - (6) 5 ---> 2<br>
            [3] (1) 1 - (2) 1 - (1) 3 - (6) 0 - (4) 6 : 6 ---> -2<br>
            [4] 9 - (4) 9 - (7) 3 - (7) 7 - 8 : (1) 6 - 4 ---> 3<br>
            [5] (4) 1 - (6) 2 - 0 - 0 - 0 : 9 - 9 - 0 - (7) 8 - (4) 7 - 8 ---> 12<br>
            ~~~ 13 ~~~<br>
            <h1><b>Известные различия с текстовыми правилами:</b></h1>
            <p><b>1)</b> Ужасное Качество вычитает один Успех из общего кол-ва Успехов, но должен вычитать кол-во Единиц, и жесткая система учета Драмата</p>
            <p><b>2)</b> Драмат на Длительном Броске вычитает из общего кол-ва Успехов кол-во Единиц, но должен прерывать бросок полностью</p>
            <p><b>3)</b> Отсутствие Успехов на одном из Бросков на Длительном броске ничего не делает, но должен уменьшать кол-во Кубов на 1 на последующие броски</p>
            <p>Если вы нашли еще ошибки или есть предложения по улучшению, <a href="https://vk.com/kylikov_nikita">пишите в VK</a></p>
            """
    else:
        tutText=''
    
    return json.dumps({'tutText': tutText})

@app.route('/RollDice', methods=['GET', 'POST'])
def RollDice():

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
    except: TEXT_EText = ''
    
    import RD
    JoinText, DetalText = RD.roll(TEXT_Dices, TEXT_Rolls, TEXT_OM, TEXT_Q, TEXT_WP, TEXT_RR, TEXT_EText)

    #send report
    if TEXT_EText and not TEXT_EText.isspace():
        if TEXT_EText.isdigit() == False:
            import report
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
        
        finalpush=[]
        for dice in dicepush:
            finalpush.append('<img src="/static/images/dicepush/%s.gif"/>' % dice)
        
    else: finalpush=''
    
    JoinText = "<br>".join(JoinText)
    JoinText ="<h2>" + JoinText + "</h2>"
    
    
    return json.dumps({'JoinText': JoinText, 'finalpush': finalpush})
    #return render_template("indexOR.html", result=JoinText, dicepush=dicepush,
    #    PUSH=TEXT_PUSH, TEXT_Dices=TEXT_Dices, TEXT_RR=TEXT_RR, fullmod = fullmod,
    #    TEXT_Rolls=TEXT_Rolls, TEXT_Q=TEXT_Q, TEXT_WP=TEXT_WP, TEXT_OM=TEXT_OM)
    
    #@app.route("/ctime")
    #def ctime():
    #    ctime=str("<h2>Time is: " + time.ctime(time.time())+"</h2>")
    #    return ctime
        
if __name__ == '__main__':
    app.run(debug=True)
