// 2480 주사위 세개

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

solution(input[0], input[1], input[2])

function solution(A, B, C) {
   console.log(A, B, C);
}