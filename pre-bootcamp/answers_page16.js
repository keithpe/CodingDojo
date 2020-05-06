// Setting and Swapping
function settingAndSwapping() {
  var myNumber = 42;
  var myName = "Keith";
  var temp = myNumber;
  myNumber = myName;
  myName = temp;
  console.log('myNumber', myNumber);
  console.log('myName', myName);
}

// Print -52 to 1066
function printMinus52To1066() {
  for (var i = -52; i <= 1066; i++) {
    console.log(i);
  }
}

// Don't worry, be Happy
function beCheerful() {
  var message = 'good morning';
  for (var i = 1; i <= 98; i++) {
    console.log(i + ') ' + message);
  }
}
// Multiples of Three - but not all
function multiplesOfThreeButNotAll() {
  for (var i = -300; i <= 0; i++) {
    if ((i !== -3) && (i !== -6)) {
      console.log(i);
    }
  }
}

// Printing Integers with While
function printingIntegersWithWhile() {
  var counter = 2000;
  while (counter <= 5280) {
    console.log(counter);
    counter++;
  }
}

// Printing Integers with While (version 2, using break)
function printingIntegersWithWhile2() {
  var counter = 2000;
  while (true) {
    console.log(counter);
    counter++;
    if (counter > 5280) {
      break;
    }
  }
}

// You say it's your birthday
function youSayItsYourBirthday(num1, num2) {
  var birthMonth = 4;
  var birthDay = 23;
  if ((num1 === birthMonth || num2 === birthMonth) &&
    (num2 === birthDay || num1 === birthDay)) {
    console.log('How did you know?');
  } else {
    console.log('Just another day...');
  }
}

function leapYear(year) {
  // Divisible by 4, leap year...
  if (year % 4 === 0) {
    // Unless it's divisible by 100...
    // ...EXCEPT if it's divisible by 400.
    if (year % 100 !== 0 || year % 400 === 0) {
      console.log('Happy Leap Year!!')
    }
  }
}

// Print And Count
// Print all integer multiples of 5, from 512 to 4096.
// Afterward, also log how many there were.
function printAndCount() {
  var count = 0;
  for (var i = 512; i <= 4096; i++) {
    if (i % 5 === 0) {
      console.log(i);
      count++;
    }
  }
  console.log('I counted ' + count + ' values.');
}

// Print multiples of 6 up to 60,000, using a WHILE.
function multiplesOfSix() {
  var multipleOfSix = 6;
  while (multipleOfSix <= 60000) {
    console.log(multipleOfSix)
    multipleOfSix += 6;
  }
}

// Print integers 1 to 100. If divisible by 5, print
// "Coding" instead. If by 10, also print " Dojo".
function countingTheDojoWay() {
  message5 = 'Coding';
  message10 = 'Coding Dojo';
  for (var i = 1; i <= 100; i++) {
    if (i % 10 === 0) {
      console.log(message10);
    } else if (i % 5 === 0) {
      console.log(message5)
    } else {
      console.log(i);
    }
  }
}

// What Do You Know?
// Your function will be given an input parameter incoming. 
// Please console.log this value.
function whatDoYouKnow(input) {
  console.log(input);
}

// Whoa, That Sucker’s Huge...
// Add odd integers from -300,000 to 300,000, and console.log 
// the final sum. Is there a shortcut?
function whoaThatSuckersHuge1() {
  var sum = 0;
  for (var i = -300000; i <= 300000; i++) {
    if (Math.abs(i % 2) !== 0) {
      sum += i;
    }
  }
  console.log('(1) Final sum is: ' + sum);
}

// Shortcut? Start with odd add two get next odd
// No check for odd needed?
function whoaThatSuckersHuge2() {
  var sum = 0;
  for (var i = -299999; i <= 300000; i += 2) {
    sum += i;
  }
  console.log('(2) Final sum is: ' + sum);
}

// Countdown by Fours
// Log positive numbers starting at 2016, counting
// down by fours (exclude 0), without a FOR loop.
function countDownByFours() {
  var countDown = 2016;
  while (countDown > 0) {
    console.log(countDown);
    countDown -= 4;
  }
}

// Flexible Countdown
// Based on earlier “Countdown by Fours”, 
// given lowNum, highNum, mult, 
// print multiples of mult from highNum down to lowNum, 
// using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
function flexibleCountDown(lowNum, highNum, mult) {
  for (var i = highNum; i >= lowNum; i -= mult) {
    console.log(i);
  }
}

// The Final Countdown
// This is based on “Flexible Countdown”. 
// The parameter names are not as helpful, but the problem is essentially 
// identical; don’t be thrown off! 
// Given 4 parameters (param1,param2,param3,param4), 
// print the multiples of param1, starting at param2 and extending 
// to param3. One exception: if a multiple is equal to param4, 
// then skip (don’t print) it. 
// Do this using a WHILE. 
// Given (3,5,17,9), print 6,12,15 
// (which are all of the multiples of 3 between 5 and 17, 
// and excluding the value 9).
// param1=mult, param2=start, param3=end, param4=skip this value
function theFinalCountDown(param1, param2, param3, param4) {
  for (var i = param2; i <= param3; i++) {
    if ((i % param1) === 0) {
      if (i !== param4) {
        console.log(i);
      }
    }
  }
}

console.log('** settingAndSwapping **');
settingAndSwapping();
console.log('** printMinus52To1066 **');
printMinus52To1066();
console.log('** beCheerful **');
beCheerful();
console.log('** multiplesOfThreeButNotAll **');
multiplesOfThreeButNotAll();
console.log('** printingIntegersWithWhile **');
printingIntegersWithWhile();
console.log('** printingIntegersWithWhile2 **');
printingIntegersWithWhile2();
console.log('** youSayItsYourBirthday **');
youSayItsYourBirthday(4, 23); // My Birthday
youSayItsYourBirthday(23, 4); // My Birthday
youSayItsYourBirthday(1, 22); // Not my Birthday
youSayItsYourBirthday(22, 1); // Not my Birthday
console.log('** leapYear **');
leapYear(2004);
console.log('** printAndCount **');
printAndCount();
console.log('** multiplesOfSix **');
multiplesOfSix();
console.log('** countingTheDojoWay **');
countingTheDojoWay();
console.log('** whatDoYouKnow **');
whatDoYouKnow('Howdy');
console.log('** whoaThatSuckersHuge**');
whoaThatSuckersHuge1();
whoaThatSuckersHuge2();
console.log('** countDownByFours **');
countDownByFours();
console.log('** flexibleCountDown **');
flexibleCountDown(2, 9, 3);
console.log('** theFinalCountDown **');
theFinalCountDown(3, 5, 17, 9);
console.log('** Done!**');