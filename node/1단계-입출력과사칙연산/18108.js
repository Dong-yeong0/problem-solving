// 18108 1998년생인 내가 태국에서는 2541년생?!

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim();

console.log(parseInt(input) - 543);

// 불기 : 서기 + 544 -> 서기 = 불기 - 544 (근데 결과 값 1 적어서 1덜 빼줌)