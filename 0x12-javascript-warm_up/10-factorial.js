#!/usr/bin/node
const args = process.argv;
function fct (x) {
  if (x === 1) {
    return (1);
  }
  return (x * fct(x - 1));
}
if (args.length === 2) {
  console.log(1);
} else {
  const x = parseInt(args[2]);
  console.log(fct(x));
}
