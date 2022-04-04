#!/usr/bin/node
// prints a square

const size = parseInt(process.argv.slice(2));

if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
