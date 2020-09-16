#!/usr/bin/node
/* script that prints a message depending of the number of arguments passed */
const nArgs = process.argv.length;
if (nArgs === 2) {
  console.log('No argument');
} else if (nArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
