const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let N = Number(input[0]);
let values = input[1].split(" ").map(x => Number(x));

let max = values[0];
let min = values[0];


for (let i = 0; i < N; i++) {
   if (max < values[i]) {
      max = values[i];
   }

   if (min > values[i]) {
      min = values[i];
   }
}

console.log(`${min} ${max}`);
/* solution(N);

function solution(N) {
   console.log(N);
} */