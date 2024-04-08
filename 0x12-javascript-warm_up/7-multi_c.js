#!/usr/bin/node
const x = process.argv[2];

if (!isNaN(parseInt(x))) {
  const numberOfOccurrences = parseInt(x);
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
