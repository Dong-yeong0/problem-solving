const fs = require("fs");

// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const filePath = "./input.txt"

const input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);

function solution(value) {

	value.shift();
	
	value.sort((a, b) => a - b);
	
	for(let i = 0; i < value.length; i++) {
		console.log(value[i]);
	}

}