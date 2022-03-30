const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n").map((item) => +item);

let valArr = input.map(input => input % 42);

solution(valArr);

function solution(arr) {
   /* // Set = 중복제거 (42배수의 나머지는 0인데 이걸 중복없이 넣으면 길이는 1이 된다.)
   const set = new Set(arr);
   arr = [...set];
   console.log(arr.length); */

   let difNum = []
   arr.forEach(num => {
      if (difNum.indexOf(num) === -1) {
         difNum.push(num);
      }
   });
   console.log(difNum.length);
}