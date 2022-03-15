// 2588 곱셈

//const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const fs = require('fs');
const filePath = "./input.txt";
let input = fs.readFileSync(filePath).toString().split('\n');

// 정수변환
input = input.map((item) => +item);

solution(input[0], input[1]);

function solution(A, B) {

   const stringB = String(B);

   const one = +stringB[2];
   const two = +stringB[1];
   const three = +stringB[0];
   console.log(A * one);
   console.log(A * two);
   console.log(A * three);
   console.log(A * B);

}
