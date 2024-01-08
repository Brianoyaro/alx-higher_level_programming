#!/usr/bin/node
const args = process.argv;
let small = args[2];
let big = args[2];
let i;
const length = args.length;
if (length === 2 || length === 3) {
  console.log(0);
} else {
  for (i = 2; i < args.length; i++) {
    if (args[i] > big) {
      small = big;
      big = args[i];
    } else if (args[i] < big && args[i] > small) {
      small = args[i];
    }
  }
  console.log(small);
}
