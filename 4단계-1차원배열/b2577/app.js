const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

solution(input);

function solution(input) {
   let value = String(input[0] * input[1] * input[2]);

   for (let i = 0; i < 10; i++) {
      let count = 0;

      for (let j = 0; j < value.length; j++) {
         if (Number(value[j]) === i) {
            count++;
         }
      }
      console.log(count);
   }
}