function Master() {
    if ($('#fProf').is(':checked'))
    {
        if (
            $('#fProfCraft').is(':checked')
            ||
            $('#fProfSince').is(':checked')
            ||
            $('#fProfComp').is(':checked')
        )
        {
            $('fieldset#MasterFS').attr('class', 'quitz-card-ready');
            $('#Resultat').html('');
        } else {    
            $('fieldset#MasterFS').attr('class', 'quitz-card-disable');
            $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
            $('#Resultat').html('no Prof checked');
        }
    } else {
        $('fieldset#MasterFS').attr('class', 'quitz-card-ready');
    }
    if (
        $('fieldset#MasterFS').attr('class') == 'quitz-card-ready'
        &&
        $('fieldset#BluePrintFS').attr('class') == 'quitz-card-ready'
    )
    {
        $('fieldset#OtherFS').attr('class', 'quitz-card-question');
    } else {
        $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
    }
}

function BluePrint() {
    var P = +(document.getElementById("fP").value);
    var T = +(document.getElementById("fT").value);
    var S = +(document.getElementById("fS").value);
    var OM = +(document.getElementById("fOM").value);
    var NZ = +(document.getElementById("fNZ").value);
    var OMM = +(document.getElementById("fOMM").value);
    var OMR = +(document.getElementById("fOMR").value);
    var OMMT = +(document.getElementById("fOMMT").value);
    var OS = +(document.getElementById("fOS").value);
    var DM = +(document.getElementById("fDM").value);
    var Q = +(document.getElementById("fQ").value);
    var wrong = 0;
    
    if (DM<0) {DM=-DM}
    if (Q<0) {Q=-Q}

    if ($('#fNA').is(':checked'))
    {
        if (
            2 * OM != OMM + OMR
            ||
            OM > NZ - 1
        )
        {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
            $('#Resultat').html('OM != NZ-1 or 2 * OM != OMM + OMR');
            wrong ++;
        } else {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
            $('#Resultat').html('');
        }
    } else {
        if (OM > NZ - 1)
        {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
            $('#Resultat').html('OM != NZ-1');
            wrong ++;
        } else {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
            $('#Resultat').html('');
        }
    }

    if (!wrong)
    {if (
        T > 0
        &&
        P >= 0
        &&
        S > 0
    )
    {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
        $('#Resultat').html('');
    } else {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('T, P or S wrong');
        wrong ++;
    }}
    
    if (!wrong)
    {if (
        NZ*NZ >= OS
    )
    {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
        $('#Resultat').html('');
    } else {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('NZ*NZ &lt; OS wrong');
        wrong ++;
    }}
    
    if (!wrong)
    {if (
        NZ >= DM
    )
    {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
        $('#Resultat').html('');
    } else {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('NZ &lt; |DM| wrong');
        wrong ++;
    }}
    
    
    if (!wrong)
    {if (
        NZ/2 >= Q
    )
    {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
        $('#Resultat').html('');
    } else {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('NZ/2 &lt; |Q| wrong');
        wrong ++;
    }}
    
    if (!wrong)
    {if (
        OMMT <= OMM
    )
    {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
        $('#Resultat').html('');
    } else {
        $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('OMM &lt; OMMT wrong');
        wrong ++;
    }}
    
    if (
        $('fieldset#MasterFS').attr('class') == 'quitz-card-ready'
        &&
        $('fieldset#BluePrintFS').attr('class') == 'quitz-card-ready'
    )
    {
        $('fieldset#OtherFS').attr('class', 'quitz-card-question');
    } else {
        $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
    }
}
    
