// Part 1 - Create code that does the following.

// Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive 
// integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

function sigma(num) {
  var sum = 0;
  for (var i = 1; i <= num; i++) {
    sum += i;
  }
  return sum;
}
console.log("Sigma of 3 is: " + sigma(3));
console.log("Sigma of 5 is: " + sigma(5));

// Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) 
// of all positive integers from 1 up to the given number (inclusive).  
// For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

function factorial(num) {
  var product = 1;
  for (var i = 1; i <= num; i++) {
    product *= i;
  }
  return product;
}
console.log("Factorial of 3 is: " + factorial(3));
console.log("Factorial of 5 is: " + factorial(5));

// Fibonacci - Create a function to generate Fibonacci numbers.In this famous mathematical sequence, 
// each number is the sum of the previous two, starting with values 0 and 1.  
// Your function should accept one argument, an index into the sequence(where 0 corresponds to the 
// initial value, 4 corresponds to the value four later, etc).
// Examples: fibonacci(0) = 0(given), fibonacci(1) = 1(given), 
// fibonacci(2) = 1(fib(0) + fib(1), or 0 + 1), 
// fibonacci(3) = 2(fib(1) + fib(2)3, or 1 + 1), 
// fibonacci(4) = 3(1 + 2), 
// fibonacci(5) = 5(2 + 3), 
// fibonacci(6) = 8(3 + 5), 
// fibonacci(7) = 13(5 + 8).
// Do this without using recursion first. If you don't know what a recursion is yet, 
// don't worry as we'll be introducing this concept in Part 2 of this assignment.

function fibonacci(num) {

  if (num <= 1) {
    return num;
  }
  var current = 1;
  var previous = 1;

  for (var i = 2; i < num; ++i) {
    var temp = current;
    current += previous;
    previous = temp;
  }
  return current;
}

console.log("***************************")
console.log("Fibonacci without recursion");
console.log("***************************")
console.log("Fibonacci of 0 is: " + fibonacci(0));
console.log("Fibonacci of 1 is: " + fibonacci(1));
console.log("Fibonacci of 2 is: " + fibonacci(2));
console.log("Fibonacci of 3 is: " + fibonacci(3));
console.log("Fibonacci of 4 is: " + fibonacci(4));
console.log("Fibonacci of 5 is: " + fibonacci(5));
console.log("Fibonacci of 6 is: " + fibonacci(6));
console.log("Fibonacci of 7 is: " + fibonacci(7));

// Array: Second-to-Last: Return the second-to-last element of an array. 
// Given [42, true, 4, "Liam", 7], return "Liam".  
// If array is too short, return null.

function secondToLast(arr) {

  if (arr.length < 2) {
    return null;
  }
  return arr[arr.length - 2];
}
var myArray = [42, true, 4, "Liam", 7];
console.log("Second to Last in [" + myArray + "] = " + secondToLast(myArray));
myArray = [42, true];
console.log("Second to Last in [" + myArray + "] = " + secondToLast(myArray));
myArray = [42];
console.log("Second to Last in [" + myArray + "] = " + secondToLast(myArray));

// Array: Nth-to-Last: 
// Return the element that is N-from-array's-end.  
// Given ([5,2,3,6,4,9,7],3), return 4.  
// If the array is too short, return null.

function nthToLast(arr, num) {
  if (arr.length < num) {
    return null;
  }
  return arr[arr.length - num]
}

var myArray = [5, 2, 3, 6, 4, 9, 7];
var num = 3;
console.log(num + " to last in [" + myArray + "] = " + nthToLast(myArray, num));
num = 10;
console.log(num + " to last in [" + myArray + "] = " + nthToLast(myArray, num));
num = 7;
console.log(num + " to last in [" + myArray + "] = " + nthToLast(myArray, num));

// Array: Second-Largest: Return the second-largest element of an array. 
// Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

function secondLargest(arr) {
  let largest = 0;
  let secondLargest = 0;

  for (var i = 0; i < arr.length; i++) {
    if (largest < arr[i]) {
      largest = arr[i];
    }
  }
  for (var i = 0; i < arr.length; i++) {
    if ((secondLargest < arr[i]) && (arr[i] != largest)) {
      secondLargest = arr[i];
    }
  }

  return secondLargest;
}
var myArray = [42, 1, 4, 3, 14, 7];
console.log("The second largest element in [" + myArray + "] = " + secondLargest(myArray));
myArray = [35, 42, 1, 4, 3, 14, 7];
console.log("The second largest element in [" + myArray + "] = " + secondLargest(myArray));

// Double Trouble: Create a function that changes a given array to list each existing element twice, 
// retaining original order.  
// Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].

function doubleTrouble(arr) {
  var newArr = [];
  for (var i = 0; i < arr.length; i++) {
    newArr.push(arr[i]);
    newArr.push(arr[i]);
  }
  return newArr;
}

myArr = [4, "Ulysses", 42, false];
console.log("Array before = [" + myArr + "]");
myArr = doubleTrouble(myArr);
console.log("Array after = [" + myArr + "]");

/////////////////////////////////
// Fibonacci Using Recursion
/////////////////////////////////

function fib(num) {

  if (num <= 1) {
    return num;
  } else {
    return fib(num - 1) + fib(num - 2);
  }
}

console.log("************************")
console.log("Fibonacci with recursion");
console.log("************************")
console.log("Fibonacci of 0 is: " + fib(0));
console.log("Fibonacci of 1 is: " + fib(1));
console.log("Fibonacci of 2 is: " + fib(2));
console.log("Fibonacci of 3 is: " + fib(3));
console.log("Fibonacci of 4 is: " + fib(4));
console.log("Fibonacci of 5 is: " + fib(5));
console.log("Fibonacci of 6 is: " + fib(6));
console.log("Fibonacci of 7 is: " + fib(7));

///////////////////////////////////////////
// DONE!
///////////////////////////////////////////