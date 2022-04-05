#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const size = this.height;
    for (let i = 0; i < size; i++) {
      console.log(c.repeat(size));
    }
  }
};
