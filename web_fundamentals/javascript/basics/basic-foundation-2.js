/////////////////////////////////////////////////////////////////////////////////////////////////
// biggieSize
// Given an array, write a function that changes all positive numbers in the array to the 
// string "big".  
// Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].
/////////////////////////////////////////////////////////////////////////////////////////////////

function biggieSize(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      arr[i] = "big";
    }
  }
  return arr;
}
myVar = [-1, 3, 5, -5];
console.log('**** biggieSize() ****');
console.log('Given the array [' + myVar + '], replacing all the positive numbers results in [' + biggieSize(myVar) + ']');

/////////////////////////////////////////////////////////////////////////////////////////////////
// printLowReturnHigh
// Create a function that takes in an array of numbers.  The function should print the lowest 
// value in the array, and return the highest value in the array.
/////////////////////////////////////////////////////////////////////////////////////////////////

function printLowReturnHigh(arr) {
  var lowest = hightest = 0;
  for (var i = 0; i < arr.length; i++) {
    if (lowest > arr[i]) {
      lowest = arr[i];
    }
    if (highest < arr[i]) {
      highest = arr[i];
    }
  }
  console.log("The lowest value in the array [" + arr + "] is: " + lowest);
  return highest;
}
var myArr = [1, 3, 5, 2, 0];
var highest = 0;
console.log('**** printLowReturnHigh() ****');
highest = printLowReturnHigh(myArr);
console.log("The highest value is: " + highest);

/////////////////////////////////////////////////////////////////////////////////////////////////
// printOneReturnAnother
// Build a function that takes in an array of numbers.  The function should print the 
// second-to-last value in the array, and return the first odd value in the array.
/////////////////////////////////////////////////////////////////////////////////////////////////

function printOneReturnAnother(arr) {
  var first_odd_value = null;
  for (var i = 0; i < arr.length; i++) {
    if ((arr[i] % 2 !== 0) && (first_odd_value === null)) {
      first_odd_value = arr[i];
    }
    if (i === arr.length - 2) {
      console.log('The second-to-last value is: ' + arr[i]);
    }
  }
  return first_odd_value;
}

var myArr = [2, 4, 5, 6, 9, 10];
console.log('**** printOneReturnAnother ****')
console.log('The array is [' + myArr + ']')
var first_odd_value = printOneReturnAnother(myArr);
console.log('The first odd value was: ' + first_odd_value);

/////////////////////////////////////////////////////////////////////////////////////////////////
// double_vision
// Given an array(similar to saying 'takes in an array'), create a function that returns a new 
// array where each value in the original array has been doubled.Calling double([1, 2, 3]) 
// should return [2, 4, 6] without changing the original array.
/////////////////////////////////////////////////////////////////////////////////////////////////

function double(arr) {
  var newArr = [];
  for (var i = 0; i < arr.length; i++) {
    newArr.push(arr[i] * arr[i]);
  }
  return newArr;
}

var myArray = [1, 2, 3];
console.log('**** double() ****');
console.log('The original array is: [' + myArray + ']. The returned array with doubled values is [' + double(myArray) + ']');

/////////////////////////////////////////////////////////////////////////////////////////////////
// countPositives() 
// Given an array of numbers, create a function to replace the last value with the number of 
// positive values found in the array.  Example, countPositives([-1,1,1,1]) 
// changes the original array to [-1,1,1,3] and returns it.
/////////////////////////////////////////////////////////////////////////////////////////////////

function countPositives(arr) {
  var positive_values = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] >= 0) {
      positive_values++;
    }
  }
  arr[arr.length - 1] = positive_values;
  return arr;
}

var myArr = [-1, 1, 1, 1];
console.log("**** countPositives ****");
console.log("Original array: [" + myArr + "]");
myArr = countPositives(myArr);
console.log("Modified array: [" + myArr + "]");

////////////////////////////////////////////////////////////////////////////////////////////////////
// evensAndOdds()
// Create a function that accepts an array.  Every time that array has three odd values in a 
// row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".
////////////////////////////////////////////////////////////////////////////////////////////////////

