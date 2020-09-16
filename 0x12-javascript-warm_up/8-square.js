#!/usr/bin/node
/* script that prints a square */
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
