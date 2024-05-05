const fs = require("fs");

// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const filePath = "./input.txt"

const input = fs.readFileSync(filePath).toString().trim().split("\n");

let testCase = Number(input[0]);
let numbers  = input[1].split(" ").map((item) => +item);

solution(testCase, numbers)

function solution(N, values) {

	let result = 0;

	for(let i = 0; i < N; i++) {
		// Todo 1은 제외
		if(values[i] === 1) {
			continue;
		} else {
			let count = 0;
			for(let j = 2; j < values[i]; j++) {
				if(values[i] % j === 0) {
					count++;
				}
			}
			if(count === 0) {
				result++;
			}
		}
	}

	console.log(result);
}