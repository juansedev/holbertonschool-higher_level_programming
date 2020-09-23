#!/usr/bin/node
/*  script that reads and prints the content of a file */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
