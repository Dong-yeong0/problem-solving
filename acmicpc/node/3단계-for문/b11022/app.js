const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

const valueArray = [];
for (let i = 1; i <= +input[0]; i++) {
   const tempValue = input[i].split(" ").map((item) => +item);
   valueArray.push({
      "A": tempValue[0],
      "B": tempValue[1]
   });
}

solution(+input[0], valueArray);

function solution(T, valueArray) {
   let result = "";
   for (let i = 0; i < T; i++) {
      const A = valueArray[i].A;
      const B = valueArray[i].B;
      result += `Case #${i + 1}: ${A} + ${B} = ${A + B} \n`;
   }
   console.log(result);
}
