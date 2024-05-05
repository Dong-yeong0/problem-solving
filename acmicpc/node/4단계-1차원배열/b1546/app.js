const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let numbers = input[1].split(" ").map((item) => +item);

numbers.sort((a, b) => a - b);
solution(+input[0], numbers);

function solution(N, numbers) {
   let sum = 0;
   const maxValue = numbers[N - 1];
   for (let i = 0; i < N; i++) {
      sum += numbers[i] / maxValue * 100;
   }
   console.log(sum / N);
}