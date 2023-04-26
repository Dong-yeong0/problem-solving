const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split(" ");

solution(input);

function solution(input) {
   let num1 = +input[0].split("").reverse().join("");
   let num2 = +input[1].split("").reverse().join("");
   console.log(num1 > num2 ? num1 : num2);
}