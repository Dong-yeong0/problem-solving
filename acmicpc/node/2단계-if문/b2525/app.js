// 2884 알람시계

const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split("\n");

let currentHour = input[0].split(" ")[0];
let currentMin = input[0].split(" ")[1];
let cookTime = input[1];

solution(+currentHour, +currentMin, +cookTime);

function solution(H, M, cook) {

   H += parseInt(cook / 60);
   M += parseInt(cook % 60);

   while (true) {

      if (H < 24 && M < 60) {
         break;
      }

      if (H >= 24) {
         H -= 24;
      } else {
         M -= 60;
         H++;
      }

   }
   console.log(H, M);

}