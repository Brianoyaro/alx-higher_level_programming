#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if ((num % 1) === 0) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
