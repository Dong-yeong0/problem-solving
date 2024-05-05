// 10869 사칙연산

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

let add = input[0] + input[1];
let minus = input[0] - input[1];
let multiple = input[0] * input[1];
let divide = parseInt(input[0] / input[1])
let remain = input[0] % input[1];

console.log(`${add}\n${minus}\n${multiple}\n${divide}\n${remain}`);

// `` (백틱) 활용 (노마더 코더 깅의)