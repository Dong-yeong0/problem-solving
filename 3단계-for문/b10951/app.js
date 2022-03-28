const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(input);

function solution(values) {
   let result = "";
   let i = 0;
   while (i < values.length - 1) {
      let numbers = values[i].split(" ").map((item) => +item);
      result += `${numbers[0] + numbers[1]}\n`;
      i++;
   }
   console.log(result);
}