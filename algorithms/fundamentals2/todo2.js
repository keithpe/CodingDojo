//****************************************************************************
// Threes and Fives
//****************************************************************************
// Create threesFives() that adds values from 100 and 4000000 (inclusive) 
// if that value is evenly divisible by 3 or 5 but not both. 
// Display the final sum in the console.
//****************************************************************************

function threesFives() {
    let sum = 0;
    for (idx = 100; idx <= 4000000; idx++) {
        // console.log(idx, 'idx % 3', idx % 3, 'idx % 5', idx % 5)
        if (((idx % 3 == 0) && !(idx % 5 == 0)) || (!(idx % 3) && (idx % 5))) {
            // console.log(idx, 'divisible by EITHER 3 OR 5 BUT NOT BOTH')
            sum += idx;
        }
    }
    console.log('Final Sum is:', sum)
}

console.log("\n**** threesFives ****")
threesFives()


//****************************************************************************
// Create betterThreesFives(start, end) that allows you to enter arbitrary 
// start and end values for your range. 
// Think of threesFives() as betterThreesFives(100,4000000).
//****************************************************************************

function betterThreesFives(start, end) {
    let sum = 0;
    for (idx = start; idx <= end; idx++) {
        // console.log(idx, 'idx % 3', idx % 3, 'idx % 5', idx % 5)
        if (((idx % 3 == 0) && !(idx % 5 == 0)) || (!(idx % 3) && (idx % 5))) {
            // console.log(idx, 'divisible by EITHER 3 OR 5 BUT NOT BOTH')
            sum += idx;
        }
    }
    console.log('Final Sum is:', sum)

}

console.log("\n**** betterThreesFives ****")
betterThreesFives(100, 4000000)
betterThreesFives(100, 400)


//****************************************************************************
// Generate Coin Change
//****************************************************************************
// Change is inevitable (especially when breaking a twenty). Make 
// generateCoinChange(cents). Accept a number of American cents, compute 
// and print how to represent that amount with the smallest number of coins. 
// Common American coins are pennies (1 cent), nickels (5 cents), 
// dimes (10 cents), and quarters (25 cents).
//****************************************************************************
// Example output, given (94):
//
// 94 cents can be represented by:
// quarters: 3
// dimes: 1
// nickels: 1
// pennies: 4
//****************************************************************************

function generateCoinChange(cents) {

    // Display original amount
    console.log('Original amount in cents:', cents)

    // remainingChange will store remaining change as we calculate each coin
    let remainingChange = cents;

    // Calculate coins from largest to smallest
    let quarters = Math.floor(cents / 25);
    remainingChange = cents % 25;
    console.log('quarters:', quarters)

    // Dimes
    let dimes = Math.floor(remainingChange / 10);
    remainingChange %= 10;
    console.log('dimes:', dimes)

    // Nickels
    let nickels = Math.floor(remainingChange / 5);
    remainingChange %= 5;
    console.log('nickels:', nickels)

    // Pennies
    let pennies = Math.floor(remainingChange / 1);
    remainingChange %= 1;
    console.log('pennies:', pennies)

    console.log('remaining change:', remainingChange)

}

console.log("\n**** generateCoinChange ****")
generateCoinChange(94)


//****************************************************************************
// generateCoinChange2 - Allow for half dollar and dollar coins in calc.
//****************************************************************************

function generateCoinChange2(cents) {

    // Display original amount
    console.log('Original amount in cents:', cents)

    // remainingChange will store remaining change as we calculate each coin
    let remainingChange = cents;

    // Calculate coins from largest to smallest

    // Dollar Coin
    let dollars = Math.floor(remainingChange / 100);
    remainingChange %= 100;
    console.log('dollar:', dollars)

    // Half Dollar Coin
    let halfDollar = Math.floor(remainingChange / 50);
    remainingChange %= 50;
    console.log('half dollar:', halfDollar)

    // Quarters
    let quarters = Math.floor(remainingChange / 25);
    remainingChange %= 25;
    console.log('quarters:', quarters)

    // Dimes
    let dimes = Math.floor(remainingChange / 10);
    remainingChange %= 10;
    console.log('dimes:', dimes)

    // Nickels
    let nickels = Math.floor(remainingChange / 5);
    remainingChange %= 5;
    console.log('nickels:', nickels)

    // Pennies
    let pennies = Math.floor(remainingChange / 1);
    remainingChange %= 1;
    console.log('pennies:', pennies)

    console.log('remaining change:', remainingChange)

}

console.log("\n**** generateCoinChange2 (include half dollar and dollar coins) ****")
generateCoinChange2(194)


//****************************************************************************
// Messy Math Mashup
//****************************************************************************
// Create a function messyMath(num) that will return the following sum: 
// add all integers from 0 up to the given num, except for the following 
// special cases of our count value:
//
// If current count (not num) is evenly divisible by 3, don’t add to the sum; 
// skip to the next count;
// 
// Otherwise, if the current count is evenly divisible by 7, include it twice 
// in sum instead of once;
// 
// Regardless of the above, if the current count is exactly 1/3 of num, 
// return -1 immediately.
// 
// For example, if given num is 4, return 7. If given num is 8, return 34. 
// If given num is 15, return -1.
// 
//****************************************************************************
// NOTE: I could not get this to work.
//****************************************************************************

