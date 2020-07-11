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