function evensAndOdds(arr) {
  var number_of_odds = number_of_evens = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) { // Even Number
      number_of_evens++;
      number_of_odds = 0;
    } else {
      number_of_odds++;
      number_of_evens = 0;
    }
    if (number_of_odds === 3) {
      console.log("That's odd!");
      number_of_odds = number_of_evens = 0;
    }
    if (number_of_evens === 3) {
      console.log("Even more so!");
      number_of_odds = number_of_evens = 0;
    }
  }
}

var myArray = [1, 2, 3, 4, 5, 7, 9, 3, 4, 6, 8, 10, 11];
console.log("**** evensAndOdds() ****");
console.log("Original Array: [" + myArray + "]");
evensAndOdds(myArray);

////////////////////////////////////////////////////////////////////////////////////////////////////
// incrementTheSeconds()
// Given an array of numbers arr, add 1 to every other element, specifically those whose index is 
// odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.
////////////////////////////////////////////////////////////////////////////////////////////////////

function incrementTheSeconds(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (i % 2 !== 0) { // This index value is odd.
      arr[i]++; //Add 1 to the element.
    }
  }
  console.log("Modified array: [" + arr + "]");
  return arr;
}

console.log("**** incrementTheSeconds ****");
var myArray = [1, 3, 5, 2, 3, 4, 6, 3];
console.log("Original array: [" + myArray + "]");
myArray = incrementTheSeconds(myArray);

////////////////////////////////////////////////////////////////////////////////////////////////////
// previousLengths()
// Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an 
// array') containing strings.  Working within that same array, replace each string with a 
// number - the length of the string at the previous array index - and return the array.  
// For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. 
// Hint: Can for loops only go forward?
////////////////////////////////////////////////////////////////////////////////////////////////////

function previousLengths(arr) {

  for (var i = arr.length - 1; i > 0; i--) {
    arr[i] = arr[i - 1].length;
  }
  return arr;
}

var myArray = ["hello", "dojo", "awesome"];
console.log("**** previousLengths() ****");
console.log("Original Array: [" + myArray + "]");
myArray = previousLengths(myArray);
console.log("Modified Array: [" + myArray + "]");

////////////////////////////////////////////////////////////////////////////////////////////////////
// addSeven()
// Build a function that accepts an array. Return a new array with all the values of the original, 
// but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return 
// [8,9,10] in a new array.
////////////////////////////////////////////////////////////////////////////////////////////////////

function addSeven(arr) {
  var myNewArr = [...arr]; // Make a copy of the array (don't use the reference to the other array)
  for (var i = 0; i < myNewArr.length; i++) {
    myNewArr[i] += 7;
  }
  return myNewArr;
}

var myArray = [1, 2, 3];
var myNewArray = addSeven(myArray);
console.log("**** addSeven() ****");
console.log("Original Array: [" + myArray + "]");
console.log("New Array: [" + myNewArray + "]");

////////////////////////////////////////////////////////////////////////////////////////////////////
// reverseArray()
// Reverse Array - Given an array, write a function that reverses its values, in-place.  
// Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed 
// like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  
// (Hint: you'll need to swap values).
////////////////////////////////////////////////////////////////////////////////////////////////////

function reverseArray(arr) {
  var swap_value = 0;

  // We only need to swap number until we get to the center of the array
  for (var i = 0; i < (Math.floor(arr.length / 2)); i++) {
    swap_value = arr[i];
    arr[i] = arr[arr.length - (i + 1)];
    arr[arr.length - (i + 1)] = swap_value;
  }
}

var myArray = [3, 1, 6, 4, 2];
console.log("**** reverseArray ****");
console.log("Original array: [" + myArray + "]");
reverseArray(myArray);
console.log("Modified array: [" + myArray + "]");
console.log("Now try it with an even number of elements (6)");
myArray = [3, 1, 6, 4, 2, 5];
console.log("Original array: [" + myArray + "]");
reverseArray(myArray);
console.log("Modified array: [" + myArray + "]");

////////////////////////////////////////////////////////////////////////////////////////////////////
// outlookNegative()
// Given an array, create and return a new one containing all the values of the original array, 
// but make them all negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].
////////////////////////////////////////////////////////////////////////////////////////////////////

function outlookNegative(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      arr[i] *= -1;
    }
  }
  return arr;
}

