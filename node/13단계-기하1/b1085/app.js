const fs = require("fs");

// const filePath = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ").map((item) => +item);

let [x, y, w, h] = input;

solution(x, y, w, h);

function solution(x, y, w, h) {
   let xDiff = w - x;
   let yDiff = h - y;

   let result = [x, y, xDiff, yDiff];

   console.log(Math.min.apply(null, result));
}