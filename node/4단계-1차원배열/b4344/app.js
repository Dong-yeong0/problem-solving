const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(+input[0]);

function solution(testCase) {
   for (let i = 1; i <= testCase; i++) {
      let people = 0;
      let sum = 0;

      scores = input[i].split(" ").map((item) => +item);
      const n = scores[0];

      for (let j = 1; j <= n; j++) {
         sum += scores[j];
      }

      const avg = sum / n;

      for (let k = 1; k <= n; k++) {
         if (scores[k] > avg) {
            people++;
         }
      }
      console.log(`${((people / n) * 100).toFixed(3)}%`)
   }
}