var myArray = [1, -3, 5];
console.log("**** outlookNegative ****");
console.log("Original Array: [" + myArray + "]");
outlookNegative(myArray);
console.log("Modified Array: [" + myArray + "]");


////////////////////////////////////////////////////////////////////////////////////////////////////
// alwaysHungry()
// Create a function that accepts an array, and prints "yummy" each time one of the values is 
// equal to "food".  If no array values are "food", then print "I'm hungry" once.
////////////////////////////////////////////////////////////////////////////////////////////////////

function alwaysHungry(arr) {

  var counter = 0;
  for (var i = 0; i < arr.length; i++) {
    // Use toUpperCase() to catch different capitalization of food (Food,FOOD,food);
    if (arr[i].toString().toUpperCase() === "FOOD") {
      console.log("yummy");
      counter++;
    }
  }
  if (counter === 0) {
    console.log("I'm hungry");
  }
}

console.log("**** alwaysHungry() ****");
var myArray = ["keith", "hungry", 1, 3, "home", "butter", "FOOD", 1, 2, "food", "Food"];
console.log("array: [" + myArray + "]");
alwaysHungry(myArray);
myArray = ["keith", "hungry", 1, 3, "home", "butter", "feed", 1, 2, "fooder", "yummy"];
console.log("array: [" + myArray + "]");
alwaysHungry(myArray);

////////////////////////////////////////////////////////////////////////////////////////////////////
// swapTowardTheCenter()
// Given an array, swap the first and last values, third and third-to-last values, etc.  
// Example: swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into 
// ["pizza", 42, "Ada", 2, true].  
// swapTowardCenter([1,2,3,4,5,6]) turns the array into [6,2,4,3,5,1].  
// No need to return the array this time.
////////////////////////////////////////////////////////////////////////////////////////////////////

function swapTowardTheCenter(arr) {

  var swap = 0;

  // Swap the first and last (only if there is more than one element in the array)
  if (arr.length > 1) {
    swap = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = swap;
  }

  // Swap the third and third-to-last, if there is a third element
  if (arr.length > 2) {
    swap = arr[2];
    arr[2] = arr[arr.length - 3];
    arr[arr.length - 3] = swap;
  }
  console.log("Modified Array: [" + myArray + "]");
}

// Test with the two arrays given in the instructions
console.log("**** swapToTheCenter ****");
var myArray = [true, 42, "Ada", 2, "pizza"];
console.log("Original Array: [" + myArray + "]");
swapTowardTheCenter(myArray);
myArray = [1, 2, 3, 4, 5, 6];
console.log("Original Array: [" + myArray + "]");
swapTowardTheCenter(myArray);

// Now try it with just two elements (just swap first and last)
myArray = [1, 2];
console.log("Original Array: [" + myArray + "]");
swapTowardTheCenter(myArray);

// Now try it with just ONE element (no swapping at all)
myArray = [1];
console.log("Original Array: [" + myArray + "]");
swapTowardTheCenter(myArray);

////////////////////////////////////////////////////////////////////////////////////////////////////
// scaleTheArray()
// Given an array arr and a number num, multiply all values in the array arr by the number num, 
// and return the changed array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9].
////////////////////////////////////////////////////////////////////////////////////////////////////

function scaleTheArray(arr, number) {

  for (var i = 0; i < arr.length; i++) {
    arr[i] *= number;
  }
}

console.log("**** scaleTheArray ****");
var myArray = [1, 2, 3];
console.log("Original Array: [" + myArray + "]");
scaleTheArray(myArray, 3)
console.log("Modified Array: [" + myArray + "]");

////////////////////////////////////////////////////////////////////////////////////////////////////
// NOTE about arrays and passing by referennce (rather than value): 
////////////////////////////////////////////////////////////////////////////////////////////////////
// Arrays are passed by reference, not by value, so the array that is passed to the function
// is actually a pointer/reference to the original. So when we change the array in the function,
// it's actually changing the original array. So we don't need to return the array from the 
// function. Most of the functions I've created in this file RETURN the modified array from within
// the function, because that's what the instructions requested. But this last function, 
// scaleTheArray(), I didn't return ANYTHING. The original array is already modified.
////////////////////////////////////////////////////////////////////////////////////////////////////

console.log("\n*********************");
console.log(" All Done");
console.log("*********************\n");

