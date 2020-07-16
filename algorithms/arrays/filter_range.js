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
// TODO: The instructions say NO builtin functions AND work IN-PLACE, but 
// I'm assuming that we can use pop as in previous examples that also allowed 
// no builtin functions. Otherwise I would use a second array to do this.
//****************************************************************************

function filterRange(arr, min, max) {

    console.log('min:', min, 'max:', max);

    // Check the last element in the array. If it's not within the min/max
    // values then pop it off the array. Repeat the same number as the
    // array length

    let original_arr_length = arr.length;

    while (original_arr_length) {

        if ((arr[arr.length - 1] >= min) && (arr[arr.length - 1] <= max)) {
            temp = arr[arr.length - 1];
            for (let idx = arr.length - 1; idx >= 0; idx--) {
                arr[idx] = arr[idx - 1];
            }
            arr[0] = temp;
        } else {
            arr.pop();
        }
        original_arr_length--;
    }
}

console.log('\n**** Filter Range ****')
arr = [1, 7, 2, 4, 3, 5, 27];
min = 2;
max = 4;
console.log('original array: ' + arr)
filterRange(arr, min, max)
console.log('modified array: ' + arr)