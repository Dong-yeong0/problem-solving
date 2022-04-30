const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	let N = Number(input);
	let start = 1;
	let sum = 1;

	while(sum < N) {
		sum += 6 * start;
		start++;
	}

	console.log(start);
}