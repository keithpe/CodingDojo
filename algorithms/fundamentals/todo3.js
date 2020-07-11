//----------------------------------------------------------------------------
// Biggie Size
//----------------------------------------------------------------------------
// Given an array, write a function that changes all positive numbers in 
// the array to “big”. 
// Example: makeItBig([-1,3,5,-5]) returns that same array, 
// changed to [-1,"big","big",-5].
//----------------------------------------------------------------------------

function biggieSize(arr) {
    for (var idx = 0; idx < arr.length; idx++) {
        if (arr[idx] > 0) {
            arr[idx] = "big"
        }
    }
}
var arr = [-1, 3, 5, -5]
console.log("\n**** BiggieSize ****")
console.log('before:', arr)
arr = biggieSize(arr)
console.log('after:', arr)


//----------------------------------------------------------------------------
// Print Low, Return High
//----------------------------------------------------------------------------
// Create a function that takes an array of numbers. The function should 
// print the lowest value in the array, and return the highest value in 
// the array.
//----------------------------------------------------------------------------

function printLow_ReturnHigh(arr) {
    var lowest = arr[0];
    var highest = arr[0];
    for (var idx = 0; idx < arr.length; idx++) {
        // Check for lowest
        if (lowest > arr[idx]) {
            lowest = arr[idx]
        }
        // Check for highest
        if (highest < arr[idx]) {
            highest = arr[idx]
        }
    }
    console.log('The lowest value in the array:', lowest)
    return highest;
}

arr = [1, 2, 7, -4, 5]
console.log("\n**** Print Low Return High ****")
console.log('original array value', arr)
var highest = printLow_ReturnHigh(arr)
console.log('The highest value in the array:', highest)


//----------------------------------------------------------------------------
// Print One, Return Another
//----------------------------------------------------------------------------
// Build a function that takes an array of numbers. The function should 
// print the second-to-last value in the array, and return the first odd 
// value in the array.
//----------------------------------------------------------------------------

function printOne_ReturnAnother(arr) {
    var first_odd_value;
    for (var idx = 0; idx < arr.length; idx++) {
        if ((arr[idx] % 2 != 0) && !first_odd_value) {
            first_odd_value = arr[idx]
        }
        if (idx == arr.length - 2) {
            console.log('The second-to-last value in the array is:', arr[idx])
        }
    }

    return first_odd_value
}

arr = [0, 4, 6, 2, 7, 9, 4, 5]
console.log("\n**** Print One Return Another ****")
console.log('original array value', arr)
var first_odd_value = printOne_ReturnAnother(arr)
console.log('The first odd value in the array:', first_odd_value)


//----------------------------------------------------------------------------
// Double Vision
//----------------------------------------------------------------------------
// Given an array, create a function to return a new array where each value 
// in the original has been doubled. Calling double([1,2,3]) should 
// return [2,4,6] without changing original.
//----------------------------------------------------------------------------

function double(arr) {
    var newArray = [];
    for (var idx = 0; idx < arr.length; idx++) {
        newArray.push(arr[idx] * 2)
    }
    return newArray;
}

arr = [0, 2, 7, 8, 10, 15]
console.log("\n**** Double Vision ****")
console.log('original array value', arr)
newArray = double(arr)
console.log('original array value (unchanged)', arr)
console.log('newArray with doubled values is:', newArray)


//----------------------------------------------------------------------------
// Count Positives
//----------------------------------------------------------------------------
// Given an array of numbers, create a function to replace last value with 
// the number of positive values. Example,  countPositives([-1,1,1,1]) 
// changes array to [-1,1,1,3] and returns it.
//----------------------------------------------------------------------------
// NOTE: Arrays are passed by reference, not value, so changing the array 
// that is passed to this function results in the original array outside the 
// function being changed because the function changes the original array 
// (there is no copy of the array. The function modifies the origina array). 
// Seems silly to return the original array.
//----------------------------------------------------------------------------

