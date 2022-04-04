#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
// If the argument can’t be converted to an integer, print “Not a number”

if (parseInt(process.argv.slice(2))) {
  console.log('My number:', parseInt(process.argv.slice(2)));
} else {
  console.log('Not a number');
}
