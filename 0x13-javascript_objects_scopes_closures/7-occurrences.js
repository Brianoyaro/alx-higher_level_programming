#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let val = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      val += 1;
    }
  }
  return (val);
};
