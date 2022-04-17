const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

const taseCase = Number(input[0]);


solution(taseCase, input);

function solution(testCase, input) {
   let result = "";
   for(let i = 1; i <= taseCase; i++) {
      let loopCount = Number(input[i].split(" ")[0]);
      let str = input[i].split(" ")[1];

      for(let j = 0; j < str.length; j++) {
         for(let k = 0; k < loopCount; k++) {
            result += str[j];
         }
      }
      result += "\n";
   }
   console.log(result);
}