// Practice using a T-diagram to go through the following code snippets and predict the output.
// Once you're done run your code and see if your prediction was correct.  
// Create a .js file with the code snippets and your predicted output and upload it once you're done.

// Predict 1: 8,6,7,5,3,0,9
console.log("Predict 1:");
var arr = [8, 6, 7, 5, 3, 0, 9]
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
console.log("Final value of i: " + i);

// Predict 2: "that is odd", "that is odd", 8,4,2,0,"that is odd"
console.log("Predict 2:");
var arr = [7, 3, 8, 4, 2, 0, 1];
for (var i = 0; i < arr.length; i++) {
  if (arr[i] % 2 == 0) {
    console.log(arr[i]);
  }
  else {
    console.log("That is odd!");
  }
}

// Predict 3:
// arr=[-1,-3,-8,5,"zero",2,-4,1] 
// newArr=[-5,-2,-1]
console.log("Predict 3:");
var arr = [1, 3, 8, -5, 0, -2, 4, -1];
var newArr = [];
for (var i = 0; i < arr.length; i++) {
  if (arr[i] < 0) {
    newArr.push(arr[i]);
    arr[i] = arr[i] * -1;
  }
  else if (arr[i] == 0) {
    arr[i] = "Zero";
  }
  else {
    arr[i] = arr[i] * -1;
  }
}
console.log(arr);
console.log(newArr);