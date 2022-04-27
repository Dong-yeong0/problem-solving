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
	
	console.log(`${child}/${parents});

}
// 왜 틀린거지
