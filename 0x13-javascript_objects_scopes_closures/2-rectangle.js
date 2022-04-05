#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle
// The constructor must take 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
