
CalcEvenListener=()=>{

    document.querySelectorAll('.calc_button').forEach((BUTTON)=>{
        BUTTON.addEventListener('click',()=>UpdateScreen(BUTTON.value))
    })
}

function UpdateScreen(Button_value) {

    const CalcScreen = document.querySelector('#calc_screen');
    let tempvalue=CalcScreen.value+Button_value;
    if(Button_value==='AC'){

        tempvalue='';

    }
    else if(Button_value === 'Del'){

        let tempScreenArray = (CalcScreen.value).split('')
        tempScreenArray.splice(-1,1);
        tempvalue = tempScreenArray.join('');

    }
    else if(Button_value === '='){

        tempvalue = String(eval(CalcScreen.value));
        localStorage.setItem('CalcAns',tempvalue);
    }
    else if(Button_value === 'Ans'){
        const Prev_Answer =localStorage.getItem('CalcAns') || '0';
        tempvalue= CalcScreen.value + Prev_Answer;
    }

    CalcScreen.value = tempvalue;

}

CalcEvenListener();