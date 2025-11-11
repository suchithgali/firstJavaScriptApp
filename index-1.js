const display = document.getElementById("display");
let current = "", previous = "", op = null, lastOp = null, lastNum = null;

const clearOps = () => document.querySelectorAll(".operator")
  .forEach(btn => btn.classList.remove("active"));

function append(val) {
  if (val === "." && current.includes(".")) return;

  current += val;
  display.value = current;

  clearOps();
}

function setOperation(o, button) {
  if (current && previous && op) calculate();

  if (current || previous) {
    if (current) {
      previous = current;
      current = "";
    }
    op = lastOp = o;

    clearOps();
    button.classList.add("active");
  }
}

function calculate() {
  if (!(op || lastOp)) return;

  let a = parseFloat(previous);
  let b = parseFloat(current || lastNum);

  switch (op || lastOp) {
    case "+": previous = a + b; break;
    case "-": previous = a - b; break;
    case "*": previous = a * b; break;
    case "/": previous = a / b; break;
  }

  display.value = previous;
  previous = previous.toString();

  if (current) lastNum = current;

  current = "";
  op = null;

  clearOps();
}

function clearDisplay() {
  display.value = current = previous = "";
  op = lastOp = lastNum = null;

  clearOps();
}
