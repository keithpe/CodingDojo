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