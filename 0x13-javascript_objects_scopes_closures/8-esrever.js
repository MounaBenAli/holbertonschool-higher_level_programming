#!/usr/bin/node
// Write a function that returns the reversed version of a list:

exports.esrever = function (list) {
  const output = [];
  for (let i = list.length - 1; i > -1; i--) {
    output.push(list.pop());
  }
  return output;
};
