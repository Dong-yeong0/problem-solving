const fs = require("fs");

//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().toLowerCase();

solution(input);

function solution(values) {
   const result = new Array(26).fill(0);

   for(let i = 0; i < values.length; i++) {
      result[values.charCodeAt(i) - 97]++;
   }

   const max = Math.max(...result);
   const index = result.indexOf(max);
   
   let isSame = false;

   for(let j = 0; j < 26; j++) {
      if(result[j] === max && index != j) {
         isSame = true;
         break;
      }
   }
   console.log(isSame ? "?" : String.fromCharCode(result - 65));
}