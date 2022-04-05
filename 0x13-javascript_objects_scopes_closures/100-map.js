#!/usr/bin/node
// imports an array and computes a new array

let list = require('./100-data.js').list;
console.log(list);

let newArr = [];
for (let i = 0; i < list.length; i++) {
  newArr = list.map((x, i) => x * i);
}
console.log(newArr);

