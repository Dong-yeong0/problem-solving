const fs = require("fs");

// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const filePath = "./input.txt"

let input = fs.readFileSync(filePath).toString().trim().split("\n");

input = parseInt(input[0]);

const answer = [];

solution(input);

console.log(answer.join(""));


function solution(value) {
   for(let i = 0; i < value; i++) {
      for(let j = 0; j < value; j++) {
         countingStar(i, j, value);
      }
      answer.push("\n");
   }
}

function countingStar(i, j, value) {
   if(i % 3 == 1 && j % 3 == 1) {
      answer.push(" ");
   } else {
      if(value == 1) {
         answer.push("*");
      } else {
         countingStar(parseInt(i/3), parseInt(j/3), parseInt(value/3));
      }
      
   }
}