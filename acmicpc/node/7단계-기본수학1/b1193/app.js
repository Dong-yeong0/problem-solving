
// 왜 틀린거지
const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().map((item) => +item);

solution(input);

function solution(input) {
	let line = 0;
	let maxValue = 0;

	while(maxValue < N) {
		line++;
		maxValue += line;
	}
	
	let index = N - (maxValue - line);
	
	if(line % 2 == 0) {
		child = index;
		parents = (line + 1) -child;
	} else {	
		child = (line + 1) - index;
		parents = (line + 1) - child;
	}
	
	console.log(`${child}/${parents}`);

}


let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
let number = Number(input);
let value = 1;
while (true) {
	number -= value;
	if (number <= 0) {
		number += value;
		break;
	}
	value++;
}

if (value % 2 === 1) {
	console.log(`${value - (number - 1)}/${1 + (number - 1)}`);
} else {
	console.log(`${1 + (number - 1)}/${value - (number - 1)}`);
}
