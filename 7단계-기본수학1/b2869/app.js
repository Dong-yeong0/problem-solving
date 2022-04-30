const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ");

solution(input);

function solution(input) {
	let A = Number(input[0]);
	let B = Number(input[1]);
	let V = Number(input[2]);
	let days = 0;

	days = Math.ceil((V - B) / (A - B));
	
	console.log(days);
}