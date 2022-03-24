const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(+input[0]);

function solution(N) {
   let result = "";
   for (let i = 1; i <= N; i++) {
      result += i + "\n";
   }
   console.log(result);
}
// 마지막에 \n 더 붙는데 맞추네?
// 이 문제 for 안에서 console 찍으면 시간초과 걸리고 한번에 담아서 해야되는 문제