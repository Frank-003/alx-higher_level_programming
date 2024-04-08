#!/usr/bin/node
function factorial(n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (n < 0) {
    return "Factorial is not defined for negative numbers.";
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const argument = process.argv[2];
const result = factorial(argument);
console.log(result);
