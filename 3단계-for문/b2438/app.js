const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(+input[0]);

function solution(N) {
   let result = "";
   for (let i = 0; i < N; i++) {
      for (let j = 0; j <= i; j++) {
         result += "*";
      }
      result += "\n";
   }
   console.log(result);
}