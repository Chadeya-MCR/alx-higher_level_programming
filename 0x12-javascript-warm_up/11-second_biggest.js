#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (i, j) { return j - i; })[1];
  console.log(second);
}
//@yego5
