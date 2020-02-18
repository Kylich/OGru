function CtoO() {
    alert('C to O');
}
function Other1() {
   $('#Resultat').html("..."); 
}
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
            $('#Resultat').html('Выбери Профу');
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
            $('#Resultat').html('OM должно быть не больше НЗ-1 или ОМ для Ближнего и Дальнего Боя по сумме не равны двойному общему ОМ (ОМ * 2 = ОМ ББ + ОМ ДБ)');
            wrong ++;
        } else {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-ready');
            $('#Resultat').html('');
        }
    } else {
        if (OM > NZ - 1)
        {
            $('fieldset#BluePrintFS').attr('class', 'quitz-card-disable');
            $('#Resultat').html('OM должно быть не больше НЗ-1');
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
        $('#Resultat').html('Ошибка в Требовании, Структуре или Прочности');
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
        $('#Resultat').html('Слишком много ОС');
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
        $('#Resultat').html('ДМ не должно быть больше НЗ');
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
        $('#Resultat').html('Качество не должно быть больше НЗ / 2');
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
        $('#Resultat').html('Отмена Штрафа за ОМ для Ближнего Боя без ОМ для Ближнего Боя');
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
