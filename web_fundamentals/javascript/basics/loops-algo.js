// loops-algo (from javascript basics section)

// Print odds 1-20
for (i = 1; i <= 20; i++) {
  if (i % 2 !== 0) {
    // Number is odd
    console.log(i);
  }
}

// Sum and print 1-5
// The expected output will be: Num: 1, Sum: 1, Num: 2, Sum: 3, Num: 3, Sum: 6, Num: 4, Sum: 10, Num: 5, Sum: 15
var sum = 0;
for (num = 1; num <= 5; num++) {
  sum += num;
  console.log('Num:', num, 'Sum:', sum);
}