#!/usr/bin/node
// imports an array and computes a new array

let list = require('./100-data.js').list;
console.log(list);

let newArr = [];
newArr = list.map((x, i) => x * i);
console.log(newArr);

