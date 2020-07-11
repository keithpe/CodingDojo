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
arr = [-1, 3, 5, -5]
console.log("\n**** BiggiSize ****")
console.log('before:', arr)
biggieSize(arr)
console.log('after:', arr)