#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!isNaN(parseInt(arg1)) && !isNaN(parseInt(arg2))) {
  const result = add(parseInt(arg1), parseInt(arg2));
  console.log(result);
} else {
  console.log("Invalid input. Please provide two integers.");
}
