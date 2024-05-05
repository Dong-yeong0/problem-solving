// 2884 알람시계

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

const input = fs.readFileSync(filePath).toString().split(" ").map(Number);

solution(input[0], input[1]);

function solution(H, M) {
   M -= 45;
   if (M < 0) {
      M += 60;
      H -= 1;
   }
   if (H < 0) {
      H = 23;
   }
   console.log(H, M);
}