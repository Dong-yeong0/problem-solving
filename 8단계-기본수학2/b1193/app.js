const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim();

solution(+input);

function solution(value) {
	let i = 2;
	var result = [];

	while(true) {
		if(value % i == 0) {
			value /= i;
			result.push(i);
			i = 1;
		}
		i++;
		if(i > value){
			break;
		}
	}
	console.log(result.join("\n"));
}
