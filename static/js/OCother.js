function Other() {
    if (
        $('fieldset#MasterFS').attr('class') == 'quitz-card-ready'
        &&
        $('fieldset#BluePrintFS').attr('class') == 'quitz-card-ready'
    )
    {
        var OY = 0;
        var OYtext = '';

        var TY = +(document.getElementById("fTY").value);
        var R = +(document.getElementById("fR").value);
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
        var KTYC = 0, Noy = 0, OMoy = 0;

        if ( $('#fNA').is(':checked') ) { OMMT = OMMT } else { OMMT = 0 }
        
        if ( N > TY) { Noy = N - TY } else { Noy = 0 }
        
        if ( OM > 0 ) { OMoy = OM + 1 }
        else if ( OM < 0 ) { OMoy = OM - 1 }
        
        // !TCh + !PCh + !OM+1  + !N (>TY) + !OS + !Q*2 + !OMMCh + !DM = OY
        OY = Tch + Pch + OS + 2*Q + DM + OMoy + OMMT + Noy;
        
        var Error = false;
        
        if (OY < 1 )
        {
            OYtext = '<h1>ОУ должно быть больше 0 </h1><br>';
            Error = true;
        } else {
            OYtext = '<h1> ОУ = ' + OY + '<br> Требуется Успехов = ' + OY*5 +  '</h1><br><h2>Кол-во ОУ:</h2><h3> Требования изм. = ' + Tch + '\
            <br>Проч-ть изм. = ' + Pch + '<br>Особ. Св-ва = ' + OS + '<br>Кач-во = ' + 2*Q + '<br>Основ. Мод. = ' + OMoy + '\
            <br>ОМ ББ штраф = ' + OMMT + '<br>Назначения = ' + Noy + '<br>Доп. Мод. = ' + DM + '</h3><br><br>';
        }

        /*
        DONE
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
        self.BuffPROFQt.show() if self.MERITchQt.text() in PROFall else self.BuffPROFQt.hide()
        */

        var z = 0, q = false, Prof = false, Merit = 0;
        var MeritCraft = false, MeritSince = false, MeritComp = false;
        var ProfCraft = false, ProfSince = false, ProfComp = false;
        
        if ( $('#fProf').is(':checked') )
            {
                Prof = true;
                if ( $('#fProfCraft').is(':checked') ) { ProfCraft = true }
                if ( $('#fProfSince').is(':checked') ) { ProfSince = true }
                if ( $('#fProfComp') .is(':checked') ) { ProfComp  = true }
            }
        
        if ( TY <= 3 ) {
                Merit = Craft;
                MeritCraft = true;
        }

        else if ( TY == 4 ) {
            while (true) {
                if ( Craft == z ) {
                    Merit = Craft;
                    MeritCraft = true;
                    q = true;
                }
                
                if ( Since == z ) {
                    Merit = Since;
                    MeritSince = true;
                    q = true;
                }
                
                if (q) {break}
                z++;
            }
        }
      
        else {
            while (true) {
                if ( Craft == z ) {
                    Merit = Craft;
                    MeritCraft = true;
                    q = true;
                }
                
                if ( Since == z ) {
                    Merit = Since;
                    MeritSince = true;
                    q = true;
                }
                
                if ( Comp == z ) {
                    Merit = Comp;
                    MeritComp = true;
                    q = true;
                }
                
                if (q) {break}
                z++;
            }
        }
        
        var ProfText = 'Доступные профы: ';
        
        if ( MeritCraft && ProfCraft ) { ProfText += 'Крафт, ' }
        if ( MeritSince && ProfSince ) { ProfText += 'ТочнНауки, ' }
        if ( MeritComp && ProfComp   ) { ProfText += 'Компы, ' }
        
        if ( ProfText == 'Доступные профы: ' ) {
            ProfText = '';
        } else {
            ProfText = ProfText.slice(0,-2) + '.';
        }


        /* 
        M    = self.MQt.value()
        N    = self.NQt.value()
        MERIT= self.MERITQt.value()
        TY   = self.TYQt.value()
        INT  = self.INTQt.value()
        CRFT = self.CRFTQt.value()
        Other= self.OtherQt.value()

        KTYC = 1 if self.KTYCQt.isChecked() else 0

        if N==1: N = 0
        else: N -= 1

        if M < TY:
            self.DebaffMQt.show()
        else:
            self.DebaffMQt.hide()

        if CRFT < TY:
            self.DebaffCRFTQt.show()
        else:
            self.DebaffCRFTQt.hide()
        
        if MERIT == 0: MERIT = -3
        DicePull = M - N + MERIT + INT + Other + KTYC - TY
        */
        

        if (
            $('#fKTYC').is(':checked')
            &&
            R > 1
            &&
            TY < 7
            ) { KTYC = 1 }

        if ( N == 1 ) { N = 0 } else { N-- }        
        
        var DebaffM = '', DebaffCraft = '';
        
        if ( M < TY ) {
            DebaffM = 'Мастерская < TY => -успехи';
        }
        
        if ( Craft < TY ) {
            DebaffCraft = 'Крафт < TY => -успехи';
        }
        
        if (Merit == 0) {Merit = -3}
        
        var DicePull = M - N + Merit + INT + Other + KTYC - TY;

        var Terp = 0, NumRoll = 0;
        if ($('#fTerp').is(':checked')) {Terp = 2}         
        
        NumRoll = Merit + INT + Terp;
        
        var ItogText = '';
        
        if ( Error ) { ItogText = OYtext } else {
        ItogText = OYtext + ProfText + '<br>' +  DebaffM + '<br>' + DebaffCraft + '<br>' + '\
        <h1>Кол-во деталей = '+ R*R + '<br>Кол-во Кубов = ' + String(DicePull) + '<br>' + 'Кол-во Бросков = ' + String(NumRoll) + '</h1>';
        }
        
        $('#Resultat').html(ItogText);
        $('fieldset#OtherFS').attr('class', 'quitz-card-ready');
    } else {
        $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('Сначала проверь формы Мастера и Чертежа');
    }
}