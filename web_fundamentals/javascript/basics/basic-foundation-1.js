/////////////////////////////////////////////////////////////////////////////////////////////////
// Get 1 to 255 
// Write a function that returns an array with all the numbers from 1 to 255.
/////////////////////////////////////////////////////////////////////////////////////////////////

function get_1_to_255() {
  var arr = [];
  for (i = 1; i <= 255; i++) {
    arr.push(i);
  }
  return arr;
}
var myArr = (get_1_to_255());
console.log('get_1_to_255: returns an array with all the numbers from 1 to 255.');
console.log(...myArr);

/////////////////////////////////////////////////////////////////////////////////////////////////
// Get even 1000 
// Write a function that would get the sum of all the even numbers from 1 to 1000.  
// You may use a modulus operator for this exercise.
/////////////////////////////////////////////////////////////////////////////////////////////////

function get_even_1000() {
  var sum = 0;
  for (var i = 0; i <= 1000; i++) {
    if (i % 2 === 0) {  // Even Number!
      sum += i;
    }
  }
  return sum;
}
console.log('get_even_100: The sum of even numbers from 1 to 1000 is:', get_even_1000());

/////////////////////////////////////////////////////////////////////////////////////////////////
// Sum odd 5000 
// Write a function that returns the sum of all the odd numbers from 1 to 5000. 
// (e.g. 1+3+5+...+4997+4999).
/////////////////////////////////////////////////////////////////////////////////////////////////

function sum_odd_5000() {
  var sum = 0;
  for (var i = 1; i <= 5000; i++) {
    if (i % 2 !== 0) { // Odd number (not even)
      sum += i;
    }
  }
  return sum;
}
console.log('sum_odd_5000: The sum of all the odd numbers from 1 to 5000:', sum_odd_5000());

/////////////////////////////////////////////////////////////////////////////////////////////////
// Iterate_an_array
// Write a function that returns the sum of all the values within an array. 
// (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14.
/////////////////////////////////////////////////////////////////////////////////////////////////

function iterate_an_array(arr) {
  var sum = 0;
  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
console.log('iterate_an_array: The sum of all the values with the array:', iterate_an_array([1, 2, 5]));
console.log('iterate_an_array: The sum of all the values with the array:', iterate_an_array([-5, 2, 5, 12]));

/////////////////////////////////////////////////////////////////////////////////////////////////
// Find_max
// Given an array with multiple values, write a function that returns the maximum number 
// in the array. (e.g. for [-3,3,5,7] max is 7)
/////////////////////////////////////////////////////////////////////////////////////////////////

function find_max(arr) {

  var max = arr[0];
  for (var i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i];
    }
  }
  return max;
}

var myArr = [-3, 3, 5, 7];
console.log('The maximum number in the array [' + myArr + '] is: ' + find_max(myArr));

/////////////////////////////////////////////////////////////////////////////////////////////////
// find_average
// Given an array with multiple values, write a function that returns the average of the values 
// in the array. (e.g. for [1,3,5,7,20] average is 7.2)
/////////////////////////////////////////////////////////////////////////////////////////////////

function find_average(arr) {
  var avg = 0, sum = 0;
  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  avg = sum / arr.length;
  return avg;
}

var myArr = [1, 3, 5, 7, 20];
console.log('The average of the values in the array [' + myArr + '] is ' + find_average(myArr));

/////////////////////////////////////////////////////////////////////////////////////////////////
// array_odd
// Write a function that would return an array of all the odd numbers between 1 to 50. 
// (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
/////////////////////////////////////////////////////////////////////////////////////////////////

function array_odd() {
  myArr = [];
  for (var i = 1; i <= 50; i++) {
    if (i % 2 !== 0) { // Odd number (not even)
      myArr.push(i);
    }
  }
  return myArr;
}

console.log('An array of all the odd numbers between 1 to 50: [' + array_odd() + ']');

/////////////////////////////////////////////////////////////////////////////////////////////////
// greater_than_y
// Given value of Y, write a function that takes an array and returns the number of values that 
// are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. 
// (There are two values in the array greater than 3, which are 5, 7).
/////////////////////////////////////////////////////////////////////////////////////////////////

function greater_than_y(y, arr) {
  var count = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > y) {
      count++;
    }
  }
  return count;
}
var y = 3;
myArr = [1, 3, 5, 7];
console.log('The number of values in the array [' + myArr + '] that are greater than the value of ' + y + ' is ' + greater_than_y(y, myArr));

/////////////////////////////////////////////////////////////////////////////////////////////////
// squares
// Given an array with multiple values, write a function that replaces each value in the array 
// with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
/////////////////////////////////////////////////////////////////////////////////////////////////

function squares(arr) {
  for (var i = 0; i < arr.length; i++) {
    arr[i] = arr[i] * arr[i];
  }
  return arr;
}

myArr = [1, 5, 10, -2];
console.log("Squaring all the elements in the array [" + myArr + "] returns the array [" + squares(myArr) + "]");

/////////////////////////////////////////////////////////////////////////////////////////////////
// negatives
// Given an array with multiple values, write a function that replaces any negative numbers 
// within the array with the value of 0. When the program is done the array should contain no 
// negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
/////////////////////////////////////////////////////////////////////////////////////////////////

function negatives(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      arr[i] = 0;
    }
  }
  return arr;
}
var myArr = [1, 5, 10, -2];
console.log('Given the array [' + myArr + '], the new array replaces any negative values with 0. Like this: [' + negatives(myArr) + ']');

/////////////////////////////////////////////////////////////////////////////////////////////////
// Max_Min_Avg()
// Given an array with multiple values, write a function that returns a new array that only 
// contains the maximum, minimum, and average values of the original array. 
// (e.g. [1,5,10,-2] will return [10,-2,3.5])
/////////////////////////////////////////////////////////////////////////////////////////////////

function max_min_avg(arr) {
  var newArr = [];
  var max = min = avg = sum = 0;
  for (var i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i];
    }
    if (min > arr[i]) {
      min = arr[i];
    }
    sum += arr[i];
  }
  avg = sum / arr.length;
  newArr = [max, min, avg];
  return newArr;
}
var myArr = [1, 5, 10, -2];
console.log("Given the array [" + myArr + "] here's an array with the max, min and avg values for the original array: [" + max_min_avg(myArr) + "]");

/////////////////////////////////////////////////////////////////////////////////////////////////
// swap_values 
// Write a function that will swap the first and last values of any given array. The default 
// minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
/////////////////////////////////////////////////////////////////////////////////////////////////

function swap_values(arr) {
  if (arr.length < 2) {
    console.log('Array must contain at least two elements');
    return;
  }
  var temp = arr[0];
  arr[0] = arr[arr.length - 1];
  arr[arr.length - 1] = temp;
  return arr;
}
myArr = [1, 5, 10, -2];
console.log('Given the array [' + myArr + '], swapping first and last values returns [' + swap_values(myArr) + ']');


/////////////////////////////////////////////////////////////////////////////////////////////////
// number_to_string 
// Write a function that takes an array of numbers and replaces any negative values within 
// the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will 
// return ['Dojo','Dojo',2].
/////////////////////////////////////////////////////////////////////////////////////////////////

function number_to_string(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      arr[i] = 'Dojo';
    }
  }
  return arr;
}
myArr = [-1, -3, 2];
console.log('Given the array [' + myArr + '], replacing all negative values results with "Dojo" returns this array [' + number_to_string(myArr) + ']')