function messyMath(num) {

    let sum = 0;
    let count = 0;
    for (let idx = 0; idx <= num; idx++) {

        count += 1;

        // Is current count evenly divisible by 3, don't add to sum
        // Count is from 1 - num, add 1 to idx to calculate count
        if (count % 3 == 0) {
            continue;
        }

        // OTHERWISE: if current count is evenly divisible by 7, include
        // it twice in sum instead of once
        else if (count % 7 == 0) {
            sum += (idx * 2);
        } else {
            sum += idx;
        }

        // REGARDLESS of above, if current count is exactly 1/3 of num 
        // return -1 immediately

        if (count == (num / 3)) {
            return -1
        }
    }
    return sum;
}

console.log("\n**** messyMath ****")
console.log('returnValue =', messyMath(4))
console.log('returnValue =', messyMath(8))
console.log('returnValue =', messyMath(15));




//****************************************************************************
// Twelve-Bar Blues
//****************************************************************************
// Write a function that console.logs the number 1, then "chick", 
// then "boom", then "chick", then 2, then "chick", "boom", "chick" – 
// continuing the same cycle for each number up to (including) 12.
//****************************************************************************

function twelveBarBlues() {

    for (let idx = 1; idx <= 12; idx++) {
        console.log(idx, 'chick', 'boom', 'chick');
    }

}


console.log("\n**** Twelve-Bar Blues ****")
twelveBarBlues()


//****************************************************************************
// Fibonacci
//****************************************************************************
// Create a function to generate Fibonacci numbers. In this famous 
// mathematical sequence, each number is the sum of the previous two, 
// starting with values 0 and 1. 
//
// Your function should accept one argument, an index into the sequence 
// (where 0 corresponds to the initial value, 4 corresponds to the value four 
// later, etc). 
//
// Examples: fibonacci(0) = 0 (given), 
// fibonacci(1) = 1 (given), 
// fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), 
// fibonacci(3) = 2 (fib(1)+fib(2), or 1+1), 
// fibonacci(4) = 3 (1+2), 
// fibonacci(5) = 5 (2+3), 
// fibonacci(6) = 8 (3+5), 
// fibonacci(7) = 13 (5+8), etc.
//****************************************************************************

function fibonacci(num) {

    if (num <= 1) {
        return 1;
    } else {
        return fibonacci(num - 1) + fibonacci(num - 2)
    }
}

console.log("\n**** Fibonacci ****")
console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(3));
console.log(fibonacci(4));
console.log(fibonacci(5));
console.log(fibonacci(6));
console.log(fibonacci(7));
console.log(fibonacci(8));

//****************************************************************************
// Sum to One Digit
//****************************************************************************
// Kaitlin sees beauty in numbers, but also believes that less is more. 
// Implement sumToOne(num) that sums a given integer’s digits repeatedly 
// until the sum is only one digit. Return that one-digit result. 
//
// Example: sumToOne(928) returns 1, because 9+2+8 = 19, 
// then 1+9 = 10, then 1+0 = 1.
//****************************************************************************

function sumToOne(num) {
    if (num < 10) {
        return num
    }
    let sum = 0;
    let digit = 0;
    while (num > 9) {
        digit = num % 10;
        digit = Math.floor(digit);
        console.log('digit', digit)
        num /= 10;
        num = Math.floor(num)
        sum += digit
        console.log('INSIDE LOOP: sum', sum, 'digit', digit, 'num', num)
    }
    sum += num;
    console.log('OUTSIDE LOOP: sum', sum, 'digit', digit, 'num', num)
    return sumToOne(sum)
}

console.log("\n**** sumToOne ****")
console.log(sumToOne(928));
console.log(sumToOne(346));


//****************************************************************************
// Clock Hand Angles
//****************************************************************************
// Regardless of how hard a Dojo student works (and they should work hard), 
// they need time now and then to unwind – like hands on a clock. Traditional 
// clocks are increasingly uncommon, but most can still read an analog 
// clock’s hands of hours, minutes and seconds. 
// 
// Create clockHandAngles(seconds) that, given a number of seconds since 
// 12:00:00, prints angles (in degrees) of the hour, minute and second hands. 
// 
// As a review, 360 degrees form a full rotation. For input of 3600 secs 
// (equivalent to 1:00:00), print "Hour hand: 30 degs. Minute hand: 0 degs. 
// Second hand: 0 degs." 
// 
// For an input parameter seconds of 119730 
// (which is equivalent to 9:15:30 plus 24 hours!), you should log 
// "Hour hand: 277.745 degs. Minute hand: 93 degs. Second hand: 180 degs." 
// 
//****************************************************************************
// Note: in the second example, the angle for the minute hand is not simply 
// 90 degrees; it has advanced a bit further, because of the additional 30 
// seconds in that minute so far.
//****************************************************************************
// Second: also calculate and print degrees for an additional “week hand” 
// that rotates once each week. 
//****************************************************************************

function clockHandAngles(seconds) {

}

console.log("\n**** clockHandAngles ****")
clockHandAngles(3600)
clockHandAngles(119730)

//****************************************************************************
// Is Prime
//****************************************************************************
// Return whether a given integer is prime. Prime numbers are only evenly 
// divisible by themselves and 1. 
// 
// Many highly optimized solutions exist, but for now, just create one that 
// is easy to understand and debug.
//****************************************************************************

function isPrime(n) {

    if (n === 1) {
        return false;
    } else if (n === 2) {
        return true;
    } else {
        for (var x = 2; x < n; x++) {
            if (n % x === 0) {
                return false;
            }
        }
        return true;
    }
}

console.log("\n**** isPrime ****")
console.log(isPrime(23))
console.log(isPrime(24))