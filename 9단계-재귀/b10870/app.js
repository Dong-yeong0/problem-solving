const fs = require("fs");

// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const filePath = "./input.txt"

const input = fs.readFileSync(filePath).toString().trim();

solution(+input);

function solution(value) {
   console.log(fibonacci(value));
}

function fibonacci(n) {
	if(n === 0) {
      return 0;
   }
   if(n === 1) {
      return 1;
   }
   return fibonacci(n - 1) + fibonacci(n - 2);
}