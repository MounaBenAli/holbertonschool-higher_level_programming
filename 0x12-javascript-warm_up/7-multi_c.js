#!/usr/bin/node
//  prints x times “C is fun”

const times = process.argv.slice(2);
let i = 0;
const str = 'C is fun';

if (parseInt(times)) {
  while (i < times) {
    i += 1;
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
