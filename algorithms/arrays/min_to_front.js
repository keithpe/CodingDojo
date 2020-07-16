//****************************************************************************
// Min to Front
//****************************************************************************
// Given an array of comparable values, move the lowest element to array’s 
// front, shifting backward any elements previously ahead of it. Do not 
// otherwise change the array’s order. 
// 
// Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. 
// As always, do this without using built-in functions.
//****************************************************************************

function minToFront(arr) {

    // We'll use min_idx as a pointer to the minimum value when we find it
    let min_idx = 0;

    // We'll store the min value here, so we can compare it to arr elements
    // as we move through the array
    let min = arr[0];

    // Loop through the array and find the minimum value
    for (let idx = 1; idx < arr.length; idx++) {
        if (arr[idx] < min) {
            min = arr[idx];
            min_idx = idx;
        }
    }

    // Now move everything the position just BEFORE the original location of 
    // the minimum value to the right in the array. 
    for (let idx = min_idx; idx > 0; idx--) {
        arr[idx] = arr[idx - 1]
    }
    // Store the minimum value in position 0
    arr[0] = min

    console.log('minimum value of ' + min + ' found at index ' + min_idx)

}

console.log('\n**** Min to Front ****')
arr = [4, 2, 1, 3, 5]
console.log('original array: ' + arr)
minToFront(arr)
console.log('modified array: ' + arr)