const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ");

let A = Number(input[0]);
let B = Number(input[1]);
let C = Number(input[2]);


solution(A,B,C);

function solution(A, B, C) {
   let N = A / (C - B);

   let answer = Math.floor(N) + 1;

   B >= C ? (answer = -1) : answer;

   console.log(answer);
}
