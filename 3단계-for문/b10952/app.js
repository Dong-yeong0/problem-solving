const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");


let values = [];
for (let i = 0; i < input.length; i++) {
   values.push(input[i].split(" ").map((item) => +item));
}

solution(values);

function solution(values) {
   let i = 0;
   let isNotZero = true;
   let result = "";
   while (isNotZero) {
      if (i !== 0) {
         result += "\n";
      }
      let sum = values[i][0] + values[i][1];

      if (sum === 0) {
         isNotZero = false;
      } else {
         result += sum;
         i++;
      }
   }
   console.log(result);
}