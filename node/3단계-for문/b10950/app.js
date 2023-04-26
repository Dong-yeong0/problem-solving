// 10950 A + B -3

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
function solution(testCase, valueArray) {
   for (let i = 0; i < testCase; i++) {
      const A = valueArray[i].A;
      const B = valueArray[i].B;
      console.log(A + B);
   }
}