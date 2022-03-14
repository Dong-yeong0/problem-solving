// 10926 ??!
// trim() => 양쪽 끝 공백 제거

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim();

console.log(`${input}??!`);