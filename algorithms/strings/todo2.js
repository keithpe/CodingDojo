//****************************************************************************
// Reverse
//****************************************************************************
// Implement reverseString(str) that, given string, returns that string 
// with characters reversed.
//
// Given "creature", return "erutaerc". 
// Tempting as it seems, do not use the built-in reverse()!
//****************************************************************************

function reverseString(str) {

    let newStr = '';
    for (let idx = str.length - 1; idx >= 0; idx--) {
        newStr += str[idx]
    }
    return newStr
}

console.log("\n**** Reverse String ****")
str = 'creature'
console.log('original string:', str)
str = reverseString(str)
console.log('modified string:', str)


//****************************************************************************
// Remove Even-Length Strings
//****************************************************************************
// Build a standalone function to remove strings of even lengths from a 
// given array. 
// For array containing ["Nope!","Its","Kris","starting","with","K!",
// "(instead","of","Chris","with","C)","."], 
// change that same array to ["Nope!","Its","Chris","."].
//****************************************************************************

function removeEvenLengthStrings(arr) {

    let newArr = []

    for (let idx = 0; idx < arr.length; idx++) {
        if (arr[idx].length % 2 != 0) {
            newArr.push(arr[idx])
        }
    }
    return newArr
}


console.log("\n**** Remove Even-Length Strings ****")
arr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."]
console.log('original array:', arr)
arr = removeEvenLengthStrings(arr)
console.log('modified array:', arr)


//****************************************************************************
// Integer to Roman Numerals
//****************************************************************************
// Given a positive integer that is less than 4000, return a string 
// containing that value in Roman numeral representation. 
// In this representation, I is 1, V is 5, X is 10, L = 50, C = 100, D = 500, 
// and M = 1000. Remember that 4 is IV, 349 is CCCIL and 444 is CDXLIV.
//****************************************************************************

function integerToRomanNumerals(num) {

    let romanNum = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    let decimalNum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    if (num <= 0) {
        return num;
    }

    let romanNumeral = "";

    // Loop through all roman numerals (from largest to smallest )
    for (let idx = 0; idx < romanNum.length; idx++) {

        while (num >= decimalNum[idx]) {
            num -= decimalNum[idx];
            romanNumeral += romanNum[idx];
        }
    }
    return romanNumeral;
}


console.log("\n**** Integer to Roman Numerals ****")
let num = 425;
num = 349;
num = 444;
let roman_numerals = integerToRomanNumerals(num)
console.log(num + ' decimal is ' + roman_numerals + ' in roman numerals')