// 2753 윤년

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");


solution(+input[0]);

function solution(year) {
   if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0) {
      console.log("1");
      return;
   }
   console.log("0");

}