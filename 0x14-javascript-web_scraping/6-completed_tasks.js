#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonRes = JSON.parse(body);
    const taskByUser = {};
    for (const task of jsonRes) {
      if (task.completed) {
        if (task.userId in taskByUser) {
          taskByUser[task.userId] += 1;
        } else {
          taskByUser[task.userId] = 1;
        }
      }
    }
    console.log(taskByUser);
  }
});
