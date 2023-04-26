// 1330 두 수 비교하기
//const filePath = "./input.txt";

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

let input = fs.readFileSync(filePath).toString().trim().split("\n");


solution(input[0], input[1]);

function solution(A, B) {
   console.log(A > B ? ">" : A < B ? "<" : "==");
}