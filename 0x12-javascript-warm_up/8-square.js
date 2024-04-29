#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let k = 0;
  while (k < x) {
    console.log('X'.repeat(x));
    k++;
  }
}
//@yego5
