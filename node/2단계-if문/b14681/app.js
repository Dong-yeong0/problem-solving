// 14681 사분면 고르기 (fs 모듈 사용 시 에러)

/* const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);


solution(input[0], input[1]);

function solution(x, y) {
   let num = 0;
   if (x > 0 && y > 0) {
      num = 1;
   }
   if (x < 0 && y > 0) {
      num = 2;
   }
   if (x < 0 && y < 0) {
      num = 3;
   }
   if (x > 0 && y < 0) {
      num = 4;
   }
   console.log(num);
} */

const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

let input = [];

rl.on('line', function (line) {
   input.push(line);
}).on('close', function () {
   let firstNum = Number(input[0]);
   let secondNum = Number(input[1]);

   if (firstNum > 0 && secondNum > 0) {
      console.log(1);
   } else if (firstNum < 0 && secondNum > 0) {
      console.log(2);
   } else if (firstNum < 0 && secondNum < 0) {
      console.log(3);
   } else if (firstNum > 0 && secondNum < 0) {
      console.log(4);
   }

   process.exit();
});