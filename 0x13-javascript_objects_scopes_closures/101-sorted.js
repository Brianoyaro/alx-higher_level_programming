#!/usr/bin/node
const dict = require('./101-data.js').dict;
const obj = {};
let flag = 0;
let key_;
for (const [key, value] of Object.entries(dict)) {
  for (key_ in obj) {
    if (parseInt(key_) === value) {
      flag = 1;
      obj[value].push(key);
    }
  }
  if (flag === 0) {
    obj[value] = [key];
  }
  flag = 0;
}
console.log(obj);
