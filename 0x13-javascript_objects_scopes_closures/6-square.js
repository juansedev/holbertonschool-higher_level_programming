#!/usr/bin/node
/*  class Square that defines a square and inherits from Rectangle of
 *  4-rectangle.js:
 *  You must use the class notation for defining your class and extends
 *  The constructor must take 1 argument: size
 *  The constructor of Rectangle must be called (by using super()
 *  Create an instance method called charPrint(c) that prints the rectangle
 *  using the character c If c is undefined, use the character X
*/

const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
