const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let count = Number(input[0]);
let numbers = input[1].split(' ').map((item) => +item);


numbers.sort((a, b) => a - b);      // 오름차순 정렬  (down -> up ASC) 이게 좀 신기하네 a-b 가 오름차순이고 b-a가 DESC네

// 맨 마지막에는 출력하는게 마지막 index - 1 이니까 
console.log(`${numbers[0]} ${numbers[count - 1]}`);