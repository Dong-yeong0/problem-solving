const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let firstLine = input[0].split(" ").map((item) => +item);
let values = input[1].split(" ").map((item) => +item);

solution(firstLine, values);

function solution(firstLine, values) {
   result = [];
   for (let i = 0; i < firstLine[0]; i++) {
      if (values[i] < firstLine[1]) {
         result.push(values[i]);
      }
   }
   console.log(result.join(" "));
}