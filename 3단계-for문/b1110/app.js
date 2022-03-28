const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(+input[0]);

function solution(input) {
   let result = 0;
   let num = input;
   let sum;
   while (true) {
      result++;
      sum = Math.floor(num / 10) + num % 10;
      num = (num % 10) * 10 + sum % 10;
      if (input === num) {
         break;
      }
   }
   console.log(result);
}