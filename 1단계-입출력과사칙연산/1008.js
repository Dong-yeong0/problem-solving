// 1008 A / B

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

let result = input.reduce((acc, cur) => {
   return acc / cur;
});

console.log(parseFloat(result));

/*
* Input : 1 3
* 백준 출력 : 0.33333333333333333333333333333333
* 내 출력   : 0.3333333333333333
* 상대오차가 10^-9 이하면 허락한다니 맞네
*/
