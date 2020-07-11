// From Page 20 of the Algorithms Book (Chapter 1 - Fundamentals)

//------------------------------------------------------------------------------------------------------------
// Countdown
//------------------------------------------------------------------------------------------------------------
// Create a function that accepts a number as an input. Return a new array that counts down by one, from
// the number (as array's 'zeroth' element) down to 0 (as the last element). How long is this array?
//------------------------------------------------------------------------------------------------------------

function countdown(num) {
    let arr = [];
    for (var i = num; i >= 0; i--) {
        arr.push(i);
    }
    console.log(
        "number=" + num + ", new array=[" + arr + "], new array size=" + arr.length
    );
}
console.log("\n**** Countdown ****");
countdown(10);

//------------------------------------------------------------------------------------------------------------
// Print and Return
//------------------------------------------------------------------------------------------------------------
// Function will receive an array with two numbers. Print the first value and return the second.
//------------------------------------------------------------------------------------------------------------

function printAndReturn(arr) {
    console.log("First Number is: ", arr[0]);
    return arr[1];
}
let arr = [3, 4];
console.log("\n**** Print and Return ****");
console.log("arr=[" + arr + "]");
let num = printAndReturn(arr);
console.log("number returned is: " + num);

//------------------------------------------------------------------------------------------------------------
// First Plus Length
//------------------------------------------------------------------------------------------------------------
// Given an array return the sum of the first value in the array, plus the array's length. What happens if
// the array's first value is NOT a number, but a string (like "what?")  or a boolean (like false).
//------------------------------------------------------------------------------------------------------------

function firstPlusLength(arr) {
    return arr[0] + arr.length;
}
console.log("\n**** First Plus Length ****");
arr = [3, 2, 5, 6, 7];
let returnValue = firstPlusLength(arr);
console.log("(1) arr=[" + arr + "], (2) return value=" + returnValue);

// If first array element is a string, and I try to add string with number, number is recast as a string
// and the return value is a string concatenated with another string (the cast number). For example: what?5
arr = ["what?", 3, 4, 7, 9];
returnValue = firstPlusLength(arr);
console.log("(1) arr=[" + arr + "], (2) return value=" + returnValue);

// If first array element is an a boolean (which counts as 1 - false is 0), I get 1 plus the lengh of the array.
arr = [true, 3, 4, 5, 6];
returnValue = firstPlusLength(arr);
console.log("(1) arr=[" + arr + "], (2) return value=" + returnValue);

//------------------------------------------------------------------------------------------------------------
// Values greater than second
//------------------------------------------------------------------------------------------------------------
// For [1,3,5,7,9,13], print values that are greater than it's 2nd value. Return how many values this is.
//------------------------------------------------------------------------------------------------------------

function valuesGreaterThanSecond(arr) {
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > arr[1]) {
            count += 1;
        }
    }
    console.log(
        "There were " +
        count +
        " values greater than the arrays 2nd value (" +
        arr[1] +
        "), in the array[" +
        arr +
        "]"
    );
}

console.log("**** valuesGreaterThanSecond ****");
valuesGreaterThanSecond([1, 3, 5, 7, 9, 13]);

//------------------------------------------------------------------------------------------------------------
// Values greater than second, Generalized
//------------------------------------------------------------------------------------------------------------
// Write a function that accepts an array, and returns a new array with the array values that are greater
// than it's 2nd value. Print how many values this is. What will you do if the array
// is only one element long?
//
// Answer: The array has to have at least 2 elements (if we're going to check it against the other elements
// in the array.
//------------------------------------------------------------------------------------------------------------

function valuesGreaterThanSecondGeneralized(arr) {
    if (arr.length < 2) {
        console.log("The array must have at least 2 elements. Aborting script.");
        return null;
    }

    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > arr[1]) {
            newArr.push(arr[i]);
        }
    }
    console.log(
        "There were " +
        newArr.length +
        " values greater than the 2nd element (" +
        arr[1] +
        ") in the origina array [" +
        arr +
        "]"
    );
}

console.log("**** valuesGreaterThanSecondGeneralized ****");
valuesGreaterThanSecondGeneralized([1, 3, 5, 7, 9, 13]);
// Test with only one element in the array.
valuesGreaterThanSecondGeneralized([1]);

//------------------------------------------------------------------------------------------------------------
// This Length, That Value.
//
// Given two numbers, return array of length num1 with each value num2. Print "Jinx". If they are the same.
//------------------------------------------------------------------------------------------------------------

function thisLengthThatValue(num1, num2) {
    console.log("Jinx! Both numbers are the same. " + num1 + " and " + num2);
    let arr = [];
    for (let i = 0; i < num1; i++) {
        arr.push(num2);
    }
    console.log("num1=" + num1);
    console.log("num2=" + num2);
    return arr;
}

console.log("**** thisLengthThatValue ****");
let array = thisLengthThatValue(4, 9);
console.log("array=[" + array + "]");

array = thisLengthThatValue(4, 4);
console.log("array=[" + array + "]");

//------------------------------------------------------------------------------------------------------------
// Fit the First Value.
//
// Function should accept an array. If value at [0] is greater than array's length, print "Too big@". If
// value at [0] is less than array's length, print "Too small!", otherwise print "Just right!".
//------------------------------------------------------------------------------------------------------------

function fitTheFirstValue(arr) {
    if (arr[0] > arr.length) {
        console.log("Too Big!!");
    } else if (arr[0] < arr.length) {
        console.log("Too Small!!");
    } else {
        console.log("Just Right!!");
    }
}

console.log("**** fitTheFirstValue ****");

array = [3, 4, 5, 1, 3]; // Too Small
fitTheFirstValue(array);

array = [8, 4, 5, 1, 3]; // Too Big
fitTheFirstValue(array);

array = [5, 4, 5, 1, 3]; // Just RIght
fitTheFirstValue(array);

//------------------------------------------------------------------------------------------------------------
// Fahrenheit to Celsius
//
// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees), that accepts.
// a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees.
// For review, Fahrenheit = (9/5 * Celsius) + 32.
//------------------------------------------------------------------------------------------------------------

function fahrenheitToCelsius(fDegrees) {
    return ((fDegrees - 32) * 5) / 9;
}

console.log("**** fahrenheitToCelsius ****");
let fahrenheit = 32;
let celsius = fahrenheitToCelsius(fahrenheit);
console.log("Fahrenheit = " + fahrenheit + " Celsius = " + celsius);

//------------------------------------------------------------------------------------------------------------
// Celsius to Fahrenheit
//
// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius and returns the
// equivalent temperature expressed in Fahrenheit degrees.
//
//------------------------------------------------------------------------------------------------------------

function celsiusToFahrenheit(cDegrees) {
    return (9 / 5) * cDegrees + 32;
}

console.log("**** celsiusToFahrenheit ****");
celius = 0;
fahrenheit = celsiusToFahrenheit(celsius);
console.log("Celsius = " + celsius + ", Fahrenheit = " + fahrenheit);

//------------------------------------------------------------------------------------------------------------
// Optional: Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be
//           complex, so for this challenge just try a series of Celsius integer values starting at 200,
//           going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.
//------------------------------------------------------------------------------------------------------------

for (let celsius = 200; celsius > -200; celsius--) {
    console.log("Celsius = " + celsius);
    fahrenheit = celsiusToFahrenheit(celsius);
    if (celsius === fahrenheit) {
        console.log("********** Celsius and Fahrenheit ARE equal *********");
        console.log(" Celsius = " + celsius + " = Fahrenheit = " + fahrenheit);
        console.log("*****************************************************");
        break;
    }
}
console.log("Done");