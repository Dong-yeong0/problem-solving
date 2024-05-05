// 재귀 - 팩토리얼
const fs = require("fs");

// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const filePath = "./input.txt"

const input = fs.readFileSync(filePath).toString().trim();

solution(Number(input))

function solution(value) {
	console.log(factorial(value));
}

function factorial(n) {
	if(n <= 1) {
		return 1;
	}

	return n * factorial(n - 1);
}