//****************************************************************************
// Pop Front
//****************************************************************************
// Given an array, remove and return the value at the beginning of the array. 
// Do this without using any built-in array methods except pop().
//****************************************************************************

function popFront(arr) {
    // Save the first element in the array, we'll return it from this function
    // and overwrite shortly
    first_element = arr[0];

    // move all element values in the array to the element just before it
    for (let idx = 0; idx < arr.length - 1; idx++) {
        arr[idx] = arr[idx + 1]
    }
    // Remove the last element, which is now a dupe of the element 
    // just before it
    arr.pop()
    return first_element;
}

console.log('\n**** Pop Front ****')
arr = [1, 2, 3, 4, 5, 6, 7]
console.log('original array: ' + arr)
console.log(popFront(arr));
console.log('modified array: ' + arr)