const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ");

let A = BigInt(input[0]);
let B = BigInt(input[1]);

solution(A,B);

function solution(A, B) {
   console.log((A + B).toString());
}