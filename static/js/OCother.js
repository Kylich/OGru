function Other() {
    if (
        $('fieldset#MasterFS').attr('class') == 'quitz-card-ready'
        &&
        $('fieldset#BluePrintFS').attr('class') == 'quitz-card-ready'
    )
    {
        $('#Resultat').html("...");
        var OY = 0;
        var OYtext = '';
        var DicePull = 0;
        var NumRoll = 0;
        var ProfText = '';

        var TY = +(document.getElementById("fTY").value);
        var R = +(document.getElementById("fR").value);
        var Pch = +(document.getElementById("fPch").value);
        var Tch = +(document.getElementById("fTch").value);
        var OM = +(document.getElementById("fOM").value);
        var OMMT = +(document.getElementById("fOMMT").value);
        var OS = +(document.getElementById("fOS").value);
        var DM = +(document.getElementById("fDM").value);
        var N = +(document.getElementById("fN").value);
        var M = +(document.getElementById("fM").value);
        var INT = +(document.getElementById("fINT").value);
        var Craft = +(document.getElementById("fCraft").value);
        var Since = +(document.getElementById("fSince").value);
        var Comp = +(document.getElementById("fComp").value);
        var Other = +(document.getElementById("fOther").value);
        var Q = +(document.getElementById("fQ").value);
        var KTYC = +(document.getElementById("fKTYC").value);

        Noy = 0, OMoy = 0;
        
        if ( $('#fNA').is(':checked') ) {} else { OMMT = 0 }
        
        if ( N > TY) { Noy = N - TY } else { Noy = 0 }
        
        if ( OM > 0 ) { OMoy = OM + 1 }
        else if ( OM < 0 ) { OMoy = OM - 1 }
        
        OY = Tch + Pch + OS + 2*Q + DM + OMoy + OMMT + Noy;
        
        var Error = false;
        if (OY < 1)
        {
            OYtext = '<h1>ОУ должно быть больше 0 </h1><br>';
            Error = true;
        } else {
            OYtext = '<h1> ОУ = ' + OY + '<br> Требуется Успехов = ' + OY*5 +  '</h1><br><h2>Кол-во ОУ:</h2><h3> Требования изм. = ' + Tch + '\
            <br>Проч-ть изм. = ' + Pch + '<br>Особ. Св-ва = ' + OS + '<br>Кач-во = ' + 2*Q + '<br>Основ. Мод. = ' + OMoy + '\
            <br>ОМ ББ штраф = ' + OMMT + '<br>Назначения = ' + Noy + '<br>Доп. Мод. = ' + DM + '</h3><br><br>';
        }

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

        ProfText = 'Доступные профы: ';
        if ( MeritCraft && ProfCraft ) { ProfText += 'Крафт, ' }
        if ( MeritSince && ProfSince ) { ProfText += 'ТочнНауки, ' }
        if ( MeritComp && ProfComp   ) { ProfText += 'Компы, ' }
        
        if ( ProfText == 'Доступные профы: ' ) {
            ProfText = '';
        } else {
            ProfText = ProfText.slice(0,-2) + '.';
        }
        var Prof = 0
        if (ProfText) {Prof=1}

        /*var WP3 = 0;
        if (
            $('#fWP3').is(':checked')
            &&
            $('#fWP').is(':checked')
        ) { WP3 = 3 }*/

        if ( N == 1 ) { N = 0 } else { N-- }
        
        var DebaffM = '', DebaffCraft = '';
        
        if (M < TY) {DebaffM = 'Мастерская < TY => -успехи';}
        if (Craft < TY) {DebaffCraft = 'Крафт < TY => -успехи';}
        if ( Merit == 0 ) { Merit = -3 }
        
        DicePull = M - N + Merit + INT + Other + KTYC - TY; // + WP3;
        
        var Terp = 0;
        if ($('#fTerp').is(':checked')) {Terp = 2}         
        
        NumRoll = Merit + INT + Terp;
        
        var ItogText = '';
        if (
            Error == false
            &&
            NumRoll <= 0
        ) {
            Error = true;
            OYtext = '<h1>Кол-во Бросков меньше 1</h1><br>';
        }

        if (
            Error == false
            &&
            DicePull <= 0
        ) {
            Error = true;
            OYtext = '<h1>Кол-во Кубов меньше 1</h1><br>';
        }

        var RRtxt='';
        if ( $('#fRR').is(':checked') ) {
            RRtxt = 'ПСВ: Переброс или +3 куба';
        } else {
            RRtxt = 'ПСВ: +3 куба';
        }

        if ( Error ) { ItogText = OYtext } else {
        ItogText = OYtext + '<br>' +  DebaffM + '<br>' + DebaffCraft + '<br>' + '\
        <h1>Кол-во деталей = ' + R*R + '<br>Кол-во Кубов = ' + String(DicePull) + '<br>' + '\
        Кол-во Бросков = ' + String(NumRoll) + '</h1><br><h3>' + ProfText + '<br>' + RRtxt + '</h3>\
        <br><a href="/openroller/' + DicePull + '/' + NumRoll + '/' + Prof + '">Перенести в OpenRoller</a>';

       }
        
        $('#Resultat').html(ItogText);
        $('fieldset#OtherFS').attr('class', 'quitz-card-ready');
    } else {
        $('fieldset#OtherFS').attr('class', 'quitz-card-disable');
        $('#Resultat').html('Сначала проверь формы Мастера и Чертежа');
    }
}
