#!/usr/bin/node
const args = process.argv;
let i = 0;
for (i = 0; args[i]; i++) {
  continue;
}
if (i === 2) {
  console.log('No argument');
}
if (i >= 3) {
  console.log(args[2]);
}
