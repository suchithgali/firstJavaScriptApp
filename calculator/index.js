const display = document.getElementById("display");
let current = "", firstNum = "", previousNum = "", operation = null;

function append(val){
    current += val;
    display.value = current;
    previousNum = current;
}


function clearDisplay(){
    current = "";
    firstNum = "";
    previousNum = "";
    operation = null;
    lastOp = null;
    display.value = current;
}

function setOperation(op, button){
    if(current && firstNum && operation){
        calculate();
    }

    if (current){
        firstNum = current;
        current = "";
        operation = op;
        lastOp = op;
    }
}

function calculate(){
    if (operation){
        let result;
        if (operation === '+'){
            result = parseFloat(firstNum) + parseFloat(current);
        }
        if (operation === '-'){
            result = parseFloat(firstNum) - parseFloat(current);
        }
        if (operation === '*'){
            result = parseFloat(firstNum) * parseFloat(current);
        }
        if (operation === '/'){
            result = parseFloat(firstNum) / parseFloat(current);
        }
        display.value = result;
        current = result.toString();
        firstNum = previousNum;
        operation = null;
    } else if (lastOp){
        let result;
        if (lastOp === '+'){
            result = parseFloat(current) + parseFloat(previousNum);
        }
        if (lastOp === '-'){
            result = parseFloat(current) - parseFloat(previousNum);
        }
        if (lastOp === '*'){
            result = parseFloat(current) * parseFloat(previousNum);
        }
        if (lastOp === '/'){
            result = parseFloat(current) / parseFloat(previousNum);
        }
        display.value = result;
        current = result.toString();
    }
}


