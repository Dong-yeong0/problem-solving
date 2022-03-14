/*
* 입력 받기 30분 삽질 (??) readline 모듈도 있지만 fs가 쓰고 싶었다.
*/

/*
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let firstNumber = parseInt(input[0]); 
let secondNumber = parseInt(input[1]);

console.log(firstNumber + secondNumber);

*/

// 속도는 reduce가 빠르고 메모리는 살짝 더 잡아먹는다.
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

let answer = input.reduce((acc, cur) => {
   return acc + cur;
});

console.log(answer);
