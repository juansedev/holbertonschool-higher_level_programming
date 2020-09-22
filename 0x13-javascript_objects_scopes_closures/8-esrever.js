#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = list.length, j = 0; i > 0; i--, j++) {
    reverseList[j] = list[i - 1];
  }
  return reverseList;
};
