#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

let text = '';

const array = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

for (let i = 0; i < array.length; i++) {
  text = array[i];
  console.log(text);
}
