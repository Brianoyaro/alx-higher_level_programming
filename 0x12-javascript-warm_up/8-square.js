#!/usr/bin/node
const args = process.argv;
const length = parseInt(args[2]);
let string = '';
let i;
let j;
let flag = 0;
if (length % 1 === 0) {
  for (i = 0; i < length; i++) {
    for (j = 0; j < length; j++) {
      string += 'X';
    }
    if (flag < (length - 1)) {
      string += '\n';
    }
    flag += 1;
  }
  console.log(string);
} else {
  console.log('Missing size');
}
