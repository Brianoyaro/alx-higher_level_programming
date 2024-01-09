#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let j = 0;
  const arr = [];
  for (i = list.length - 1; i >= 0; i--) {
    arr[j] = list[i];
    j += 1;
  }
  return (arr);
};
