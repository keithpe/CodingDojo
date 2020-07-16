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



//****************************************************************************
// Rotate
//****************************************************************************
// Implement rotateArr(arr, shiftBy) that accepts array and offset. 
// Shift arr’s values to the right by that amount. ‘Wrap-around’ any values 
// that shift off array’s end to the other side, so that no data is lost. 
// Operate in-place: given ([1,2,3],1), change the array to [3,1,2]. 
// Don’t use built-in functions.
//
// Second: allow negative shiftBy (shift L, not R).
//
// Third: minimize memory usage. With no new array, handle arrays/shiftBys 
// in the millions.
//
// Fourth: minimize the touches of each element.
// 
// No built-in array functions.
//****************************************************************************

function rotateArr(arr, shiftBy) {

    // The outer loop handles the shiftby loop
    for (let shiftIDX = 0; shiftIDX < shiftBy; shiftIDX++) {
        // We're shifting right so save the value in the last array index position
        wrap_around_value = arr[arr.length - 1]
        for (let idx = arr.length - 1; idx > 0; idx--) {
            arr[idx] = arr[idx - 1]
        }
        arr[0] = wrap_around_value;
    }
}

console.log('\n**** Rotate ****')
arr = [1, 2, 3, 4, 5, 6, 7]
shiftBy = 3
console.log('original array: ' + arr)
console.log('shiftBy', shiftBy)
rotateArr(arr, shiftBy)
console.log('modified array: ' + arr)

//****************************************************************************
// Second: allow negative shiftBy (shift L, not R).
//****************************************************************************

function rotateArr2(arr, shiftBy) {

    // Shift RIGHT if shiftBy is POSITIVE... 
    if (shiftBy > 0) {
        console.log('SHIFTING RIGHT')

        // The outer loop handles the shiftby loop
        for (let shiftIDX = 0; shiftIDX < shiftBy; shiftIDX++) {

            // We're shifting right so save the value in the last array index position
            wrap_around_value = arr[arr.length - 1]

            // Loop through the array and shift to the RIGHT
            for (let idx = arr.length - 1; idx > 0; idx--) {
                arr[idx] = arr[idx - 1]
            }
            // Restore wrap around value after each loop through the array (for each shift)
            arr[0] = wrap_around_value;
        }

    } else {
        // ... shiftBy is negative, shift LEFT

        // The outer loop handles the shiftby loop
        console.log('SHIFTING LEFT')

        for (let shiftIDX = 0; shiftIDX > shiftBy; shiftIDX--) {

            // We're shifting right so save the value in the last array index position
            wrap_around_value = arr[0]

            // Loop through the array and shift to the LEFT
            for (let idx = 0; idx < arr.length - 1; idx++) {
                arr[idx] = arr[idx + 1]
            }

            // Restore the wrap around value after each loop through the array (for each shift)
            arr[arr.length - 1] = wrap_around_value;
        }
    }
}

console.log('\n**** Rotate2 (allow negative shiftBy - shift L, not R) ****')
arr = [1, 2, 3, 4, 5, 6, 7]
shiftBy = -3
console.log('original array: ' + arr)
console.log('shiftBy', shiftBy)
rotateArr2(arr, shiftBy)
console.log('modified array: ' + arr)


//****************************************************************************
// Third: minimize memory usage. With no new array, handle arrays/shiftBys 
// in the millions.
// 
// If the array is only 10 elements in length and we want to rotate it by 11
// we can rotate by 1 and get the same result.
//
//****************************************************************************
// TODO: Other than limiting the loops to shiftBy - array length, I'm not sure
// what else to do.
//****************************************************************************
function rotateArr3(arr, shiftBy) {

    // Shift RIGHT if shiftBy is POSITIVE... 
    if (shiftBy > 0) {
        console.log('SHIFTING RIGHT')

        // Reduce the number of shiftby so we loop fewer times
        if (shiftBy > arr.length) {
            shiftBy = shiftBy - arr.length
        }

        // The outer loop handles the shiftby loop
        for (let shiftIDX = 0; shiftIDX < shiftBy; shiftIDX++) {

            // We're shifting right so save the value in the last array index position
            wrap_around_value = arr[arr.length - 1]

            // Loop through the array and shift to the RIGHT
            for (let idx = arr.length - 1; idx > 0; idx--) {
                arr[idx] = arr[idx - 1]
            }
            // Restore wrap around value after each loop through the array (for each shift)
            arr[0] = wrap_around_value;
        }

    } else {
        // ... shiftBy is negative, shift LEFT

        // The outer loop handles the shiftby loop
        console.log('SHIFTING LEFT')

        // Reduce the number of shiftby so we loop fewer times
        shiftBy = Math.abs(shiftBy)
        if (shiftBy > arr.length) {
            shiftBy = shiftBy - arr.length
        }
        shiftBy *= -1

        for (let shiftIDX = 0; shiftIDX > shiftBy; shiftIDX--) {

            // We're shifting right so save the value in the last array index position
            wrap_around_value = arr[0]

            // Loop through the array and shift to the LEFT
            for (let idx = 0; idx < arr.length - 1; idx++) {
                arr[idx] = arr[idx + 1]
            }

            // Restore the wrap around value after each loop through the array (for each shift)
            arr[arr.length - 1] = wrap_around_value;
        }
    }
}

console.log('\n**** Rotate3 (minimize memory usage) ****')
arr = [1, 2, 3, 4, 5, 6, 7]
shiftBy = -10
console.log('original array: ' + arr)
console.log('shiftBy', shiftBy)
rotateArr3(arr, shiftBy)
console.log('modified array: ' + arr)


//****************************************************************************
// Filter Range
//****************************************************************************
// Alan is good at breaking secret codes. One method is to eliminate values 
// that lie within a specific known range. 
// 
// Given arr and values min and max, retain only the array values between 
// min and max. Work in-place: 
//
// return the array you are given, with values in original order. 
// 
// No built-in array functions.
//****************************************************************************