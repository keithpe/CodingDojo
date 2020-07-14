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