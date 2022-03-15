// 9498 시험 성적

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");


solution(+input[0]);

function solution(jumsoo) {
   if (90 <= jumsoo && jumsoo <= 100) {
      console.log("A");
   } else if (80 <= jumsoo && jumsoo <= 89) {
      console.log("B");
   } else if (70 <= jumsoo && jumsoo <= 79) {
      console.log("C");
   } else if (60 <= jumsoo && jumsoo <= 69) {
      console.log("D");
   } else {
      console.log("F");
   }
}

