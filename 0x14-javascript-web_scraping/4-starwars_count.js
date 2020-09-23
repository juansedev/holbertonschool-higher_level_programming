#!/usr/bin/node
/*  script that reads and prints the content of a file */
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const reqJson = JSON.parse(body).results;
    let count = 0;
    for (const film of reqJson) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
