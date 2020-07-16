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


//****************************************************************************
// Remove At
//****************************************************************************
// Given an array and an index into array, remove and return the array 
// value at that index. Do this without using built-in array methods except 
// pop(). Think of popFront(arr) as equivalent to removeAt(arr,0).
//****************************************************************************

function removeAt(arr, index) {

    // Save this element. It's the one we'll return
    remove_element = arr[index]

    // Starting with the element we want to remove..
    // reassign the value at idx to the value to its right
    for (let idx = index; idx < arr.length; idx++) {
        arr[idx] = arr[idx + 1]
    }
    // Now the last item in the array is a dupe of the one to it's left
    // So remove it.
    arr.pop();
    return remove_element;
}

console.log('\n**** Remove At ****')
arr = [1, 2, 3, 4, 5, 6, 7]
console.log('original array: ' + arr)
let remove_at_index = 3
console.log('remove the element at index:', remove_at_index)
console.log('remove element at array index: ' + remove_at_index);
console.log('The value at array index ' + remove_at_index + ' was ' + removeAt(arr, remove_at_index))
console.log('modified array: ' + arr)


//****************************************************************************
// Swap Pairs
//****************************************************************************
// Swap positions of successive pairs of values of given array. If length is 
// odd, do not change the final element. 
// 
// For [1,2,3,4], return [2,1,4,3]. 
//
// For example, change input ["Brendan",true,42] to [true,"Brendan",42]. 
// 
// As with all array challenges, do this without using any built-in array 
// methods.
//****************************************************************************

function swapPairs(arr) {
    for (let idx = 0; idx < arr.length; idx += 2) {

        // If there is no element after this one, it means we have an odd
        // array length. Do not attempt to swap, just exit loop.
        if (idx + 1 == arr.length) {
            break;
        }
        // Save element at idx
        let temp = arr[idx]
        // swap idx for what is in idx+1
        arr[idx] = arr[idx + 1]
        // store saved temp value (from idx) to array index of idx+1 
        arr[idx + 1] = temp
    }
}

console.log('\n**** Swap Pairs ****')
arr = [1, 2, 3, 4, 5, 6, 7]
console.log('original array: ' + arr)
swapPairs(arr)
console.log('modified array: ' + arr)


//****************************************************************************
// Remove Duplicates
//****************************************************************************
//
// Sara is looking to hire an awesome web developer and has received 
// applications from various sources. Her assistant alphabetized them but 
// noticed some duplicates. Given a sorted array, remove duplicate values. 
// Because array elements are already in order, all duplicate values will be 
// grouped together. As with all these array challenges, do this without 
// using any built-in array methods.
//
// Second: Solve this without using any nested loops.
//****************************************************************************

function removeDuplicates(arr) {

    // Create new array to store non dupe elements.
    // And preload it with the first element from the original array
    let newArray = [arr[0]]
    // Set the index for the new array at 1, we've already add the first
    // element.
    let idx2 = 1;

    // Loop through the original array and check if the element at the current
    // index is a duple of the element at the previous element (idx-1)
    // If it is NOT a dupe at it to the new array, and increment the index
    // for the new array.
    for (let idx = 1; idx < arr.length; idx++) {
        if (arr[idx] != arr[idx - 1]) {
            newArray[idx2] = arr[idx]
            idx2++;
        }
    }
    // Return the new array. It can overwrite the orginal or be stored in a new variable.
    return newArray;
}

console.log('\n**** Remove Duplicates ****')
arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]
console.log('original array: ' + arr)
arr = removeDuplicates(arr)
console.log('modified array: ' + arr)