function countPositives(arr) {
    var number_of_positive_values = 0;

    for (var idx = 0; idx < arr.length; idx++) {
        if (arr[idx] >= 0) {
            number_of_positive_values++;
        }
    }
    arr[arr.length - 1] = number_of_positive_values;
    return arr
}

arr = [-1, 1, 1, 1]
console.log("\n**** Count Positives ****")
console.log('original array value', arr)
newArray = countPositives(arr)
console.log('original array value (changed)', arr)
console.log('newArray with doubled values is:', newArray)


//----------------------------------------------------------------------------
// Evens and Odds
//----------------------------------------------------------------------------
// Create a function that accepts an array. Every time that array has three 
// odd values in a row, print "That’s odd!" Every time the array has three 
// evens in a row, print "Even more so!"
//----------------------------------------------------------------------------

function evensAndOdds(arr) {
    var even_values_in_a_row = 0;
    var odd_values_in_a_row = 0;
    for (var idx = 0; idx < arr.length; idx++) {
        if (arr[idx] % 2 == 0) {
            even_values_in_a_row++
            odd_values_in_a_row = 0
        } else {
            odd_values_in_a_row++;
            even_values_in_a_row = 0;
        }
        if (odd_values_in_a_row >= 3) {
            console.log("That's Odd!")
        }
        if (even_values_in_a_row >= 3) {
            console.log("Even more so!")
        }

    }
}


arr = [1, 2, 3, 5, 7, 9, 4, 6, 8, 10, 12]
console.log("\n**** Evens and Odds ****")
console.log('original array value', arr)
newArray = evensAndOdds(arr)


//----------------------------------------------------------------------------
// Increment the Seconds
//----------------------------------------------------------------------------
//Given arr, add 1 to odd elements([1], [3], etc.), console.log all values 
// and return arr.
//----------------------------------------------------------------------------
// NOTE: Again, arrays are passed by reference, not value, so any changes 
// made to the array that is passed to the function changes the original
// array, returning the array is redundant.
//----------------------------------------------------------------------------
function incrementTheSeconds(arr) {
    for (var idx = 0; idx < arr.length; idx++) {
        if (idx % 2 != 0) {
            arr[idx]++
        }
    }
    return arr
}

arr = [1, 2, 3, 5, 7, 9, 4, 6, 8, 10, 12]
console.log("\n**** Increment The Seconds ****")
console.log('original array value', arr)
newArray = incrementTheSeconds(arr)
console.log('original array value (modified)', arr)
console.log('returned array value', newArray)


//----------------------------------------------------------------------------
// Previous Lengths
//----------------------------------------------------------------------------
// You are passed an array containing strings. Working within that same 
// array, replace each string with a number – the length of the string at 
// previous array index – and return the array.
//----------------------------------------------------------------------------
// NOTE: What should we put in the first array element? 0? That's what I did
//----------------------------------------------------------------------------
function previousLengths(arr) {
    for (var idx = arr.length - 1; idx >= 0; idx--) {
        if (idx == 0) {
            arr[idx] = 0;
        } else {
            temp = arr[idx - 1]
            // console.log('temp', temp);
            // console.log('temp.length', temp.length);
            arr[idx] = temp.length;
        }
    }
    return arr;
}


arr = ['keith', 'eric', 'donnie', 'sydney', 'barbara']
console.log("\n**** Previous Lengths ****")
console.log('original array value', arr)
newArray = previousLengths(arr)
console.log('original array value (modified)', arr)
console.log('returned array value', newArray)


//----------------------------------------------------------------------------
// Add Seven to Most
//----------------------------------------------------------------------------
// Build a function that accepts an array. Return a new array with all values 
// except first, adding 7 to each. Do not alter the original array.
//----------------------------------------------------------------------------
function addSevenToMost(arr) {
    var newArray = [];
    for (var idx = 1; idx < arr.length; idx++) {
        newArray.push(arr[idx] + 7);
    }
    return newArray;
}


arr = [0, 1, 2, 3, 4, 5]
console.log("\n**** Add Seven to Most ****")
console.log('original array value', arr)
newArray = addSevenToMost(arr)
console.log('original array value (unmodified)', arr)
console.log('returned array value', newArray)