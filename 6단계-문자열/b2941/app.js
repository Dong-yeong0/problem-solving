const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";
let input = fs.readFileSync(filePath).toString().trim();

let croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];

function solution(values) {
   
   for(let alphabet of croatia) {
      values = values.split(alphabet).join("Q");
   }
   
   return values.length;
   // return values;
}

console.log(solution(input));


/* const elements = ['Fire', 'Air', 'Water'];

// join() => 배열의 모든 요소를 연결해 하나의 문자열로 만들어줌 (return String)

console.log(elements.join());
// expected output: "Fire,Air,Water"

console.log(elements.join(''));
// expected output: "FireAirWater"

console.log(elements.join('-'));
// expected output: "Fire-Air-Water" */