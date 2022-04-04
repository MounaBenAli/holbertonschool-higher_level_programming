#!/usr/bin/node
// searches the second biggest integer in the list of arguments

// let's consider an array of argv
const strArr = process.argv.slice(2, process.argv.length);

if (process.argv.length <= 3) {
  console.log('0');
} else {
// let's convert it to a real array of numbers, not of strings :
  const intArray = strArr.map(Number);
  // now let's sort it and take the second element :
  const secondMax = intArray.sort(function (a, b) { return b - a; })[1];
  console.log(secondMax);
}
