// Predict 1
// This loop should display: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
for (var num = 0; num < 15; num++) {
  console.log(num);
}

// Predict 2
// This loop should display: 3,9
// i values: 1,3,5,7,9,11
for (var i = 1; i < 10; i += 2) {
  if (i % 3 == 0) {
    console.log(i);
  }
}

// Predict 3
// This loop should display: 1,4,5,8,10,11,14,16
// J values: 1,2,4,5,6,8,9,10,11,12,14,15,16
for (var j = 1; j <= 15; j++) {
  if (j % 2 == 0) {
    j += 2;
  }
  else if (j % 3 == 0) {
    j++;
  }
  console.log(j);
}