function Other() {
    if (
        $('fieldset#MasterFS').attr('class') == 'quitz-card-ready'
        &&
        $('fieldset#BluePrintFS').attr('class') == 'quitz-card-ready'
    )
    {
        var OY = 0;
        var OYtext = '';
        var MERIT = 0;
        var TY = +(document.getElementById("fTY").value);
        var Pch = +(document.getElementById("fPch").value);
        var Tch = +(document.getElementById("fTch").value);
        var OM = +(document.getElementById("fOM").value);
        var OMMT = +(document.getElementById("fOMMT").value);
        var OS = +(document.getElementById("fOS").value);
        var DM = +(document.getElementById("fDM").value);
        var N = +(document.getElementById("fN").value);
        var Q = +(document.getElementById("fQ").value);
        var M = +(document.getElementById("fM").value);
        var INT = +(document.getElementById("fINT").value);
        var Craft = +(document.getElementById("fCraft").value);
        var Since = +(document.getElementById("fSince").value);
        var Comp = +(document.getElementById("fComp").value);
        var Other = +(document.getElementById("fOther").value);
        var KTYC = 0;
        
        if ( $('#fKTYC').is(':checked') ) { KTYC = 1 }
        if ( $('#fNA').not(':checked') ) { OMMT = 0 }
        
        if ( N > TY) { N = N - TY } else { N = 0 }
        
        if ( OM > 0 ) { OM = OM + 1 }
        else if ( OM < 0 ) { OM = OM - 1 }
        
        // !TCh + !PCh + !OM+1  + !N (>TY) + !OS + !Q*2 + !OMMCh + !DM = OY
        OY = Tch + Pch + OS + 2*Q + DM + OM + OMMT + N;
        
        if (OY < 1 )
        {
            OYtext = 'OY <= 0 wrong'
        } else {
            OYtext = '<h1> OY = ' + OY + '</h1><br><h3> Tch = ' + Tch + ', \
            Pch = ' + Pch + ', OS = ' + OS + ', Q = ' + 2*Q + ', OM = ' + OM + ', \
            OMMT = ' + OMMT + ', N = ' + N + ', DM = ' + DM + '</h3>'
        }
        
        if(N==1){N=0}else{N--}        
        
        
        /*
        M    = self.MQt.value()
        N    = self.NQt.value()
        MERIT= self.MERITQt.value()
        TY   = self.TYQt.value()
        INT  = self.INTQt.value()
        CRFT = self.CRFTQt.value()
        Other= self.OtherQt.value()

        if M < TY:
            self.DebaffMQt.show()
        else:
            self.DebaffMQt.hide()

        if CRFT < TY:
            self.DebaffCRFTQt.show()
        else:
            self.DebaffCRFTQt.hide()

        KTYC = 1 if self.KTYCQt.isChecked() else 0

        if N==1: N = 0
        else: N -= 1

        if MERIT == 0: MERIT = -3

        DicePull = M - N + MERIT + INT + Other + KTYC - TY
        */
        
        
        var z = 0;
        var q = false;
        var MeritCraft = false, MeritSince = false, MeritComp = false;
        var ProfCraft = false, ProfSince = false, ProfComp = false;
        
        
        
        /*
        if self.PCRFTQt.isChecked():
            PROFall.append('CRFT')
        if self.PSINCQt.isChecked():
            PROFall.append('SINC')
        if self.PCOMPQt.isChecked():
            PROFall.append('COMP')
        self.MERITchQt.clear()

        if TY <= 3:
            self.MERITchQt.setText('CRFT')
            self.MERITQt.setValue(CRFT)
        elif TY == 4:
            while True:
                if CRFT == z:
                    MeritList.append('CRFT')
                    q = True
                if SINC == z:
                    MeritList.append('SINC')
                    q = True 
                if q: break
                z += 1
            q2 = False
            while True:
                if q2: break
                for i in MeritList:
                    if i in PROFall:
                        self.MERITchQt.setText(i)
                        if i == 'CRFT':
                            self.MERITQt.setValue(CRFT)
                        else:
                            self.MERITQt.setValue(SINC)
                        q2 = True
                if self.MERITchQt.text()=='':
                    self.MERITchQt.setText(MeritList[0])
                if self.MERITchQt.text() == 'CRFT':
                    self.MERITQt.setValue(CRFT)
                else:
                    self.MERITQt.setValue(SINC)
                q2 = True
        else:
            while True:
                if CRFT == z:
                    MeritList.append('CRFT')
                    q = True
                if SINC == z:
                    MeritList.append('SINC')
                    q = True
                if COMP == z:
                    MeritList.append('COMP')
                    q = True
                if q: break
                z += 1
            q2 = False
            while True:
                if q2: break
                for x in MeritList:
                    if x in PROFall:
                        self.MERITchQt.setText(x)
                        if x == 'CRFT':
                            self.MERITQt.setValue(CRFT)
                        elif x == 'SINC':
                            self.MERITQt.setValue(SINC)
                        else:
                            self.MERITQt.setValue(COMP)
                        q2 = True
                if self.MERITchQt.text() == '':
                    self.MERITchQt.setText(MeritList[0])
                if self.MERITchQt.text() == 'CRFT':
                    self.MERITQt.setValue(CRFT)
                elif self.MERITchQt.text() == 'COMP':
                    self.MERITQt.setValue(COMP)
                else:
                    self.MERITQt.setValue(SINC)
                q2 = True
        self.BuffPROFQt.show() if self.MERITchQt.text() in PROFall else self.BuffPROFQt.hide()
        */
        
        
        
        $('#Resultat').html(OYtext);
        $('fieldset#OtherFS').attr('class', 'quitz-card-ready');
    } else {
        $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
    }
}

function OtherFS_Q() {
    $('fieldset#OtherFS').attr('class', 'quitz-card-question');
}
function BluePrintFS_Q() {
    $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
    $('fieldset#BluePrintFS').attr('class', 'quitz-card-question');
}
function MasterFS_Q() {
    $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
    $('fieldset#MasterFS').attr('class', 'quitz-card-question');
}

function NZch() {
    var NZ = 0;
    var TY = +(document.getElementById("fTY").value);
    var R = +(document.getElementById("fR").value);
    if (TY > R) {NZ = R;} else {NZ = TY;}
    document.getElementById('fNZ').value = NZ;
}

function Tch() {
    var NZ = 0, T = '';
    var TY = +(document.getElementById("fTY").value);
    var R = +(document.getElementById("fR").value);
    var Tch =  +(document.getElementById("fTch").value);
    
    if (TY > R) {NZ = R;} else {NZ = TY;}
    T = NZ - Tch;

    document.getElementById('fT').value = T;
}

function Pch() {
    
    var P = Math.floor(+(document.getElementById("fTY").value)/2);
    var Pch = +(document.getElementById("fPch").value);
    var R = +(document.getElementById("fR").value);
    
    document.getElementById('fP').value = P + Pch;
    document.getElementById('fS').value = P + Pch + R;
}