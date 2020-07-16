//****************************************************************************
// Reverse
//****************************************************************************
// 
// Given a numerical array, reverse the order of values, in -place.
// The reversed array should have the same length, with existing elements 
// moved to other indices so that order of elements is reversed.
// Working‘ in -place’ means that you cannot use a second array– move values 
// within the array that you are given.
// 
// As always, do not use built - in array functions such as splice().
//****************************************************************************

function reverse(arr) {
    for (let idx = 0; idx < arr.length / 2; idx++) {
        temp = arr[idx]
        arr[idx] = arr[arr.length - 1 - idx]
        arr[arr.length - 1 - idx] = temp
    }
}

console.log('\n**** Reverse ****')
arr = [1, 2, 3, 4, 5, 6, 7]
console.log('original array: ' + arr)
reverse(arr)
console.log('modified array: ' + arr)