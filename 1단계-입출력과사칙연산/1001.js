// 1001 A - B

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

let result = input.reduce((acc, cur) => {
   return acc - cur;
});

console.log(result);