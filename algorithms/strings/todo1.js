//****************************************************************************
// Remove Blanks
//****************************************************************************
// Create a function that, given a string, returns all of that string’s 
// contents, but without blanks. 
// 
// If given the string " Pl ayTha tF u nkyM usi c ", 
// return "PlayThatFunkyMusic".
//****************************************************************************

function removeBlanks(str) {

    newstr = ''
    for (let idx = 0; idx < str.length; idx++) {
        if (str[idx] != ' ') {
            newstr += str[idx];
        }
    }
    return newstr
}
console.log("\n**** Remove Blanks ****")
console.log(removeBlanks("P  la   y tha t fu  nky  m u si  c"))


//****************************************************************************
// Get Digits
//****************************************************************************
// Create a JavaScript function that given a string, returns the integer 
// made from the string’s digits. 
// Given "0s1a3y5w7h9a2t4?6!8?0", the function should return 
// the number 1357924680.
//****************************************************************************

function getDigits(str) {

    // Store our 'converted' int here
    myInt = 0;

    for (let idx = 0; idx < str.length; idx++) {

        // Is this character a number? If yes than convert it to int
        if (str.charCodeAt(idx) >= 48 && str.charCodeAt(idx) <= 57) {

            // Shift the number to the left by one, so we can add the next number to it
            myInt = myInt * 10

            // Get the int value of this string char (48 is ascii for the number 0)
            // 48 - 48 is 0, the int representation of ascii 48.
            myInt += str.charCodeAt(idx) - 48;

        }
    }
    // console.log('myInt=', myInt);
    return myInt
}

console.log("\n**** Get Digits ****")
let str = '0s1a3y5w7h9a2t4?6!8?0'
let myInt = 0;

myInt = getDigits(str)
console.log(str + ' converts to ' + myInt)

//****************************************************************************
// Acronyms
//****************************************************************************
// Create a function that, given a string, returns the string’s acronym 
// (first letters only, capitalized). 
// 
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
// 
// Given "Live from New York, it's Saturday Night!", return "LFNYISN".
//****************************************************************************

function acronyms(str) {

    let newstr = '';
    for (let idx = 0; idx < str.length; idx++) {

        // Skip over any spaces until we get to a letter
        while (str[idx] == ' ' && idx < str.length) {
            idx++
        }

        // Store the letter, in uppercase as the next letter in the acronym
        newstr += str[idx].toUpperCase()

        // Skip over any non blank characters until we get to a space
        while (str[idx] != ' ' && idx < str.length) {
            idx++
        }
    }

    return newstr
}


console.log("\n**** Acronyms ****")
str = " there's no free lunch - gotta pay yer way. "
myAcronym = acronyms(str);
console.log('TEST1: The acronym for "' + str + '" is ' + myAcronym)

str = "Live from New York, it's Saturday Night!"
myAcronym = acronyms(str)
console.log('TEST2: The acronym for "' + str + '" is ' + myAcronym)


//****************************************************************************
// Count Non-Spaces
//****************************************************************************
// Accept a string and return the number of non-space characters found 
// in the string. 
//
// For example, given "Honey pie, you are driving me crazy", 
// return 29 (not 35).
//****************************************************************************

function countNonSpaces(str) {
    let non_space_characters = 0;
    for (let idx = 0; idx < str.length; idx++) {
        if (str[idx] != ' ') {
            non_space_characters++;
        }
    }
    return non_space_characters;
}


console.log("\n**** Count Non-Spaces ****")
str = "Honey pie, you are driving me crazy"
let count = countNonSpaces(str)
console.log('Given: "' + str + '", the count is ' + count)


//****************************************************************************
// Remove Shorter Strings
//****************************************************************************
// Given a string array and value (length), remove any strings shorter than 
// the length from the array.
//****************************************************************************

function removeShorterStrings(strArr, length) {

    let newStrArr = []
    for (let idx = 0; idx < stringArray.length; idx++) {
        if (strArr[idx].length >= length) {
            newStrArr.push(strArr[idx])
        }
    }
    return newStrArr

}


console.log("\n**** removeShortStrings ****")
let stringArray = ['My', 'Name', 'is', 'Bertram']
console.log('Original String Array:', stringArray)
stringArray = removeShorterStrings(stringArray, 5)
console.log('Modified String Array:', stringArray)