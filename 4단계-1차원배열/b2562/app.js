const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n").map((item) => +item);

solution(input);

function solution(input) {
   let count = 0;
   let max = input[0];
   for (let i = 0; i < 9; i++) {
      if (max < input[i]) {
         max = input[i];
         count = i;
      }
   }
   console.log(max);
   console.log(count + 1);
}