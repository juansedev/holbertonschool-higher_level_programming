#!/usr/bin/node
/*  script that reads and prints the content of a file */
const request = require('request');
const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log(response.statusCode);
});
