#!/usr/bin/node
const Square_ = require('./5-square.js');
class Square extends Square_ {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let i;
    let j;
    let string = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        string += c;
      }
      if (i < this.height - 1) {
        string += '\n';
      }
    }
    console.log(string);
  }
}
module.exports = Square;
