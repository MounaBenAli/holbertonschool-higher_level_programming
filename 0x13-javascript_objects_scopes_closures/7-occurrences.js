#!/usr/bin/node
// Write a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let nb_occ = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nb_occ += 1;
    }
  }
  return nb_occ;
};
