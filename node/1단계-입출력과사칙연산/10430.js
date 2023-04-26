// 10430 나머지

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

let A = input[0];
let B = input[1];
let C = input[2];

console.log(`${(A + B) % C}\n${((A % C) + (B % C)) % C}\n${(A * B) % C}\n${((A % C) * (B % C)) % C}`);