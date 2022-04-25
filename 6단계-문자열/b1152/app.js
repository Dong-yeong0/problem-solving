const fs = require("fs");

//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ");

solution(input);

function solution(value) {
   let wordCount = 0;

   for(let i = 0; i < value.length; ++i) {
      if(input[i] !== "") {
         wordCount++;
      }
   }

   console.log(wordCount);
}