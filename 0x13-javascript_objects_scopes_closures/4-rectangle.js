#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        string += 'X';
      }
      if (i < this.height - 1) {
        string += '\n';
      }
    }
    console.log(string);
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
