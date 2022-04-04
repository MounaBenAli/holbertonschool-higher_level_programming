#!/usr/bin/node
//  prints prints a square

const size = process.argv.slice(2);
let square = '';

if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
} else {
  console.log('Missing size');
}
