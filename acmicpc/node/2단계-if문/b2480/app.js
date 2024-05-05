// 2480 주사위 세개

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

input.sort();

solution(input[0], input[1], input[2])

function solution(A, B, C) {
   let reward = 0;
   if (A === B && B === C) {
      reward = 10000 + (A * 1000);
   } else if (A === B || B === C) {
      reward = 1000 + (B * 100);
   } else {
      reward = C * 100;
   }
   console.log(reward);
}