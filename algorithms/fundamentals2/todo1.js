//****************************************************************************
// Sigma
//****************************************************************************
// Implement function sigma(num) that given a number, returns the sum of 
// all positive integers up to number (inclusive). 
// Ex.: sigma(3) = 6 (or 1 + 2 + 3); sigma(5) = 15 (or 1 + 2 + 3 + 4 + 5).
//****************************************************************************

function sigma(num) {
    let sum = 0;
    for (let idx = 1; idx <= num; idx++) {
        sum += idx;
    }

    return sum;
}

console.log("\n**** Sigma ****")
let num = 3;
let sum = sigma(num)
console.log("sigma(" + num + ") is: " + sum)
num = 5;
sum = sigma(num)
console.log("sigma(" + num + ") is: " + sum)


//****************************************************************************
// Factorial
//****************************************************************************
// Just the Facts, ma’am. Factorials, that is. Write a function factorial(num) 
// that, given a number, returns the product (multiplication) of all positive 
// integers from 1 up to number (inclusive). 
//
// For example, factorial(3) = 6 (or 1 * 2 * 3); 
// factorial(5) = 120 (or 1 * 2 * 3 * 4 * 5).
//****************************************************************************

function factorial(num) {
    let factorial = 1;
    for (let idx = 1; idx <= num; idx++) {
        factorial *= idx
    }
    return factorial
}

console.log("\n**** Factorial ****")
num = 3;
let factorial_val = factorial(num);
console.log("factorial(" + num + ") is: " + factorial_val)
num = 5
factorial_val = factorial(num);
console.log("factorial(" + num + ") is: " + factorial_val)



//****************************************************************************
// Star Art
//****************************************************************************
//
// Assume that you have a text field that is exactly 75 characters long. 
// You want to fill it with spaces and asterisks ('*'), sometimes called 
// stars. 
//
// You should print the given number of asterisks consecutively. 
// 
// Depending on which function is called, those stars should be left-justified 
// (the first star would be very first char in the text field), or 
// right-justified (the last star would be very last char in the text field, 
// with potentially some number of spaces at beginning of text field before 
// the block of stars start), or centered in the 75-character text field 
// (with the same number of spaces on either side of the block of stars, 
// plus/minus one).
//
//****************************************************************************
// 
// Write a function drawLeftStars(num) that accepts a number and prints 
// that many asterisks.
// 
// Write a function drawRightStars(num) that prints 75 characters total. 
// Stars should build from the right side. The last num characters should be 
// asterisks; the other 75 should be spaces.   
// 
// Write function drawCenteredStars(num) that prints 75 characters total. 
// The stars should be centered in the 75. The middle num characters should 
// be asterisks; the rest of the 75 spaces.
//
// (Optional) Create epic text-art Empire vs. Rebellion battle scenes, 
// with ships like (=*=)and >o<.
// 
//****************************************************************************

function drawLeftStars(num) {
    let line = ''
    for (let idx = 0; idx < num; idx++) {
        line += '*'
    }
    console.log(line)
}

function drawRightStars(num) {
    let line = ''
    for (let idx = 0; idx < 75 - num; idx++) {
        line += ' '
    }
    for (let idx = 0; idx < num; idx++) {
        line += '*'
    }
    console.log(line)
}

function drawCenterStars(num) {
    let line = ''
    // Leftmost spaces
    for (let idx = 0; idx < (75 - num) / 2; idx++) {
        line += ' '
    }
    // Then the asterisks
    for (let idx = 0; idx < num; idx++) {
        line += '*'
    }
    console.log(line)
}

console.log("\n**** Stars ****")
console.log('|--------*---------*---------*---------*---------*---------*---------*----|')
drawLeftStars(25)
drawCenterStars(25)
drawRightStars(25)